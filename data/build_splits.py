#!/usr/bin/env python
"""Build evaluation splits — the heart of honest evaluation.

We emit four split schemes over **one shared cohort** so the headline comparison
(random vs taxonomic-holdout) is not confounded by different sample sets:

  1. ``random``          — stratified 5-fold. The optimistic, leaky number.
  2. ``tax_family``      — stratified *group* 5-fold holding out whole FAMILIES.
                           Test viruses share no family with training viruses.
                           This is the honest test of generalization.
  3. ``tax_genus``       — same, holding out whole GENERA (stricter, smaller
                           sub-cohort since genus is ~58% resolved).
  4. ``temporal``        — train on viruses whose earliest genome release < T,
                           test on >= T. Simulates prospective use.

CAVEAT (documented in FINDINGS.md): the temporal "year" is the earliest GenBank
*sequence release* year, which reflects deposition, not virus discovery. It is a
proxy, not a true characterization date.

Output: ``data/processed/splits.parquet`` keyed by ``virus_taxhash``.
"""

from __future__ import annotations

import json
import logging

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold

from zoonotic.config import PROCESSED_DIR, RANDOM_SEED, RESULTS_DIR, ensure_dirs
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.build_splits")

N_FOLDS = 5
TEMPORAL_CUTOFF = 2020  # train < cutoff, test >= cutoff (configurable)


def define_cohort(labels: pd.DataFrame) -> pd.DataFrame:
    """The shared modelable cohort: family + year known, and a fetchable genome.

    Every split scheme is computed on exactly this set so cross-split numbers are
    comparable. (``tax_genus`` additionally requires a resolved genus.)
    """
    genome_fetchable = labels["ncbi_taxid"].notna() | labels["n_accessions"].gt(0)
    cohort = labels[
        labels["family"].notna()
        & labels["first_year"].notna()
        & genome_fetchable
    ].copy()
    return cohort


def _stratified_folds(y: pd.Series) -> pd.Series:
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    folds = pd.Series(-1, index=y.index, dtype=int)
    for k, (_, test_idx) in enumerate(skf.split(y, y)):
        folds.iloc[test_idx] = k
    return folds


def _stratified_group_folds(y: pd.Series, groups: pd.Series) -> pd.Series:
    sgkf = StratifiedGroupKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    folds = pd.Series(-1, index=y.index, dtype=int)
    for k, (_, test_idx) in enumerate(sgkf.split(y, y, groups=groups)):
        folds.iloc[test_idx] = k
    return folds


def build(labels: pd.DataFrame) -> pd.DataFrame:
    cohort = define_cohort(labels)
    log.info("cohort: %d viruses, %d positive (%.2f%%)",
             len(cohort), int(cohort.label.sum()), 100 * cohort.label.mean())

    splits = pd.DataFrame(index=cohort.index)
    splits["virus_taxhash"] = cohort["virus_taxhash"]

    # 1. random stratified
    splits["random_fold"] = _stratified_folds(cohort["label"])

    # 2. taxonomic family holdout
    splits["tax_family_fold"] = _stratified_group_folds(cohort["label"], cohort["family"])

    # 3. taxonomic genus holdout (sub-cohort with genus resolved)
    splits["tax_genus_fold"] = pd.Series(pd.NA, index=cohort.index, dtype="Int64")
    gsub = cohort[cohort["genus"].notna()]
    gfolds = _stratified_group_folds(gsub["label"], gsub["genus"])
    splits.loc[gsub.index, "tax_genus_fold"] = gfolds.astype("Int64")

    # 4. temporal holdout
    yr = cohort["first_year"].astype(int)
    splits["temporal_year"] = yr
    splits["temporal_split"] = pd.Series(
        ["test" if v >= TEMPORAL_CUTOFF else "train" for v in yr], index=cohort.index
    )
    splits["temporal_cutoff"] = TEMPORAL_CUTOFF

    return splits.reset_index(drop=True)


def _leakage_check(splits: pd.DataFrame, labels: pd.DataFrame) -> dict:
    """Sanity: no family appears in two different tax_family folds."""
    m = splits.merge(labels[["virus_taxhash", "family", "genus"]], on="virus_taxhash")
    fam_fold_counts = m.groupby("family")["tax_family_fold"].nunique()
    genus_fold_counts = m.dropna(subset=["tax_genus_fold"]).groupby("genus")["tax_genus_fold"].nunique()
    return {
        "families_split_across_folds": int((fam_fold_counts > 1).sum()),
        "genera_split_across_folds": int((genus_fold_counts > 1).sum()),
    }


def summarize(splits: pd.DataFrame, labels: pd.DataFrame) -> dict:
    m = splits.merge(labels[["virus_taxhash", "label"]], on="virus_taxhash")
    out = {
        "cohort_size": int(len(m)),
        "cohort_positives": int(m.label.sum()),
        "n_folds": N_FOLDS,
        "temporal_cutoff": TEMPORAL_CUTOFF,
        "temporal_train_n": int((splits.temporal_split == "train").sum()),
        "temporal_test_n": int((splits.temporal_split == "test").sum()),
        "temporal_test_positives": int(
            m.loc[splits.temporal_split == "test", "label"].sum()
        ),
        "genus_subcohort_n": int(splits["tax_genus_fold"].notna().sum()),
        "positives_per_random_fold": m.groupby(splits.random_fold)["label"].sum().to_dict(),
        "positives_per_family_fold": m.groupby(splits.tax_family_fold)["label"].sum().to_dict(),
    }
    out.update(_leakage_check(splits, labels))
    return out


def main() -> None:
    setup_logging()
    ensure_dirs()
    labels = pd.read_parquet(PROCESSED_DIR / "labels.parquet")
    splits = build(labels)
    summary = summarize(splits, labels)

    out = PROCESSED_DIR / "splits.parquet"
    splits.to_parquet(out, index=False)
    (RESULTS_DIR / "splits_summary.json").write_text(json.dumps(summary, indent=2, default=str))

    log.info("wrote %s", out)
    for k, v in summary.items():
        log.info("  %-30s %s", k, v)
    # the leakage check must pass: whole families/genera stay within one fold
    assert summary["families_split_across_folds"] == 0, "FAMILY LEAKAGE across folds!"
    assert summary["genera_split_across_folds"] == 0, "GENUS LEAKAGE across folds!"
    log.info("leakage check passed: families/genera are not split across folds")


if __name__ == "__main__":
    main()
