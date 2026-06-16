"""Genome-composition features — the cheap, interpretable baseline.

Reproduces the "signal is in composition" hypothesis behind zoonotic_rank: a
virus's host range leaves a fingerprint in its nucleotide composition (notably
dinucleotide biases such as CpG / UpA suppression, which track host antiviral
pressure). We compute, genome-wide:

  * mononucleotide frequencies              (4 dims)
  * dinucleotide frequencies                (16 dims)
  * dinucleotide **bias** (obs/expected)    (16 dims)  <- the key signal
  * k-mer spectra for requested k           (4**k dims each)

All features are sequence-length-normalized so a 3 kb and a 30 kb genome are
comparable. Ambiguous bases (N, etc.) are ignored.

These functions are pure and unit-testable; ``featurize_viruses`` wires them to
the on-disk genomes and caches the resulting matrix.
"""

from __future__ import annotations

import logging
from collections import Counter
from itertools import product
from pathlib import Path

import pandas as pd

from zoonotic.config import FEATURES_CACHE
from zoonotic.ncbi import genome_path

log = logging.getLogger("zoonotic.features.composition")

BASES = ("A", "C", "G", "T")
_TRANS = str.maketrans("U", "T")  # RNA -> DNA alphabet


def read_sequence(fasta_path: Path) -> str:
    """Concatenate all records in a (multi-)FASTA into one uppercase ACGT string.

    Multi-segment genomes are concatenated; this is fine for composition, which
    is position-independent. Non-ACGT characters are dropped.
    """
    seq_chars: list[str] = []
    with open(fasta_path) as fh:
        for line in fh:
            if line.startswith(">"):
                continue
            seq_chars.append(line.strip().upper())
    seq = "".join(seq_chars).translate(_TRANS)
    return "".join(c for c in seq if c in BASES)


def _kmers(k: int) -> list[str]:
    return ["".join(p) for p in product(BASES, repeat=k)]


def kmer_frequencies(seq: str, k: int) -> dict[str, float]:
    """Length-normalized k-mer frequencies (sums to 1 over observed k-mers)."""
    counts = Counter(seq[i : i + k] for i in range(len(seq) - k + 1))
    total = sum(counts[kmer] for kmer in _kmers(k)) or 1
    return {f"k{k}_{kmer}": counts.get(kmer, 0) / total for kmer in _kmers(k)}


def dinucleotide_bias(seq: str) -> dict[str, float]:
    """Dinucleotide odds ratio: observed / (freq(x)*freq(y)). 1.0 == no bias.

    This is the classic genome-composition signal (e.g. CpG suppression).
    """
    mono = kmer_frequencies(seq, 1)
    di = kmer_frequencies(seq, 2)
    out = {}
    for x, y in product(BASES, repeat=2):
        expected = mono[f"k1_{x}"] * mono[f"k1_{y}"]
        obs = di[f"k2_{x}{y}"]
        out[f"bias_{x}{y}"] = obs / expected if expected > 0 else 0.0
    return out


def composition_features(fasta_path: Path, ks: tuple[int, ...] = (1, 2, 3)) -> dict[str, float]:
    """Full composition feature dict for one genome FASTA."""
    seq = read_sequence(fasta_path)
    feats: dict[str, float] = {"seq_len": float(len(seq))}
    if len(seq) < max(ks) + 1:
        # too short to featurize meaningfully; return zeros (caller can drop)
        return feats
    for k in ks:
        feats.update(kmer_frequencies(seq, k))
    feats.update(dinucleotide_bias(seq))
    return feats


def featurize_viruses(
    viruses: pd.DataFrame,
    ks: tuple[int, ...] = (1, 2, 3),
    *,
    cache_name: str = "composition.parquet",
    force: bool = False,
) -> pd.DataFrame:
    """Build a composition feature matrix for a virus table.

    ``viruses`` must have ``virus_taxhash`` and ``virus_name`` (to locate the
    cached genome). Returns a DataFrame indexed by ``virus_taxhash``; viruses
    without a downloaded genome are skipped (and reported).
    """
    cache = FEATURES_CACHE / cache_name
    if cache.exists() and not force:
        log.info("composition features cached: %s", cache)
        return pd.read_parquet(cache)

    rows: dict[str, dict[str, float]] = {}
    n_missing = 0
    for row in viruses.itertuples(index=False):
        if not isinstance(row.virus_name, str):  # NaN name -> no genome
            n_missing += 1
            continue
        gpath = genome_path(row.virus_name)
        if not gpath.exists() or gpath.stat().st_size == 0:
            n_missing += 1
            continue
        rows[row.virus_taxhash] = composition_features(gpath, ks)

    feats = pd.DataFrame.from_dict(rows, orient="index")
    feats.index.name = "virus_taxhash"
    feats = feats.fillna(0.0)
    FEATURES_CACHE.mkdir(parents=True, exist_ok=True)
    feats.to_parquet(cache)
    log.info("composition features: %d viruses x %d dims (%d genomes missing)",
             len(feats), feats.shape[1], n_missing)
    return feats


if __name__ == "__main__":
    # Smoke test against whatever genomes are already on disk.
    import logging as _l

    _l.basicConfig(level=_l.INFO)
    from zoonotic.config import GENOME_DIR

    for fa in sorted(GENOME_DIR.glob("*.fasta"))[:3]:
        feats = composition_features(fa)
        print(f"{fa.name}: {len(feats)} features, seq_len={feats.get('seq_len')}, "
              f"bias_CG={feats.get('bias_CG'):.3f}")
