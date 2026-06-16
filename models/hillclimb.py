"""Automated hill-climbing over (features × model × params) to maximise *honest*
generalisation.

The objective is **family-holdout** performance (PR-AUC primary, watchlist lift
secondary) — never the leaky random split, which would just reward taxonomy
overfitting. A round evaluates a batch of candidate specs through the same
honest-eval harness and returns a small leaderboard; the driver proposes the next
batch around the winners. Selection bias is real (trying N specs and keeping the
best inflates the apparent winner), so finalists are re-checked with the
family-clustered bootstrap CI.
"""

from __future__ import annotations

import pandas as pd

from zoonotic.config import RANDOM_SEED


def make_estimator(mtype: str, params: dict):
    p = dict(params or {})
    if mtype == "xgboost":
        from xgboost import XGBClassifier
        base = dict(n_estimators=400, max_depth=4, learning_rate=0.05, subsample=0.8,
                    colsample_bytree=0.8, reg_lambda=1.0, scale_pos_weight=9.0,
                    eval_metric="aucpr", tree_method="hist", random_state=RANDOM_SEED, n_jobs=-1)
        base.update(p)
        return XGBClassifier(**base)
    if mtype == "histgb":
        from sklearn.ensemble import HistGradientBoostingClassifier
        base = dict(learning_rate=0.05, max_iter=400, l2_regularization=1.0,
                    class_weight="balanced", random_state=RANDOM_SEED)
        base.update(p)
        return HistGradientBoostingClassifier(**base)
    if mtype in ("logreg", "linear_svc"):
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        base = dict(C=1.0, penalty="l2", solver="liblinear", max_iter=2000,
                    class_weight="balanced", random_state=RANDOM_SEED)
        base.update(p)
        return Pipeline([("s", StandardScaler()), ("c", LogisticRegression(**base))])
    if mtype == "random_forest":
        from sklearn.ensemble import RandomForestClassifier
        base = dict(n_estimators=600, max_depth=None, class_weight="balanced_subsample",
                    n_jobs=-1, random_state=RANDOM_SEED)
        base.update(p)
        return RandomForestClassifier(**base)
    if mtype == "extra_trees":
        from sklearn.ensemble import ExtraTreesClassifier
        base = dict(n_estimators=800, max_depth=None, class_weight="balanced_subsample",
                    n_jobs=-1, random_state=RANDOM_SEED)
        base.update(p)
        return ExtraTreesClassifier(**base)
    if mtype == "mlp":
        from sklearn.neural_network import MLPClassifier
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        base = dict(hidden_layer_sizes=(128, 32), alpha=1e-3, max_iter=300,
                    early_stopping=True, random_state=RANDOM_SEED)
        base.update(p)
        return Pipeline([("s", StandardScaler()), ("c", MLPClassifier(**base))])
    raise ValueError(f"unknown model type {mtype!r}")


def _feature_matrix(name: str, labels: pd.DataFrame) -> pd.DataFrame:
    if name == "composition":
        from features.composition import featurize_viruses
        return featurize_viruses(labels)
    if name == "esm":
        from features.embeddings import featurize_viruses
        return featurize_viruses(labels)
    if name == "effort":
        from features.metadata import effort_features
        return effort_features(labels)
    from features.extra import _GENERATORS, featurize
    if name in _GENERATORS:
        return featurize(name, labels)
    raise ValueError(f"unknown feature set {name!r}")


def combine_features(names: list[str], labels: pd.DataFrame) -> pd.DataFrame:
    mats = [(n, _feature_matrix(n, labels)) for n in names]
    idx = mats[0][1].index
    for _, m in mats[1:]:
        idx = idx.intersection(m.index)
    return pd.concat([m.loc[idx].add_prefix(f"{n}_") for n, m in mats], axis=1)


def evaluate_spec(spec: dict, restrict: set | None = None) -> dict:
    """Evaluate one (features, model, params) spec; return its leaderboard row."""
    from models.dataset import build_dataset, load_labels
    from models.evaluate import evaluate_scheme

    labels = load_labels()
    X = combine_features(spec["features"], labels)
    ds = build_dataset(X, restrict_to=restrict)

    def factory():
        return make_estimator(spec["model"], spec.get("params", {}))

    out = {s: evaluate_scheme(ds, factory, s)[0] for s in ("random", "tax_family")}
    fam, rnd = out["tax_family"], out["random"]
    return {
        "label": spec.get("label", ""),
        "features": "+".join(spec["features"]),
        "model": spec["model"],
        "params": spec.get("params", {}),
        "n": fam.get("n"), "dims": int(X.shape[1]),
        "fam_prauc": fam.get("pr_auc"), "fam_roc": fam.get("roc_auc"),
        "fam_lift": fam.get("lift@50"), "fam_p50": fam.get("p@50"),
        "rand_roc": rnd.get("roc_auc"), "rand_prauc": rnd.get("pr_auc"),
    }


def run_specs(specs: list[dict], restrict: set | None = None) -> list[dict]:
    rows = []
    for s in specs:
        try:
            rows.append(evaluate_spec(s, restrict))
        except Exception as exc:  # noqa: BLE001 — keep the round going
            rows.append({"label": s.get("label", ""), "error": str(exc)[:200]})
    return rows
