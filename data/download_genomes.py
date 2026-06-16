#!/usr/bin/env python
"""Download representative genomes for the modelable cohort (resumable, shardable).

For each virus we prefer a RefSeq reference genome (by NCBI taxid), falling back
to VIRION's own accessions. Every result is cached so the job is fully resumable.

The core ``run()`` supports sharding (``shard_index``/``num_shards``) so Modal can
fan the work across many containers, and a ``commit_cb`` so each container can
checkpoint its writes to the Volume periodically.

  python data/download_genomes.py            # cohort only (default)
  python data/download_genomes.py --all      # every labeled virus
  python data/download_genomes.py --limit 50 # smoke test
  python data/download_genomes.py --shard-index 0 --num-shards 8
"""

from __future__ import annotations

import argparse
import json
import logging
import time
from collections.abc import Callable

import numpy as np
import pandas as pd

from zoonotic.config import GENOME_DIR, PROCESSED_DIR, RESULTS_DIR, ensure_dirs
from zoonotic.logging_utils import setup_logging
from zoonotic.ncbi import configure_entrez, fetch_genome_for_virus, genome_path

log = logging.getLogger("zoonotic.download.genomes")


def _target_viruses(use_all: bool) -> pd.DataFrame:
    labels = pd.read_parquet(PROCESSED_DIR / "labels.parquet")
    if use_all:
        return labels
    splits = pd.read_parquet(PROCESSED_DIR / "splits.parquet")
    return labels[labels["virus_taxhash"].isin(splits["virus_taxhash"])].copy()


def run(
    *,
    use_all: bool = False,
    limit: int | None = None,
    shard_index: int = 0,
    num_shards: int = 1,
    commit_every: int = 0,
    commit_cb: Callable[[], None] | None = None,
) -> dict:
    """Fetch genomes for (a shard of) the target viruses. Returns a summary dict."""
    ensure_dirs()
    configure_entrez()

    targets = _target_viruses(use_all)
    if num_shards > 1:
        targets = targets.iloc[shard_index::num_shards]  # strided shard
    if limit:
        targets = targets.head(limit)
    log.info("genome targets: %d viruses (shard %d/%d, scope=%s)",
             len(targets), shard_index, num_shards, "all" if use_all else "cohort")

    found = missing = errored = 0
    t0 = time.monotonic()
    for i, row in enumerate(targets.itertuples(index=False), 1):
        # Per-virus resilience: a single virus that persistently fails Entrez (or
        # has a malformed accessions value) must NOT crash the whole batch — log
        # it, negative-cache it so resume skips it, and move on.
        acc_val = row.accessions
        accs = list(acc_val) if isinstance(acc_val, (list, tuple, np.ndarray)) else []
        taxid = int(row.ncbi_taxid) if pd.notna(row.ncbi_taxid) else None
        try:
            path = fetch_genome_for_virus(row.virus_name, taxid=taxid, fallback_accessions=accs)
        except Exception as exc:  # noqa: BLE001 — one bad virus shouldn't end the run
            log.warning("virus %r failed, skipping: %s", row.virus_name, exc)
            genome_path(row.virus_name).with_suffix(".empty").write_text("")
            path, errored = None, errored + 1
        found += bool(path)
        missing += not path
        if i % 100 == 0:
            rate = i / (time.monotonic() - t0)
            eta = (len(targets) - i) / rate / 60
            log.info("  %d/%d found=%d missing=%d (%.1f/s, ETA %.0f min)",
                     i, len(targets), found, missing, rate, eta)
        if commit_every and commit_cb and i % commit_every == 0:
            commit_cb()
    if commit_cb:
        commit_cb()

    summary = {
        "targets": int(len(targets)),
        "found": found,
        "missing": missing,
        "errored": errored,
        "shard": f"{shard_index}/{num_shards}",
        "scope": "all" if use_all else "cohort",
    }
    suffix = f"_shard{shard_index}" if num_shards > 1 else ""
    (RESULTS_DIR / f"genomes_summary{suffix}.json").write_text(json.dumps(summary, indent=2))
    log.info("genome download done: %s", summary)
    return summary


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="fetch every labeled virus, not just the cohort")
    ap.add_argument("--limit", type=int, default=None, help="cap number of viruses (smoke test)")
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--num-shards", type=int, default=1)
    args = ap.parse_args()

    setup_logging()
    run(use_all=args.all, limit=args.limit,
        shard_index=args.shard_index, num_shards=args.num_shards)
    n_fasta = len(list(GENOME_DIR.glob("*.fasta")))
    log.info("fasta files on disk: %d", n_fasta)


if __name__ == "__main__":
    main()
