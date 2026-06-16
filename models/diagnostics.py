"""Diagnostics that make the leakage legible, computed from persisted OOF preds.

  * leakage_curve     — performance vs distance-to-nearest-training-virus. The
                        clearest single demonstration that the model leans on
                        having seen close relatives.
  * hard_lineage_probe— would the model have flagged SARS-CoV-2-related / H5
                        influenza under family holdout? (the 2025 critique's test)
  * watchlist         — what the top-50 list actually contains.
  * per_family        — where the family-holdout signal comes from.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score


def _row_normalized(X: pd.DataFrame) -> np.ndarray:
    """Z-score columns (so seq_len/k-mer scales are comparable), then L2-normalize
    rows for cosine similarity."""
    mu = X.mean(0)
    sd = X.std(0).replace(0, 1.0)
    Z = ((X - mu) / sd).to_numpy()
    norms = np.linalg.norm(Z, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return Z / norms


def nearest_train_distance(dataset, scheme: str) -> pd.Series:
    """Cosine distance from each OOF test virus to its nearest *training* virus."""
    Xn = _row_normalized(dataset.X)
    idx = dataset.X.index.to_numpy()
    out: dict = {}
    for tr, te in dataset.folds(scheme):
        if len(tr) == 0 or len(te) == 0:
            continue
        sim = Xn[te] @ Xn[tr].T          # (n_test, n_train) cosine similarity
        maxsim = sim.max(axis=1)
        for j, ti in enumerate(te):
            out[idx[ti]] = 1.0 - float(maxsim[j])
    return pd.Series(out, name="dist")


def leakage_curve(dataset, preds_by_scheme: dict, n_bins: int = 6) -> dict:
    """Pool OOF preds from all schemes, bin by distance-to-nearest-train, report
    per-bin AUC + how many viruses each scheme contributes to each bin."""
    frames = []
    for scheme, preds in preds_by_scheme.items():
        if preds is None:
            continue
        d = nearest_train_distance(dataset, scheme)
        f = preds.merge(d, left_on="virus_taxhash", right_index=True)
        f["scheme"] = scheme
        frames.append(f)
    df = pd.concat(frames, ignore_index=True)
    df["bin"] = pd.qcut(df["dist"], n_bins, labels=False, duplicates="drop")
    rows = []
    for b, g in df.groupby("bin"):
        auc = roc_auc_score(g.y_true, g.y_score) if g.y_true.nunique() == 2 else None
        rows.append({
            "bin": int(b),
            "dist_lo": round(float(g.dist.min()), 3),
            "dist_hi": round(float(g.dist.max()), 3),
            "n": int(len(g)),
            "pos_rate": round(float(g.y_true.mean()), 3),
            "auc": round(float(auc), 3) if auc is not None else None,
            "frac_random": round(float((g.scheme == "random").mean()), 3),
            "frac_family": round(float((g.scheme == "tax_family").mean()), 3),
        })
    med = {s: round(float(df.loc[df.scheme == s, "dist"].median()), 3)
           for s in df.scheme.unique()}
    return {"bins": rows, "median_dist_by_scheme": med}


def hard_lineage_probe(preds: pd.DataFrame, labels: pd.DataFrame, patterns: dict) -> dict:
    """For named high-stakes lineages, report OOF score + percentile rank (under
    this scheme) + true label — i.e. would a watchlist have surfaced them?"""
    p = preds.copy()
    p["pct"] = p["y_score"].rank(pct=True)
    nm = labels.set_index("virus_taxhash")["virus_name"]
    p["name"] = p["virus_taxhash"].map(nm)
    res = {}
    for key, pat in patterns.items():
        hit = p[p["name"].astype(str).str.contains(pat, case=False, na=False, regex=True)]
        res[key] = {
            "n": int(len(hit)),
            "examples": [
                {"name": r["name"], "score": round(float(r.y_score), 3),
                 "percentile": round(float(r.pct), 3), "y": int(r.y_true)}
                for _, r in hit.sort_values("y_score", ascending=False).head(4).iterrows()
            ],
        }
    return res


def watchlist(preds: pd.DataFrame, labels: pd.DataFrame, k: int = 50, show: int = 15) -> dict:
    nm = labels.set_index("virus_taxhash")["virus_name"]
    fam = labels.set_index("virus_taxhash")["family"]
    top = preds.sort_values("y_score", ascending=False).head(k).copy()
    top["name"] = top["virus_taxhash"].map(nm)
    top["family"] = top["virus_taxhash"].map(fam)
    return {
        "k": k,
        "precision_at_k": round(float(top.y_true.mean()), 3),
        "items": [
            {"name": r["name"], "family": r["family"],
             "score": round(float(r.y_score), 3), "y": int(r.y_true)}
            for _, r in top.head(show).iterrows()
        ],
    }
