"""Extra genome features for the hill-climb — beyond the base composition set.

All read the on-disk genomes and cache an indexed matrix, exactly like
``features.composition``. These are the levers the loop searches over once model
choice is exhausted:

  * kmer4      — 256-dim tetranucleotide spectrum (finer composition)
  * aa         — 20-dim amino-acid composition of translated ORFs (protein-level)
  * dipeptide  — 400-dim amino-acid dipeptide frequencies (local protein motifs)
  * codonpos   — 12-dim nucleotide frequencies by codon position (codon bias /
                 host-adaptation signal, the influenza-style feature)
  * scalar     — GC, length, skews, ORF density (coarse genome descriptors)
"""

from __future__ import annotations

import logging
from collections import Counter
from itertools import product
from pathlib import Path

import pandas as pd

from features.composition import BASES, kmer_frequencies, read_sequence
from zoonotic.config import FEATURES_CACHE
from zoonotic.ncbi import genome_path

log = logging.getLogger("zoonotic.features.extra")

AA = "ACDEFGHIKLMNPQRSTVWY"


def _proteins(fasta_path: Path) -> list[str]:
    from features.embeddings import translate_orfs

    return translate_orfs(fasta_path, min_aa=20)


def kmer4(fasta_path: Path) -> dict:
    return kmer_frequencies(read_sequence(fasta_path), 4)


def codonpos(fasta_path: Path) -> dict:
    """Nucleotide frequency at each of the 3 codon positions (frame 0)."""
    seq = read_sequence(fasta_path)
    out = {}
    for pos in range(3):
        sub = seq[pos::3]
        n = len(sub) or 1
        c = Counter(sub)
        for b in BASES:
            out[f"cp{pos}_{b}"] = c.get(b, 0) / n
    return out


def aa_comp(fasta_path: Path) -> dict:
    prots = _proteins(fasta_path)
    joined = "".join(prots)
    n = len(joined) or 1
    c = Counter(joined)
    return {f"aa_{a}": c.get(a, 0) / n for a in AA}


def dipeptide(fasta_path: Path) -> dict:
    prots = _proteins(fasta_path)
    c: Counter = Counter()
    total = 0
    for p in prots:
        for i in range(len(p) - 1):
            c[p[i : i + 2]] += 1
            total += 1
    total = total or 1
    return {f"dp_{a}{b}": c.get(a + b, 0) / total for a in AA for b in AA}


def scalar(fasta_path: Path) -> dict:
    import math

    seq = read_sequence(fasta_path)
    n = len(seq) or 1
    c = Counter(seq)
    g, cc, a, t = c.get("G", 0), c.get("C", 0), c.get("A", 0), c.get("T", 0)
    gc = (g + cc) / n
    prots = _proteins(fasta_path)
    return {
        "gc": gc,
        "log_len": math.log1p(n),
        "at_skew": (a - t) / (a + t) if (a + t) else 0.0,
        "gc_skew": (g - cc) / (g + cc) if (g + cc) else 0.0,
        "orf_density": len(prots) / n * 1000,
        "mean_orf_len": (sum(len(p) for p in prots) / len(prots)) if prots else 0.0,
        "n_orfs": float(len(prots)),
    }


_GENERATORS = {
    "kmer4": (kmer4, "kmer4.parquet"),
    "codonpos": (codonpos, "codonpos.parquet"),
    "aa": (aa_comp, "aa.parquet"),
    "dipeptide": (dipeptide, "dipeptide.parquet"),
    "scalar": (scalar, "scalar.parquet"),
}


def featurize(name: str, viruses: pd.DataFrame, *, force: bool = False) -> pd.DataFrame:
    """Build (and cache) one extra feature matrix indexed by virus_taxhash."""
    fn, cache_name = _GENERATORS[name]
    cache = FEATURES_CACHE / cache_name
    if cache.exists() and not force:
        return pd.read_parquet(cache)

    rows: dict[str, dict] = {}
    n_missing = 0
    for row in viruses.itertuples(index=False):
        if not isinstance(row.virus_name, str):
            n_missing += 1
            continue
        gpath = genome_path(row.virus_name)
        if not gpath.exists() or gpath.stat().st_size == 0:
            n_missing += 1
            continue
        rows[row.virus_taxhash] = fn(gpath)

    feats = pd.DataFrame.from_dict(rows, orient="index").fillna(0.0)
    feats.index.name = "virus_taxhash"
    FEATURES_CACHE.mkdir(parents=True, exist_ok=True)
    feats.to_parquet(cache)
    log.info("extra[%s]: %d viruses x %d dims (%d missing)", name, len(feats), feats.shape[1], n_missing)
    return feats


# k-mer columns helper (for product completeness if needed)
def _kmer_cols(k: int) -> list[str]:
    return [f"k{k}_" + "".join(p) for p in product(BASES, repeat=k)]
