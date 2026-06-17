"""A generalisation-oriented model built from the honest-eval learnings.

Bet #1 (viral×human interaction modelling) needs structure/PPI data and a long
horizon, so it is out of scope. This module builds everything else the research
said was buildable, and tests the single question that matters:

    Under family holdout — where frozen ESM-2 15B alone only *tied* the one-line
    host-generalism baseline — can we actually *beat* that baseline by applying
    the generalisation learnings?

The learnings, operationalised:
  * **Deconfound the exposure-biased label.** The label ("observed in humans")
    is an opportunity proxy; that is why host-range breadth wins. We (a) include
    host generalism as covariates (fusion) and (b) a stricter variant that fits a
    host-generalism base model and trains the genome on the *residual* — the part
    of the label exposure does not explain.
  * **Targeted family-transcending features.** Composition carries CpG/UpA
    dinucleotide-bias (vertebrate antiviral-adaptation signatures that track
    adaptation, not ancestry) — included alongside the PLM embedding.
  * **Kill the probe-dimensionality artefact.** The 15B embedding is PCA-reduced
    per-fold to a fixed 128 dims, so a win cannot be "xgboost got more raw
    coordinates" (the caveat the dual-probe check surfaced).
  * **Family-robust training.** Family-balanced sample weights (group-DRO-lite)
    so the model cannot win by overfitting the well-sampled families.

Every variant emits OOF predictions in the standard format
(``results/preds_<tag>_<scheme>.parquet``), so the existing family-clustered
bootstrap (`models.evaluate.compare_rungs`) scores it against the baselines with
no special-casing.
"""

from __future__ import annotations

import logging
from collections import Counter

import numpy as np
import pandas as pd

from models.dataset import build_dataset, load_labels
from models.evaluate import RESULTS_DIR, compare_rungs, score_predictions

log = logging.getLogger("zoonotic.fusion")
SEED = 0
PCA_DIM = 128
ESM15B = "data/features_cache/esm_esm2_t48_15B_UR50D_top8_meanmax.parquet"


def _xgb_clf(**kw):
    from xgboost import XGBClassifier
    base = dict(n_estimators=400, max_depth=4, learning_rate=0.05, subsample=0.8,
                colsample_bytree=0.8, reg_lambda=1.0, scale_pos_weight=9.0,
                eval_metric="aucpr", tree_method="hist", random_state=SEED, n_jobs=-1)
    base.update(kw)
    return XGBClassifier(**base)


def _xgb_reg(**kw):
    from xgboost import XGBRegressor
    base = dict(n_estimators=400, max_depth=4, learning_rate=0.05, subsample=0.8,
                colsample_bytree=0.8, reg_lambda=1.0, tree_method="hist",
                random_state=SEED, n_jobs=-1)
    base.update(kw)
    return XGBRegressor(**base)


def _pca_fit_transform(Gtr: np.ndarray, Gte: np.ndarray, k: int):
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler().fit(Gtr)
    p = PCA(n_components=min(k, Gtr.shape[1]), random_state=SEED).fit(sc.transform(Gtr))
    return p.transform(sc.transform(Gtr)), p.transform(sc.transform(Gte))


def load_blocks() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Return (combined, g_cols, c_cols, e_cols) aligned on the shared cohort."""
    import warnings
    warnings.filterwarnings("ignore")
    labels = load_labels()
    g = pd.read_parquet(ESM15B).add_prefix("g_")
    from features.composition import featurize_viruses as comp_feat
    c = comp_feat(labels).add_prefix("c_")
    from features.metadata import effort_features
    e = effort_features(labels).add_prefix("e_")
    idx = g.index.intersection(c.index).intersection(e.index)
    combined = pd.concat([g.loc[idx], c.loc[idx], e.loc[idx]], axis=1)
    return combined, list(g.columns), list(c.columns), list(e.columns)


def _save_oof(ds, scheme, pos, scores, folds, tag) -> dict:
    idx = ds.X.index.to_numpy()
    y = ds.y.to_numpy()
    fams = ds.meta["family"].to_numpy()
    pos = np.asarray(pos)
    oof = pd.DataFrame({
        "virus_taxhash": idx[pos], "y_true": y[pos].astype(int),
        "y_score": np.asarray(scores, dtype=float), "fold": folds, "family": fams[pos],
    })
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    oof.to_parquet(RESULTS_DIR / f"preds_{tag}_{scheme}.parquet")
    m = score_predictions(oof["y_true"].to_numpy(), oof["y_score"].to_numpy())
    log.info("[%s] %-11s roc=%.3f pr=%.3f lift@50=%.2f", tag, scheme,
             m.get("roc_auc", float("nan")), m.get("pr_auc", float("nan")), m.get("lift@50", float("nan")))
    return m


def run_variant(ds, scheme, tag, *, gcols, ccols, ecols, pca=True,
                family_robust=False, deconfound=False, blocks=("g", "c", "e")) -> dict:
    X = ds.X
    y = ds.y.to_numpy()
    fams = ds.meta["family"].to_numpy()
    G, C, E = X[gcols].to_numpy(), X[ccols].to_numpy(), X[ecols].to_numpy()

    pos, scores, folds = [], [], []
    for fi, (tr, te) in enumerate(ds.folds(scheme)):
        if len(tr) == 0 or len(te) == 0:
            continue
        Gtr, Gte = (_pca_fit_transform(G[tr], G[te], PCA_DIM) if pca else (G[tr], G[te]))
        if deconfound:
            # base model on exposure (host generalism); genome predicts the residual
            from sklearn.linear_model import LogisticRegression
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler().fit(E[tr])
            base = LogisticRegression(C=1.0, class_weight="balanced", max_iter=2000,
                                      solver="liblinear", random_state=SEED).fit(sc.transform(E[tr]), y[tr])
            p_tr = base.predict_proba(sc.transform(E[tr]))[:, 1]
            p_te = base.predict_proba(sc.transform(E[te]))[:, 1]
            gen = np.hstack([Gtr, C[tr]])
            reg = _xgb_reg().fit(gen, y[tr] - p_tr)
            score = np.clip(p_te + reg.predict(np.hstack([Gte, C[te]])), 0.0, 1.0)
        else:
            blk_tr = {"g": Gtr, "c": C[tr], "e": E[tr]}
            blk_te = {"g": Gte, "c": C[te], "e": E[te]}
            Xtr = np.hstack([blk_tr[b] for b in blocks])
            Xte = np.hstack([blk_te[b] for b in blocks])
            clf = _xgb_clf()
            if family_robust:
                cnt = Counter(fams[tr])
                w = np.array([1.0 / cnt[f] for f in fams[tr]])
                w *= len(w) / w.sum()  # mean weight 1
                clf.fit(Xtr, y[tr], sample_weight=w)
            else:
                clf.fit(Xtr, y[tr])
            score = clf.predict_proba(Xte)[:, 1]
        pos.extend(te.tolist())
        scores.extend(np.asarray(score).tolist())
        folds.extend([fi] * len(te))
    return _save_oof(ds, scheme, pos, scores, folds, tag)


VARIANTS = {
    # ablations to attribute the fusion gain (the decisive checks)
    "genome_comp":  dict(pca=True, blocks=("g", "c")),   # NO host-range — is the gain clean?
    "comp_effort":  dict(pca=True, blocks=("c", "e")),   # NO genome — is the genome even needed?
    "deconfound":   dict(pca=True, deconfound=True),     # genome predicts the exposure residual
}


def main():
    from zoonotic.logging_utils import setup_logging
    setup_logging()
    combined, gcols, ccols, ecols = load_blocks()
    ds = build_dataset(combined, restrict_to=set(combined.index))
    log.info("cohort n=%d  dims: g=%d c=%d e=%d  base_rate=%.3f",
             ds.n, len(gcols), len(ccols), len(ecols), ds.base_rate)

    schemes = ("random", "tax_family")
    rows = []
    for tag, kw in VARIANTS.items():
        for s in schemes:
            run_variant(ds, s, tag, gcols=gcols, ccols=ccols, ecols=ecols, **kw)

    # The decisive tests, family holdout: each variant vs the baselines.
    print("\n=== family-holdout contrasts (paired family-clustered bootstrap) ===")
    for tag in VARIANTS:
        for base in ("effort_only", "esm15B_xgboost"):
            try:
                c = compare_rungs(tag, base, "tax_family", metrics=("roc_auc", "pr_auc", "lift@50"))

                def verdict(d):
                    return "BEATS" if d["ci_lo"] > 0 else ("loses" if d["ci_hi"] < 0 else "ties")
                print(f"\n{tag} − {base} @ family:")
                for m, d in c.items():
                    print(f"  {m:8s} {d['point']:+.4f} [{d['ci_lo']:+.4f},{d['ci_hi']:+.4f}] p={d['p_diff_le_0']}  -> {verdict(d)}")
                rows.append({"variant": tag, "vs": base, **{f"{m}_pt": d["point"] for m, d in c.items()}})
            except Exception as exc:  # noqa: BLE001
                print(f"{tag} vs {base}: ERR {str(exc)[:120]}")
    pd.DataFrame(rows).to_csv(RESULTS_DIR / "fusion_contrasts.csv", index=False)
    print("\nwrote results/fusion_contrasts.csv")


if __name__ == "__main__":
    main()
