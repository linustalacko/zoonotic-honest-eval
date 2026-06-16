"""The honest-evaluation harness — base-rate-aware, leakage-controlled.

Spillover is rare, so ROC-AUC flatters. We report precision/recall, PR-AUC,
precision@k (top-N watchlist precision) and *lift* over the base rate, for every
split scheme side by side. The headline of the whole project is one number: how
much the metrics drop from ``random`` to ``tax_family`` (taxonomic holdout).

Usage (after features exist):

    from features.composition import featurize_viruses
    from models.dataset import build_dataset, load_labels
    from models.evaluate import run_matrix
    from models.train import make_model

    feats = featurize_viruses(load_labels())
    ds = build_dataset(feats)
    table = run_matrix(ds, lambda: make_model("xgboost"), tag="composition+xgb")
    print(table)
"""

from __future__ import annotations

import logging
import uuid

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score

from models.dataset import ALL_SCHEMES, Dataset
from zoonotic.config import RANDOM_SEED, RESULTS_DIR
from zoonotic.experiment import log_run

log = logging.getLogger("zoonotic.evaluate")

WATCHLIST_KS = (10, 50, 100)


def precision_recall_at_k(y_true: np.ndarray, y_score: np.ndarray, k: int) -> tuple[float, float]:
    """Precision and recall within the top-k highest-scored items."""
    k = min(k, len(y_score))
    if k == 0:
        return float("nan"), float("nan")
    order = np.argsort(y_score)[::-1][:k]
    top = y_true[order]
    n_pos = int(y_true.sum())
    precision = float(top.mean())
    recall = float(top.sum() / n_pos) if n_pos else float("nan")
    return precision, recall


def score_predictions(y_true: np.ndarray, y_score: np.ndarray) -> dict[str, float]:
    """All metrics for one set of (held-out) predictions."""
    y_true = np.asarray(y_true).astype(int)
    y_score = np.asarray(y_score, dtype=float)
    n_pos = int(y_true.sum())
    base = float(y_true.mean()) if len(y_true) else float("nan")

    single_class = n_pos == 0 or n_pos == len(y_true)
    metrics: dict[str, float] = {
        "n": int(len(y_true)),
        "n_pos": n_pos,
        "base_rate": round(base, 4),
        "roc_auc": float("nan") if single_class else round(roc_auc_score(y_true, y_score), 4),
        "pr_auc": float("nan") if single_class else round(average_precision_score(y_true, y_score), 4),
        "brier": round(brier_score_loss(y_true, y_score), 4) if not single_class else float("nan"),
    }
    for k in WATCHLIST_KS:
        p, r = precision_recall_at_k(y_true, y_score, k)
        metrics[f"p@{k}"] = round(p, 4)
        metrics[f"r@{k}"] = round(r, 4)
        # lift = how many times better than picking at random
        metrics[f"lift@{k}"] = round(p / base, 2) if base and not np.isnan(p) else float("nan")
    return metrics


def evaluate_scheme(dataset: Dataset, model_factory, scheme: str) -> tuple[dict, pd.DataFrame | None]:
    """Fit/predict across a scheme's folds; return (metrics, out-of-fold preds).

    Pooling out-of-fold predictions gives one honest metric set per scheme. The
    returned OOF frame (virus_taxhash, y_true, y_score, fold, family) is what every
    downstream rigor step — confidence intervals, calibration, leakage curve,
    per-family breakdown — is computed from, with no retraining.
    """
    X = dataset.X.to_numpy()
    y = dataset.y.to_numpy()
    fams = dataset.meta["family"].to_numpy()

    oof_idx: list[int] = []
    oof_score: list[float] = []
    oof_fold: list[int] = []
    fold_aucs: list[float] = []

    for fold_i, (train_idx, test_idx) in enumerate(dataset.folds(scheme)):
        if len(test_idx) == 0 or len(train_idx) == 0:
            continue
        model = model_factory()
        model.fit(X[train_idx], y[train_idx])
        score = model.predict_proba(X[test_idx])[:, 1]
        oof_idx.extend(test_idx.tolist())
        oof_score.extend(score.tolist())
        oof_fold.extend([fold_i] * len(test_idx))
        if len(np.unique(y[test_idx])) == 2:
            fold_aucs.append(roc_auc_score(y[test_idx], score))

    if not oof_idx:
        return {"scheme": scheme, "error": "no evaluable folds"}, None

    pos = np.array(oof_idx)
    oof = pd.DataFrame({
        "virus_taxhash": dataset.X.index.to_numpy()[pos],
        "y_true": y[pos].astype(int),
        "y_score": np.asarray(oof_score, dtype=float),
        "fold": oof_fold,
        "family": fams[pos],
    })
    metrics = score_predictions(oof["y_true"].to_numpy(), oof["y_score"].to_numpy())
    metrics["scheme"] = scheme
    metrics["roc_auc_fold_mean"] = round(float(np.mean(fold_aucs)), 4) if fold_aucs else float("nan")
    metrics["roc_auc_fold_std"] = round(float(np.std(fold_aucs)), 4) if fold_aucs else float("nan")
    return metrics, oof


def run_matrix(
    dataset: Dataset,
    model_factory,
    *,
    tag: str,
    features: str = "composition",
    model: str = "unspecified",
    seed: int = 0,
    schemes: tuple[str, ...] = ALL_SCHEMES,
    log_to_db: bool = True,
    write_preds: bool = True,
) -> pd.DataFrame:
    """Run every split scheme and return the side-by-side metrics table.

    Also persists per-(rung, scheme) out-of-fold predictions to
    ``results/preds_<tag>_<scheme>.parquet`` so CIs/diagnostics need no retrain.
    """
    rows = []
    for scheme in schemes:
        m, oof = evaluate_scheme(dataset, model_factory, scheme)
        rows.append(m)
        if write_preds and oof is not None:
            RESULTS_DIR.mkdir(parents=True, exist_ok=True)
            oof.to_parquet(RESULTS_DIR / f"preds_{tag}_{scheme}.parquet")
        log.info("[%s] %-12s roc_auc=%s pr_auc=%s p@50=%s lift@50=%s",
                 tag, scheme, m.get("roc_auc"), m.get("pr_auc"),
                 m.get("p@50"), m.get("lift@50"))
        if log_to_db and "error" not in m:
            log_run(
                run_id=f"{tag}-{scheme}-{uuid.uuid4().hex[:8]}",
                tag=tag, split=scheme, features=features, model=model, seed=seed,
                params={"n_features": dataset.X.shape[1]}, metrics=m,
            )
    table = pd.DataFrame(rows)
    front = ["scheme", "n", "n_pos", "base_rate", "roc_auc", "pr_auc",
             "p@50", "lift@50", "r@50"]
    cols = [c for c in front if c in table.columns] + [c for c in table.columns if c not in front]
    return table[cols]


# --------------------------------------------------------------------------- #
# Confidence intervals — family-clustered bootstrap
# --------------------------------------------------------------------------- #
# Viruses within a family are phylogenetically correlated, so the effective
# sample size is ~the number of families, not the number of rows. We therefore
# resample *whole families* (a cluster bootstrap). Comparisons are *paired* on
# virus_taxhash so the CI on a difference is far tighter than treating two AUCs
# as independent.

def _metric_arr(y: np.ndarray, s: np.ndarray, metric: str) -> float:
    if len(np.unique(y)) < 2:
        return float("nan")
    if metric == "roc_auc":
        return float(roc_auc_score(y, s))
    if metric == "pr_auc":
        return float(average_precision_score(y, s))
    if metric in ("lift@50", "p@50"):
        p, _ = precision_recall_at_k(y, s, 50)
        if metric == "p@50":
            return float(p)
        base = float(y.mean())
        return float(p / base) if base else float("nan")
    raise ValueError(f"unknown metric {metric!r}")


def load_preds(rung: str, scheme: str) -> pd.DataFrame | None:
    p = RESULTS_DIR / f"preds_{rung}_{scheme}.parquet"
    return pd.read_parquet(p) if p.exists() else None


def _family_clustered_bootstrap(a: pd.DataFrame, b: pd.DataFrame, metric: str,
                                n: int = 2000, seed: int = RANDOM_SEED) -> dict:
    """Paired family-clustered bootstrap CI on metric(a) - metric(b).

    ``a`` and ``b`` are OOF frames over the same viruses (two schemes of one rung,
    or two rungs at one scheme); aligned on virus_taxhash.
    """
    m = a.merge(b, on="virus_taxhash", suffixes=("_a", "_b"))
    fam = m["family_a"].fillna("__na__").to_numpy()
    families = np.unique(fam)
    pos_by_fam = {f: np.where(fam == f)[0] for f in families}
    ya, sa = m["y_true_a"].to_numpy(), m["y_score_a"].to_numpy()
    yb, sb = m["y_true_b"].to_numpy(), m["y_score_b"].to_numpy()

    point = _metric_arr(ya, sa, metric) - _metric_arr(yb, sb, metric)
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(n):
        chosen = rng.choice(families, size=len(families), replace=True)
        idx = np.concatenate([pos_by_fam[f] for f in chosen])
        diffs.append(_metric_arr(ya[idx], sa[idx], metric) - _metric_arr(yb[idx], sb[idx], metric))
    diffs = np.asarray(diffs, dtype=float)
    diffs = diffs[np.isfinite(diffs)]
    return {
        "metric": metric,
        "point": round(float(point), 4),
        "ci_lo": round(float(np.percentile(diffs, 2.5)), 4),
        "ci_hi": round(float(np.percentile(diffs, 97.5)), 4),
        "p_diff_le_0": round(float(np.mean(diffs <= 0)), 4),
        "n_boot": int(len(diffs)),
    }


def gap_ci(rung: str, scheme_a: str = "random", scheme_b: str = "tax_family",
           metrics: tuple[str, ...] = ("roc_auc", "pr_auc", "lift@50"), n: int = 2000) -> dict:
    """CI on the random→holdout *gap* for one rung (the headline number)."""
    a, b = load_preds(rung, scheme_a), load_preds(rung, scheme_b)
    if a is None or b is None:
        return {}
    return {met: _family_clustered_bootstrap(a, b, met, n) for met in metrics}


def compare_rungs(rung_a: str, rung_b: str, scheme: str,
                  metrics: tuple[str, ...] = ("lift@50", "pr_auc", "roc_auc", "p@50"),
                  n: int = 2000) -> dict:
    """CI on (rung_a - rung_b) at one scheme — e.g. does the genome beat effort?"""
    a, b = load_preds(rung_a, scheme), load_preds(rung_b, scheme)
    if a is None or b is None:
        return {}
    return {met: _family_clustered_bootstrap(a, b, met, n) for met in metrics}
