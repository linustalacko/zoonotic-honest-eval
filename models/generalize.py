"""Autonomous, time-budgeted generalisation search (designed to run all night).

Goal: a model that generalises BEYOND the current frontier (frozen ESM-2 15B, which
only ties the host-range baseline under family holdout) — i.e. significantly beats
the host-range baseline on PR-AUC and lift@50 under family AND genus holdout, with
the gain surviving (a) de-entanglement of the host-count feature and (b) a leakage
check.

Key early finding the search must harden: much of `effort_only`'s apparent strength
is the +1-human entanglement in n_host_species. The de-entangled host baseline
(host-CLASS count) is far weaker, so the genome may already beat a *clean* baseline.

    uv run python -m models.generalize allnight 9     # run ~9 h then stop
    uv run python -m models.generalize roundA         # one round

Each spec emits OOF preds (results/preds_<name>_<scheme>.parquet) so the paired
family-clustered bootstrap scores it vs the baselines. Progress is journaled to
results/generalization_journal.md and results/OVERNIGHT_SUMMARY.md continuously.
"""

from __future__ import annotations

import logging
import sys
import time
from collections import Counter

import numpy as np
import pandas as pd

from models.dataset import build_dataset, load_labels
from models.evaluate import RESULTS_DIR, compare_rungs, load_preds, score_predictions

log = logging.getLogger("zoonotic.generalize")
SEED = 0
ESM15B = "data/features_cache/esm_esm2_t48_15B_UR50D_top8_meanmax.parquet"
JOURNAL = RESULTS_DIR / "generalization_journal.md"
RUNS_CSV = RESULTS_DIR / "generalize_runs.csv"
SUMMARY = RESULTS_DIR / "OVERNIGHT_SUMMARY.md"
SCHEMES = ("random", "tax_family", "tax_genus")
# comparison rungs: full (entangled) baseline, clean baseline, genome frontier
CMP = ("effort_only", "A_baseline_clean", "esm15B_xgboost")
_BEST = {"pr": 0.0, "name": None, "note": ""}


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


def _pca(Gtr, Gte, k):
    if not k:
        return Gtr, Gte
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler().fit(Gtr)
    p = PCA(n_components=min(k, Gtr.shape[1]), random_state=SEED).fit(sc.transform(Gtr))
    return p.transform(sc.transform(Gtr)), p.transform(sc.transform(Gte))


def load_blocks():
    import warnings
    warnings.filterwarnings("ignore")
    lab = load_labels()
    g = pd.read_parquet(ESM15B).add_prefix("g_")
    from features.composition import featurize_viruses as comp_feat
    c = comp_feat(lab).add_prefix("c_")
    from features.metadata import effort_features
    efull = effort_features(lab).add_prefix("ef_")           # entangled (n_host_species)
    li = lab.set_index("virus_taxhash")
    eclean = np.log1p(li[["n_host_classes"]].astype(float)).add_prefix("ec_")  # de-entangled breadth
    blocks = {"g": g, "c": c, "efull": efull, "eclean": eclean}
    idx = g.index
    for b in blocks.values():
        idx = idx.intersection(b.index)
    combined = pd.concat([b.loc[idx] for b in blocks.values()], axis=1)
    return combined, {k: list(v.columns) for k, v in blocks.items()}


def run_spec(ds, cols, spec):
    y = ds.y.to_numpy()
    fams = ds.meta["family"].to_numpy()
    idx = ds.X.index.to_numpy()
    pca = spec.get("pca", 128)
    method = spec["method"]
    blocks = spec.get("blocks", ["g", "c", "efull"])

    def blk(name, rows):
        return ds.X[cols[name]].to_numpy()[rows]

    out = {}
    for scheme in SCHEMES:
        pos, sc, fo = [], [], []
        for fi, (tr, te) in enumerate(ds.folds(scheme)):
            if len(tr) == 0 or len(te) == 0:
                continue
            Gtr = Gte = None
            if "g" in blocks or method == "deconfound":
                Gtr, Gte = _pca(blk("g", tr), blk("g", te), pca)
            if method == "deconfound":
                from sklearn.linear_model import LogisticRegression
                from sklearn.preprocessing import StandardScaler
                B = spec.get("base", "efull")
                ssc = StandardScaler().fit(blk(B, tr))
                bm = LogisticRegression(C=1.0, class_weight="balanced", max_iter=2000,
                                        solver="liblinear", random_state=SEED).fit(ssc.transform(blk(B, tr)), y[tr])
                p_tr = bm.predict_proba(ssc.transform(blk(B, tr)))[:, 1]
                p_te = bm.predict_proba(ssc.transform(blk(B, te)))[:, 1]
                gtr = np.hstack([Gtr, blk("c", tr)])
                gte = np.hstack([Gte, blk("c", te)])
                resid = _xgb_reg().fit(gtr, y[tr] - p_tr).predict(gte)
                score = np.clip(p_te + resid, 0.0, 1.0)
            else:
                mt, me = [], []
                for b in blocks:
                    if b == "g":
                        mt.append(Gtr)
                        me.append(Gte)
                    else:
                        mt.append(blk(b, tr))
                        me.append(blk(b, te))
                Xtr, Xte = np.hstack(mt), np.hstack(me)
                w = None
                if method == "dro":  # family-balanced (group-DRO-lite)
                    cnt = Counter(fams[tr])
                    w = np.array([1.0 / cnt[f] for f in fams[tr]])
                    w *= len(w) / w.sum()
                elif method == "pw":  # propensity: downweight broad-host negatives (suspect unobserved positives)
                    hc = blk("eclean", tr).ravel()
                    z = (hc - hc.mean()) / (hc.std() + 1e-9)
                    w = np.where(y[tr] == 1, 1.0, 1.0 / (1.0 + np.exp(z)))
                    w *= len(w) / w.sum()
                if method == "logreg":
                    from sklearn.linear_model import LogisticRegression
                    from sklearn.pipeline import Pipeline
                    from sklearn.preprocessing import StandardScaler
                    clf = Pipeline([("s", StandardScaler()),
                                    ("c", LogisticRegression(C=1.0, class_weight="balanced",
                                     max_iter=2000, solver="liblinear", random_state=SEED))])
                    clf.fit(Xtr, y[tr])
                else:
                    clf = _xgb_clf()
                    if w is not None:
                        clf.fit(Xtr, y[tr], sample_weight=w)
                    else:
                        clf.fit(Xtr, y[tr])
                score = clf.predict_proba(Xte)[:, 1]
            pos.extend(te.tolist())
            sc.extend(np.asarray(score).tolist())
            fo.extend([fi] * len(te))
        pos = np.asarray(pos)
        oof = pd.DataFrame({"virus_taxhash": idx[pos], "y_true": y[pos].astype(int),
                            "y_score": np.asarray(sc), "fold": fo, "family": fams[pos]})
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        oof.to_parquet(RESULTS_DIR / f"preds_{spec['name']}_{scheme}.parquet")
        out[scheme] = score_predictions(oof["y_true"].to_numpy(), oof["y_score"].to_numpy())
    return out


def ensemble(name, tags, scheme):
    """Rank-average several rungs' OOF scores into a new rung (inner join)."""
    frames = []
    for t in tags:
        p = load_preds(t, scheme)
        if p is None:
            return None
        frames.append(p.set_index("virus_taxhash")[["y_true", "y_score", "family"]].rename(columns={"y_score": t}))
    j = frames[0][["y_true", "family"]].copy()
    for t, f in zip(tags, frames):
        j[t] = f[t].rank(pct=True)
    j["y_score"] = j[tags].mean(axis=1)
    oof = j.reset_index()[["virus_taxhash", "y_true", "y_score", "family"]]
    oof["fold"] = 0
    oof.to_parquet(RESULTS_DIR / f"preds_{name}_{scheme}.parquet")
    return score_predictions(oof["y_true"].to_numpy(), oof["y_score"].to_numpy())


def _ctr(tag, base, scheme):
    try:
        c = compare_rungs(tag, base, scheme, metrics=("roc_auc", "pr_auc", "lift@50"))
        return {m: (d["point"], d["ci_lo"], d["ci_hi"], d["p_diff_le_0"]) for m, d in c.items()}
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)[:70]}


def _verdict(v):
    return "BEATS" if v[1] > 0 else ("loses" if v[2] < 0 else "ties")


def journal(spec_name, desc, out):
    lines = [f"\n### {spec_name}  ({desc})"]
    for s in SCHEMES:
        m = out.get(s, {})
        lines.append(f"- {s}: ROC {m.get('roc_auc', float('nan')):.3f} | PR {m.get('pr_auc', float('nan')):.3f} | "
                     f"lift@50 {m.get('lift@50', float('nan')):.2f} | p@50 {m.get('p@50', float('nan')):.3f}")
    row = {"name": spec_name}
    for s in SCHEMES:
        for k in ("roc_auc", "pr_auc", "lift@50", "p@50"):
            row[f"{s}_{k}"] = out.get(s, {}).get(k)
    for base in CMP:
        if base == spec_name:
            continue
        for s in ("tax_family", "tax_genus"):
            d = _ctr(spec_name, base, s)
            if "error" in d:
                continue
            seg = "; ".join(f"{mm} {v[0]:+.3f}[{v[1]:+.3f},{v[2]:+.3f}]{_verdict(v)}" for mm, v in d.items())
            lines.append(f"- vs {base} @ {s}: {seg}")
            for mm, v in d.items():
                row[f"{base}_{s}_{mm}_pt"], row[f"{base}_{s}_{mm}_lo"] = v[0], v[1]
    with open(JOURNAL, "a") as f:
        f.write("\n".join(lines) + "\n")
    df = pd.DataFrame([row])
    if RUNS_CSV.exists():
        df = pd.concat([pd.read_csv(RUNS_CSV), df], ignore_index=True)
    df.to_csv(RUNS_CSV, index=False)
    # track best variant that BEATS the clean baseline on family PR
    fam_pr = out.get("tax_family", {}).get("pr_auc", 0) or 0
    cb = _ctr(spec_name, "A_baseline_clean", "tax_family")
    beats_clean = ("error" not in cb) and cb.get("pr_auc", (0, -1, 0, 1))[1] > 0
    if beats_clean and fam_pr > _BEST["pr"]:
        _BEST.update(pr=fam_pr, name=spec_name, note="beats clean baseline on family PR (CI>0)")


def update_summary(round_name, elapsed_h):
    best = (f"`{_BEST['name']}` — family PR {_BEST['pr']:.3f} ({_BEST['note']})"
            if _BEST["name"] else "none yet clears the bar")
    txt = (f"\n## Latest status ({elapsed_h:.1f} h elapsed; last round: {round_name})\n"
           f"- **Best clean generaliser so far:** {best}\n"
           f"- Full detail in `generalization_journal.md`; numbers in `generalize_runs.csv`.\n")
    with open(SUMMARY, "a") as f:
        f.write(txt)


# ---- rounds -----------------------------------------------------------------
def specs_for(round_name):
    if round_name == "roundA":          # de-entanglement + genus holdout
        return [
            ("A_baseline_clean", "de-entangled host baseline (host-class)", dict(blocks=["eclean"], method="xgb", pca=0)),
            ("A_baseline_clean_lr", "clean host baseline, logreg", dict(blocks=["eclean"], method="logreg", pca=0)),
            ("A_fusion_full", "genome+comp+host(entangled)", dict(blocks=["g", "c", "efull"], method="xgb")),
            ("A_fusion_clean", "genome+comp+host(clean)", dict(blocks=["g", "c", "eclean"], method="xgb")),
            ("A_deconf_full", "exposure(entangled) base + genome residual", dict(blocks=["g", "c"], method="deconfound", base="efull")),
            ("A_deconf_clean", "exposure(clean) base + genome residual", dict(blocks=["g", "c"], method="deconfound", base="eclean")),
        ]
    if round_name == "roundB":          # harden: probes / DG / pca sweep on the clean fusion + genome
        return [
            ("B_genome_only", "15B genome only (PCA128)", dict(blocks=["g"], method="xgb")),
            ("B_fusion_clean_dro", "fusion(clean)+family-DRO", dict(blocks=["g", "c", "eclean"], method="dro")),
            ("B_fusion_clean_lr", "fusion(clean) logreg", dict(blocks=["g", "c", "eclean"], method="logreg")),
            ("B_fusion_clean_pca256", "fusion(clean) PCA256", dict(blocks=["g", "c", "eclean"], method="xgb", pca=256)),
            ("B_fusion_clean_pca64", "fusion(clean) PCA64", dict(blocks=["g", "c", "eclean"], method="xgb", pca=64)),
            ("B_deconf_clean_dro", "deconf(clean)+nothing (residual already)", dict(blocks=["g", "c"], method="deconfound", base="eclean")),
        ]
    if round_name == "roundC":          # label deconfounding / propensity
        return [
            ("C_fusion_clean_pw", "fusion(clean)+propensity-weight", dict(blocks=["g", "c", "eclean"], method="pw")),
            ("C_genome_pw", "genome+comp+propensity-weight", dict(blocks=["g", "c"], method="pw")),
        ]
    return []


ENSEMBLES = {
    "E_deconf_fusion": ["A_deconf_clean", "A_fusion_clean"],
    "E_genome_host": ["B_genome_only", "A_baseline_clean"],
    "E_all": ["A_deconf_clean", "A_fusion_clean", "B_genome_only", "A_baseline_clean"],
}


def run_round(ds, cols, round_name):
    specs = specs_for(round_name)
    if not specs:
        return
    with open(JOURNAL, "a") as f:
        f.write(f"\n## {round_name}\n")
    for name, desc, spec in specs:
        spec = dict(spec, name=name)
        try:
            out = run_spec(ds, cols, spec)
            journal(name, desc, out)
            log.info("  %s: family PR=%.3f lift=%.2f", name,
                     out["tax_family"].get("pr_auc", float("nan")), out["tax_family"].get("lift@50", float("nan")))
        except Exception as exc:  # noqa: BLE001
            log.warning("  %s FAILED: %s", name, str(exc)[:160])


def run_ensembles():
    with open(JOURNAL, "a") as f:
        f.write("\n## ensembles\n")
    for name, tags in ENSEMBLES.items():
        out = {}
        for s in SCHEMES:
            r = ensemble(name, tags, s)
            if r:
                out[s] = r
        if out:
            journal(name, f"rank-avg of {tags}", out)
            log.info("  %s: family PR=%.3f", name, out.get("tax_family", {}).get("pr_auc", float("nan")))


def all_night(hours):
    from zoonotic.logging_utils import setup_logging
    setup_logging()
    t0 = time.time()
    combined, cols = load_blocks()
    ds = build_dataset(combined, restrict_to=set(combined.index))
    log.info("ALL-NIGHT start: budget %.1f h, n=%d base_rate=%.3f", hours, ds.n, ds.base_rate)
    with open(JOURNAL, "a") as f:
        f.write(f"\n# ALL-NIGHT RUN (budget {hours} h, n={ds.n})\n")

    queue = ["roundA", "roundB", "roundC"]
    for rn in queue:
        if time.time() - t0 > hours * 3600:
            break
        log.info("=== %s (%.1f h elapsed) ===", rn, (time.time() - t0) / 3600)
        run_round(ds, cols, rn)
        run_ensembles()
        update_summary(rn, (time.time() - t0) / 3600)

    # deepen: PCA-dim + seed sweeps on the best family-PR fusion config until budget
    dims = [96, 160, 192, 320, 512]
    seeds = [1, 2, 3, 4, 5]
    i = 0
    while time.time() - t0 < hours * 3600:
        global SEED
        d = dims[i % len(dims)]
        SEED = seeds[i % len(seeds)]
        name = f"D_fusion_clean_pca{d}_s{SEED}"
        try:
            out = run_spec(ds, cols, dict(name=name, blocks=["g", "c", "eclean"], method="xgb", pca=d))
            journal(name, f"deepen sweep pca={d} seed={SEED}", out)
            run_ensembles()
            update_summary("deepen", (time.time() - t0) / 3600)
            log.info("  [deepen] %s family PR=%.3f (%.1f h)", name,
                     out["tax_family"].get("pr_auc", float("nan")), (time.time() - t0) / 3600)
        except Exception as exc:  # noqa: BLE001
            log.warning("  deepen %s failed: %s", name, str(exc)[:120])
        i += 1
    SEED = 0
    with open(JOURNAL, "a") as f:
        f.write(f"\n# ALL-NIGHT DONE ({(time.time()-t0)/3600:.1f} h). Best: {_BEST}\n")
    log.info("ALL-NIGHT done %.1f h. best=%s", (time.time() - t0) / 3600, _BEST)


def main():
    from zoonotic.logging_utils import setup_logging
    setup_logging()
    arg = sys.argv[1] if len(sys.argv) > 1 else "roundA"
    if arg == "allnight":
        all_night(float(sys.argv[2]) if len(sys.argv) > 2 else 9.0)
        return
    combined, cols = load_blocks()
    ds = build_dataset(combined, restrict_to=set(combined.index))
    run_round(ds, cols, arg)
    run_ensembles()


if __name__ == "__main__":
    main()
