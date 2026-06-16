"""Assemble (features, labels, splits) into train/test folds for evaluation.

A ``Dataset`` aligns a feature matrix to the labeled cohort and exposes a uniform
``folds(scheme)`` iterator over every split scheme. Models and the eval harness
never touch the raw tables directly — they go through here, so the *exact same*
cohort/labels back every split (the comparability invariant from build_splits).
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

import numpy as np
import pandas as pd

from zoonotic.config import PROCESSED_DIR

FOLD_SCHEMES = ("random", "tax_family", "tax_genus")
ALL_SCHEMES = (*FOLD_SCHEMES, "temporal")


def load_labels() -> pd.DataFrame:
    return pd.read_parquet(PROCESSED_DIR / "labels.parquet")


def load_splits() -> pd.DataFrame:
    return pd.read_parquet(PROCESSED_DIR / "splits.parquet")


@dataclass
class Dataset:
    """Feature matrix + labels + split assignments, all aligned by virus_taxhash."""

    X: pd.DataFrame  # index = virus_taxhash, columns = features
    y: pd.Series  # index = virus_taxhash, values 0/1
    meta: pd.DataFrame  # index = virus_taxhash; family/genus/year/split columns

    @property
    def n(self) -> int:
        return len(self.y)

    @property
    def base_rate(self) -> float:
        return float(self.y.mean())

    def folds(self, scheme: str) -> Iterator[tuple[np.ndarray, np.ndarray]]:
        """Yield (train_idx, test_idx) positional arrays for the given scheme.

        For k-fold schemes, yields K folds. For 'temporal', yields one split.
        """
        if scheme in FOLD_SCHEMES:
            col = {"random": "random_fold", "tax_family": "tax_family_fold",
                   "tax_genus": "tax_genus_fold"}[scheme]
            folds = self.meta[col]
            valid = folds.notna().to_numpy()
            # NA-safe: tax_genus_fold is null for viruses outside the genus
            # subcohort, so comparisons must coerce NA -> False, not pd.NA.
            for k in sorted(folds.dropna().unique()):
                test_mask = folds.eq(k).fillna(False).to_numpy(dtype=bool)
                train_mask = valid & ~test_mask
                yield np.where(train_mask)[0], np.where(test_mask)[0]
        elif scheme == "temporal":
            split = self.meta["temporal_split"]
            train = np.where((split == "train").to_numpy())[0]
            test = np.where((split == "test").to_numpy())[0]
            yield train, test
        else:
            raise ValueError(f"unknown split scheme: {scheme}")


def build_dataset(features: pd.DataFrame) -> Dataset:
    """Join a feature matrix (indexed by virus_taxhash) to labels + splits.

    Keeps only viruses present in *all three* (cohort ∩ has-features), so models
    are trained and scored on a consistent set.
    """
    labels = load_labels().set_index("virus_taxhash")
    splits = load_splits().set_index("virus_taxhash")

    idx = features.index.intersection(splits.index)
    X = features.loc[idx].copy()
    y = labels.loc[idx, "label"].astype(int)
    meta = splits.loc[idx].join(
        labels.loc[idx, ["virus_name", "family", "genus", "order", "class", "first_year"]]
    )
    return Dataset(X=X, y=y, meta=meta)
