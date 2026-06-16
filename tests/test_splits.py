"""The honest-eval claim is only valid if the splits truly isolate families /
genera / time. Verify on the real splits (skip if data not built locally)."""

import pytest

from zoonotic.config import PROCESSED_DIR

pytestmark = pytest.mark.skipif(
    not (PROCESSED_DIR / "splits.parquet").exists(),
    reason="splits.parquet not built locally",
)


def _joined():
    from models.dataset import load_labels, load_splits

    splits = load_splits().set_index("virus_taxhash")
    labels = load_labels().set_index("virus_taxhash")
    return splits.join(labels[["family", "genus"]])


def test_no_family_spans_two_family_folds():
    df = _joined().dropna(subset=["tax_family_fold", "family"])
    per_family = df.groupby("family")["tax_family_fold"].nunique()
    assert (per_family <= 1).all(), "family appears in >1 fold — phylogenetic leakage"


def test_no_genus_spans_two_genus_folds():
    df = _joined().dropna(subset=["tax_genus_fold", "genus"])
    per_genus = df.groupby("genus")["tax_genus_fold"].nunique()
    assert (per_genus <= 1).all(), "genus appears in >1 fold — leakage"


def test_temporal_split_respects_cutoff():
    from models.dataset import load_splits

    s = load_splits()
    cutoff = float(s["temporal_cutoff"].iloc[0])
    train_max = s.loc[s.temporal_split == "train", "temporal_year"].max()
    test_min = s.loc[s.temporal_split == "test", "temporal_year"].min()
    assert train_max < cutoff <= test_min
