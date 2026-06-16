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


def evaluate_scheme(dataset: Dataset, model_factory, scheme: str) -> dict:
    """Fit/predict across a scheme's folds and score the pooled held-out preds.

    Pooling out-of-fold predictions gives one honest metric set per scheme. We
    also keep per-fold ROC-AUC (mean±std) since taxonomic folds vary a lot.
    """
    X = dataset.X.to_numpy()
    y = dataset.y.to_numpy()

    oof_idx: list[int] = []
    oof_score: list[float] = []
    fold_aucs: list[float] = []

    for train_idx, test_idx in dataset.folds(scheme):
        if len(test_idx) == 0 or len(train_idx) == 0:
            continue
        model = model_factory()
        model.fit(X[train_idx], y[train_idx])
        score = model.predict_proba(X[test_idx])[:, 1]
        oof_idx.extend(test_idx.tolist())
        oof_score.extend(score.tolist())
        if len(np.unique(y[test_idx])) == 2:
            fold_aucs.append(roc_auc_score(y[test_idx], score))

    if not oof_idx:
        return {"scheme": scheme, "error": "no evaluable folds"}

    y_oof = y[np.array(oof_idx)]
    metrics = score_predictions(y_oof, np.array(oof_score))
    metrics["scheme"] = scheme
    metrics["roc_auc_fold_mean"] = round(float(np.mean(fold_aucs)), 4) if fold_aucs else float("nan")
    metrics["roc_auc_fold_std"] = round(float(np.std(fold_aucs)), 4) if fold_aucs else float("nan")
    return metrics


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
) -> pd.DataFrame:
    """Run every split scheme and return the side-by-side metrics table."""
    rows = []
    for scheme in schemes:
        m = evaluate_scheme(dataset, model_factory, scheme)
        rows.append(m)
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
