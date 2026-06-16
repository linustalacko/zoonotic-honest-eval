"""The metrics and the bootstrap CI back every claim in FINDINGS — pin them."""

import numpy as np
import pandas as pd

from models.evaluate import (
    _family_clustered_bootstrap,
    _metric_arr,
    precision_recall_at_k,
    score_predictions,
)


def test_precision_recall_at_k():
    y = np.array([1, 0, 1, 0, 0])
    s = np.array([0.9, 0.8, 0.7, 0.2, 0.1])  # top-2 = ranks of 0.9,0.8 -> 1,0
    p, r = precision_recall_at_k(y, s, 2)
    assert p == 0.5          # 1 of top-2 is positive
    assert r == 0.5          # caught 1 of 2 positives


def test_score_predictions_lift_and_base_rate():
    y = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])  # base rate 0.2
    s = np.where(y == 1, 0.9, 0.1)                  # separable probabilities in [0,1]
    m = score_predictions(y, s)
    assert m["base_rate"] == 0.2
    assert m["roc_auc"] == 1.0
    assert m["lift@10"] >= 1.0


def test_metric_arr_single_class_is_nan():
    y = np.zeros(10, dtype=int)
    assert np.isnan(_metric_arr(y, np.random.default_rng(0).random(10), "roc_auc"))


def _synth(better: bool, seed: int = 0):
    """6 families x 12 viruses; `better` controls how informative the scores are."""
    rng = np.random.default_rng(seed)
    rows = []
    for fam in range(6):
        for _ in range(12):
            y = int(rng.random() < 0.3)
            score = (y + rng.normal(0, 0.3)) if better else rng.random()
            rows.append({"virus_taxhash": f"v{len(rows)}", "y_true": y,
                         "y_score": score, "family": f"fam{fam}"})
    return pd.DataFrame(rows)


def test_bootstrap_no_difference_brackets_zero():
    a = _synth(better=True, seed=1)
    b = a.copy()  # identical predictions
    out = _family_clustered_bootstrap(a, b, "roc_auc", n=300)
    assert abs(out["point"]) < 1e-9
    assert out["ci_lo"] <= 0 <= out["ci_hi"]


def test_bootstrap_detects_real_difference():
    a = _synth(better=True, seed=2)            # informative
    b = a.copy()
    b["y_score"] = _synth(better=False, seed=3)["y_score"].to_numpy()  # noise
    out = _family_clustered_bootstrap(a, b, "roc_auc", n=400)
    assert out["point"] > 0           # informative beats noise
    assert out["p_diff_le_0"] < 0.2   # and it's reasonably significant
