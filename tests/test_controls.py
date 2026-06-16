"""The control rungs are the whole point. Two invariants must hold:
  * effort_only must never see the label (no human-derived or label-implied cols);
  * family_prior must collapse to the global rate on unseen families (the leakage
    demonstration that makes the family-holdout column meaningful)."""

import numpy as np
import pandas as pd

from features.metadata import effort_features
from models.baselines import GroupRateClassifier


def _labels():
    return pd.DataFrame({
        "virus_taxhash": ["a", "b", "c"],
        "n_assoc": [100, 10, 2],
        "n_human_assoc": [90, 0, 1],          # label source — must NOT leak
        "n_host_species": [5, 3, 1],
        "n_host_classes": [2, 1, 1],
        "has_mammal_host": [True, True, True],   # implied by label — must NOT leak
        "has_vertebrate_host": [True, True, True],
    })


def test_effort_features_are_label_independent_generalism():
    feats = effort_features(_labels())
    cols = set(feats.columns)
    # must use ONLY host-breadth; no count that entangles the label, and no
    # label-subtracted feature (those leaked — see docs/raising_the_ceiling.md).
    for banned in ("n_human_assoc", "n_assoc", "log_assoc", "log_nonhuman_assoc",
                   "log_nonhuman_hosts", "has_mammal_host", "has_vertebrate_host",
                   "label", "n_accessions", "clover_human"):
        assert banned not in cols
    assert cols == {"log_host_species", "n_host_classes"}


def test_effort_uses_host_breadth_values():
    feats = effort_features(_labels())
    # virus a: 5 host species, 2 host classes — no label subtraction
    assert np.isclose(feats.loc["a", "log_host_species"], np.log1p(5))
    assert np.isclose(feats.loc["a", "n_host_classes"], 2.0)


def test_group_rate_predicts_training_group_rate():
    X = np.array([["fam1"], ["fam1"], ["fam2"], ["fam2"]], dtype=object)
    y = np.array([1, 0, 1, 1])
    clf = GroupRateClassifier(smoothing=0.0).fit(X, y)
    p = clf.predict_proba(X)[:, 1]
    assert np.isclose(p[0], 0.5)   # fam1 = 1/2
    assert np.isclose(p[2], 1.0)   # fam2 = 2/2


def test_group_rate_collapses_to_global_on_unseen_family():
    """Under family holdout every test family is unseen -> global rate -> = prior."""
    X = np.array([["fam1"], ["fam1"], ["fam2"], ["fam2"]], dtype=object)
    y = np.array([1, 0, 1, 1])  # global rate 3/4
    clf = GroupRateClassifier(smoothing=0.0).fit(X, y)
    unseen = clf.predict_proba(np.array([["NEW"]], dtype=object))[0, 1]
    assert np.isclose(unseen, 0.75)
