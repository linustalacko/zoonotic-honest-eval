"""Model registry + the reference *ladder*, run bottom-up.

Each rung is a (feature_set, estimator) pair evaluated across every split scheme.
The ladder is designed so each rung is a control for the one above it:

  prior              constant = training base rate. The floor.
  family_prior       taxonomy memorisation (group-rate). Collapses to prior under
                     family holdout — the leakage demo.
  effort_only        research-effort + host-breadth metadata (non-genomic).
  composition_logreg k-mer + dinuc-bias, linear. "Is there linear signal?"
  composition_xgb    same features, gradient boosting. The zoonotic_rank stand-in.
  esm_logreg         ESM-2 protein embeddings. Must shrink the holdout gap to earn it.

A genome model is only interesting if, **under family holdout**, it beats BOTH
``family_prior`` and ``effort_only``. See docs/prior_work_and_fixes.md.

Run:
    python models/train.py --rung controls      # prior+family_prior+effort_only (no genomes)
    python models/train.py --rung composition_xgb
    python models/train.py --rung all
"""

from __future__ import annotations

import argparse
import logging

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from zoonotic.config import RANDOM_SEED, RESULTS_DIR, ensure_dirs
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.train")

# rung name -> (feature_set, estimator)
RUNGS: dict[str, tuple[str, str]] = {
    "prior": ("none", "prior"),
    "family_prior": ("family", "group_rate"),
    "effort_only": ("effort", "logreg"),
    "composition_logreg": ("composition", "logreg"),
    "composition_xgb": ("composition", "xgboost"),
    "esm_logreg": ("esm", "logreg"),
    "esm_xgb": ("esm", "xgboost"),
}
# Rungs that need no genomes — runnable immediately.
CONTROL_RUNGS = ("prior", "family_prior", "effort_only")
# Need genomes (composition features) but only the base deps — runnable on the
# standard Modal image.
GENOME_RUNGS = ("composition_logreg", "composition_xgb")
# Need genomes + the optional [embeddings] deps (torch/fair-esm) + ideally a GPU.
ESM_RUNGS = ("esm_logreg", "esm_xgb")


def make_model(name: str):
    """Factory returning a fresh sklearn-compatible estimator."""
    if name == "prior":
        return DummyClassifier(strategy="prior")
    if name == "group_rate":
        from models.baselines import GroupRateClassifier

        return GroupRateClassifier()
    if name == "logreg":
        return Pipeline([
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(
                max_iter=2000, C=1.0, class_weight="balanced", random_state=RANDOM_SEED
            )),
        ])
    if name == "xgboost":
        from xgboost import XGBClassifier

        return XGBClassifier(
            n_estimators=400, max_depth=4, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8, reg_lambda=1.0,
            scale_pos_weight=9.0, eval_metric="aucpr",
            tree_method="hist", random_state=RANDOM_SEED, n_jobs=-1,
        )
    raise ValueError(f"unknown model: {name!r}")


def _get_features(name: str):
    """Build a feature matrix (indexed by virus_taxhash) for a feature set."""
    from models.dataset import load_labels

    labels = load_labels()
    if name == "none":
        from features.metadata import constant_features

        return constant_features(labels)
    if name == "family":
        from features.metadata import family_features

        return family_features(labels)
    if name == "effort":
        from features.metadata import effort_features

        return effort_features(labels)
    if name == "composition":
        from features.composition import featurize_viruses

        return featurize_viruses(labels)
    if name == "esm":
        from features.embeddings import featurize_viruses

        return featurize_viruses(labels)
    raise ValueError(f"unknown feature set: {name!r}")


def run_rung(rung: str, *, restrict_to: set | None = None, tag: str | None = None,
             log_to_db: bool = True):
    """Evaluate one ladder rung across all split schemes; write metrics_<tag>.csv.

    ``restrict_to`` forces a shared cohort (e.g. with-genome set, or mammal-only);
    ``tag`` overrides the output stem (e.g. ``composition_xgb__mammal``).
    """
    from models.dataset import build_dataset
    from models.evaluate import run_matrix

    feat_set, model_name = RUNGS[rung]
    tag = tag or rung
    feats = _get_features(feat_set)
    ds = build_dataset(feats, restrict_to=restrict_to)
    log.info("[%s] dataset: %d viruses x %d features, base rate %.3f",
             tag, ds.n, ds.X.shape[1], ds.base_rate)

    table = run_matrix(
        ds, lambda: make_model(model_name),
        tag=tag, features=feat_set, model=model_name, seed=RANDOM_SEED, log_to_db=log_to_db,
    )
    out = RESULTS_DIR / f"metrics_{tag}.csv"
    table.to_csv(out, index=False)
    log.info("[%s] wrote %s", tag, out)
    return table


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--rung", default="controls",
        help="a rung name, or 'controls' (no genomes) / 'genomes' / 'all'",
    )
    args = ap.parse_args()

    setup_logging()
    ensure_dirs()

    if args.rung == "controls":
        rungs: tuple[str, ...] = CONTROL_RUNGS
    elif args.rung == "genomes":
        rungs = GENOME_RUNGS
    elif args.rung == "all":
        rungs = tuple(RUNGS)
    else:
        rungs = (args.rung,)

    for rung in rungs:
        table = run_rung(rung)
        print(f"\n=== {rung} ===")
        print(table.to_string(index=False))


if __name__ == "__main__":
    main()
