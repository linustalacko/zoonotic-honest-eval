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

DEFAULT_ESM_MODEL = "esm2_t30_150M_UR50D"  # 150M first (fast); 650M is the upgrade
MIN_PROTEIN_AA = 30
MAX_PROTEINS_PER_VIRUS = 30  # cap pooling cost for large/segmented genomes


def translate_orfs(fasta_path: Path, min_aa: int = MIN_PROTEIN_AA,
                   max_proteins: int = MAX_PROTEINS_PER_VIRUS) -> list[str]:
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
    return proteins[:max_proteins]


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
    # CUDA first (Modal GPU), then Apple MPS (local), else CPU. The earlier run
    # silently fell to CPU on a GPU box because this only checked MPS — ~450
    # viruses/hour instead of minutes.
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    model = model.to(device)
    if device == "cuda":
        model = model.half()  # fp16 — halves memory (15B fits on A100-80GB) and faster
    return model, alphabet, device


def embed_virus(fasta_path: Path, model, alphabet, device,
                max_proteins: int = MAX_PROTEINS_PER_VIRUS) -> np.ndarray | None:
    """Mean+max-pooled ESM-2 embedding across a virus's translated proteins."""
    import torch

    proteins = translate_orfs(fasta_path, max_proteins=max_proteins)
    if not proteins:
        return None
    bc = alphabet.get_batch_converter()
    repr_layer = model.num_layers
    vecs = []
    with torch.no_grad():
        for i in range(0, len(proteins), 16):  # micro-batches (bigger = better GPU use)
            chunk = [p[:1022] for p in proteins[i : i + 16]]
            _, _, toks = bc([(f"p{j}", p) for j, p in enumerate(chunk)])
            toks = toks.to(device)
            out = model(toks, repr_layers=[repr_layer])["representations"][repr_layer]
            # mean over each protein's TRUE residues only (1..L), excluding the
            # BOS token and any right-padding from shorter proteins in the batch.
            for row, prot in enumerate(chunk):
                length = len(prot)
                vecs.append(out[row, 1 : 1 + length].mean(0).float().cpu().numpy())
    if not vecs:
        return None
    # mean + max pooling across proteins — max captures the most-discriminative
    # protein (the MIL intuition) without a trainable attention. Doubles the dim.
    v = np.stack(vecs)
    return np.concatenate([v.mean(axis=0), v.max(axis=0)])


def _rows_to_df(rows: dict[str, np.ndarray]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    dim = len(next(iter(rows.values())))
    df = pd.DataFrame.from_dict(rows, orient="index", columns=[f"esm_{i}" for i in range(dim)])
    df.index.name = "virus_taxhash"
    return df


def featurize_viruses(
    viruses: pd.DataFrame,
    model_name: str = DEFAULT_ESM_MODEL,
    *,
    cache_name: str | None = None,
    force: bool = False,
    commit_every: int = 0,
    commit_cb=None,
    max_proteins: int = MAX_PROTEINS_PER_VIRUS,
) -> pd.DataFrame:
    """Build an ESM-2 embedding matrix for a virus table.

    **Resumable**: writes a ``.partial`` checkpoint every ``commit_every`` viruses
    (and calls ``commit_cb``, e.g. to commit a Modal Volume), so a preempted GPU
    container resumes instead of re-embedding from scratch. Embedding 9k viruses
    exceeds one A10 container's stable lifetime, so this is load-bearing.
    """
    cache = FEATURES_CACHE / (cache_name or f"esm_{model_name}.parquet")
    if cache.exists() and not force:
        log.info("embeddings cached: %s", cache)
        return pd.read_parquet(cache)

    partial = cache.with_suffix(".partial.parquet")
    rows: dict[str, np.ndarray] = {}
    if partial.exists() and not force:
        ex = pd.read_parquet(partial)
        rows = {idx: ex.loc[idx].to_numpy() for idx in ex.index}
        log.info("resuming ESM embedding from %d checkpointed viruses", len(rows))

    model, alphabet, device = _load_esm(model_name)
    log.info("embedding %d viruses with %s on %s (%d already done)",
             len(viruses), model_name, device, len(rows))

    FEATURES_CACHE.mkdir(parents=True, exist_ok=True)
    for i, row in enumerate(viruses.itertuples(index=False), 1):
        if row.virus_taxhash in rows:  # resume: skip done
            continue
        if not isinstance(row.virus_name, str):
            continue
        gpath = genome_path(row.virus_name)
        if not gpath.exists() or gpath.stat().st_size == 0:
            continue
        vec = embed_virus(gpath, model, alphabet, device, max_proteins=max_proteins)
        if vec is not None:
            rows[row.virus_taxhash] = vec
        if i % 50 == 0:
            log.info("  embedded %d/%d (%d vecs)", i, len(viruses), len(rows))
        if commit_every and i % commit_every == 0:
            _rows_to_df(rows).to_parquet(partial)
            if commit_cb:
                commit_cb()

    feats = _rows_to_df(rows)
    feats.to_parquet(cache)
    partial.unlink(missing_ok=True)
    if commit_cb:
        commit_cb()
    log.info("embeddings: %d viruses x %d dims", len(feats), feats.shape[1])
    return feats
