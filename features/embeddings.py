"""Foundation-model embeddings (Phase 2) — scaffold.

Pipeline: translate genome ORFs -> ESM-2 protein embeddings -> mean-pool to one
vector per virus -> lightweight classifier (same eval harness as composition).

This module is a working scaffold but its heavy deps (torch, fair-esm) live in
the optional ``embeddings`` extra:

    uv pip install -e ".[embeddings]"

It is intentionally CPU/MPS-friendly (ESM-2 ``t12_35M`` / ``t30_150M`` run on an
M-series Mac for a few thousand short viral proteins). Model choice and pooling
strategy are part of the Phase-2 plan — see FINDINGS.md / the model design notes.
"""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
import pandas as pd

from zoonotic.config import FEATURES_CACHE
from zoonotic.ncbi import genome_path

log = logging.getLogger("zoonotic.features.embeddings")

DEFAULT_ESM_MODEL = "esm2_t30_150M_UR50D"  # 150M params; good CPU/MPS tradeoff
MIN_PROTEIN_AA = 30
MAX_PROTEINS_PER_VIRUS = 30  # cap pooling cost for large/segmented genomes


def translate_orfs(fasta_path: Path, min_aa: int = MIN_PROTEIN_AA) -> list[str]:
    """Extract candidate protein sequences by 6-frame translation.

    Deliberately simple (no gene calling): translate all six frames, split on
    stop codons, keep ORFs >= ``min_aa``. For composition-level signal this is
    enough; a Phase-2 refinement could use a real ORF finder (e.g. prodigal-gv).
    """
    from Bio.Seq import Seq

    from features.composition import read_sequence

    nt = read_sequence(fasta_path)
    if len(nt) < min_aa * 3:
        return []
    seq = Seq(nt)
    proteins: list[str] = []
    for strand in (seq, seq.reverse_complement()):
        for frame in range(3):
            trimmed = strand[frame : frame + (len(strand) - frame) // 3 * 3]
            aa = str(trimmed.translate())
            proteins.extend(p for p in aa.split("*") if len(p) >= min_aa)
    # longest first; cap to bound embedding cost
    proteins.sort(key=len, reverse=True)
    return proteins[:MAX_PROTEINS_PER_VIRUS]


def _load_esm(model_name: str):
    try:
        import esm  # noqa: F401
        import torch
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "ESM embeddings need the optional deps. Install with:\n"
            '  uv pip install -e ".[embeddings]"'
        ) from exc
    import esm as esm_mod

    model, alphabet = getattr(esm_mod.pretrained, model_name)()
    model.eval()
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    model = model.to(device)
    return model, alphabet, device


def embed_virus(fasta_path: Path, model, alphabet, device) -> np.ndarray | None:
    """Mean-pooled ESM-2 embedding across a virus's translated proteins."""
    import torch

    proteins = translate_orfs(fasta_path)
    if not proteins:
        return None
    bc = alphabet.get_batch_converter()
    repr_layer = model.num_layers
    vecs = []
    with torch.no_grad():
        for i in range(0, len(proteins), 4):  # micro-batches
            batch = [(f"p{j}", p[:1022]) for j, p in enumerate(proteins[i : i + 4])]
            _, _, toks = bc(batch)
            toks = toks.to(device)
            out = model(toks, repr_layers=[repr_layer])["representations"][repr_layer]
            # mean over residues (excluding BOS/EOS) then collect per-protein
            for row in range(out.shape[0]):
                vecs.append(out[row, 1:-1].mean(0).cpu().numpy())
    return np.mean(vecs, axis=0) if vecs else None


def featurize_viruses(
    viruses: pd.DataFrame,
    model_name: str = DEFAULT_ESM_MODEL,
    *,
    cache_name: str | None = None,
    force: bool = False,
) -> pd.DataFrame:
    """Build an ESM-2 embedding matrix for a virus table (cached)."""
    cache = FEATURES_CACHE / (cache_name or f"esm_{model_name}.parquet")
    if cache.exists() and not force:
        log.info("embeddings cached: %s", cache)
        return pd.read_parquet(cache)

    model, alphabet, device = _load_esm(model_name)
    log.info("embedding %d viruses with %s on %s", len(viruses), model_name, device)

    rows: dict[str, np.ndarray] = {}
    for i, row in enumerate(viruses.itertuples(index=False), 1):
        gpath = genome_path(row.virus_name)
        if not gpath.exists() or gpath.stat().st_size == 0:
            continue
        vec = embed_virus(gpath, model, alphabet, device)
        if vec is not None:
            rows[row.virus_taxhash] = vec
        if i % 50 == 0:
            log.info("  embedded %d/%d", i, len(viruses))

    dim = len(next(iter(rows.values()))) if rows else 0
    feats = pd.DataFrame.from_dict(
        rows, orient="index", columns=[f"esm_{i}" for i in range(dim)]
    )
    feats.index.name = "virus_taxhash"
    FEATURES_CACHE.mkdir(parents=True, exist_ok=True)
    feats.to_parquet(cache)
    log.info("embeddings: %d viruses x %d dims", len(feats), dim)
    return feats
