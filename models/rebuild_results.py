"""Regenerate ONE internally-consistent results set for the paper.

The repo accumulated metrics/preds/CIs across several iterations of the feature
definitions (notably the effort -> host-generalism correction), so the serialized
numbers no longer reconcile (e.g. the family-holdout effort PR-AUC is 0.30 in the
metrics CSV but the cached CI implies ~0.22). Rather than patch prose, this script
rebuilds everything from the current code in one pass:

  * every rung on ONE shared with-genome cohort (so n and base rate match);
  * fresh OOF preds + metrics for each (rung, scheme);
  * the family-clustered bootstrap CIs for every contrast the paper cites.

Outputs results/canonical_results.json (the single source of truth) and prints a
reconciliation table. ESM rungs sit on the composition ∩ ESM set (one virus fewer);
the paired bootstraps inner-join on virus_taxhash, so contrasts stay valid.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from models.dataset import build_dataset, load_labels, load_splits
from models.evaluate import compare_rungs, gap_ci
from models.train import run_rung
from zoonotic.config import RESULTS_DIR

CANON = RESULTS_DIR / "canonical_results.json"
METRICS = ("roc_auc", "pr_auc", "lift@50", "p@50")
ALL_RUNGS = ("prior", "family_prior", "effort_only",
             "composition_logreg", "composition_xgb", "esm_logreg", "esm_xgb")


def shared_cohort() -> set:
    """With-genome cohort: composition features ∩ the split assignments."""
    from features.composition import featurize_viruses as comp_feat
    comp = comp_feat(load_labels())
    splits = load_splits()
    return set(comp.index) & set(splits["virus_taxhash"])


def rebuild(rungs: tuple[str, ...] = ALL_RUNGS) -> dict:
    cohort = shared_cohort()
    print(f"shared with-genome cohort: n={len(cohort)}")

    matrix: dict[str, list] = {}
    for rung in rungs:
        table = run_rung(rung, restrict_to=cohort, tag=rung, log_to_db=False)
        matrix[rung] = table.to_dict("records")
        fam = next((r for r in matrix[rung] if r.get("scheme") == "tax_family"), {})
        rnd = next((r for r in matrix[rung] if r.get("scheme") == "random"), {})
        print(f"  {rung:20s} random ROC={rnd.get('roc_auc')} PR={rnd.get('pr_auc')} | "
              f"family ROC={fam.get('roc_auc')} PR={fam.get('pr_auc')} lift@50={fam.get('lift@50')}")

    # CIs: the leakage gap, and the decisive family-holdout contrasts.
    cis = {
        "gap_composition_xgb": gap_ci("composition_xgb", metrics=METRICS),
        "gap_esm_xgb": gap_ci("esm_xgb", metrics=METRICS),
        # Does the genome beat pure taxonomy memorisation under family holdout?
        "composition_xgb_vs_family_prior__family": compare_rungs(
            "composition_xgb", "family_prior", "tax_family", metrics=METRICS),
        # Does the genome beat the non-genomic host-generalism baseline?
        "composition_xgb_vs_effort_only__family": compare_rungs(
            "composition_xgb", "effort_only", "tax_family", metrics=METRICS),
        # Does the protein-LM beat composition? beat generalism?
        "esm_xgb_vs_composition_xgb__family": compare_rungs(
            "esm_xgb", "composition_xgb", "tax_family", metrics=METRICS),
        "esm_xgb_vs_effort_only__family": compare_rungs(
            "esm_xgb", "effort_only", "tax_family", metrics=METRICS),
    }

    out = {"cohort_n": len(cohort), "metrics_matrix": matrix, "confidence_intervals": cis}
    CANON.parent.mkdir(parents=True, exist_ok=True)
    CANON.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {CANON}")

    print("\n=== family-holdout contrasts (point [lo, hi] p(diff<=0)) ===")
    for name, ci in cis.items():
        print(f"\n{name}")
        for met, d in ci.items():
            if d:
                print(f"  {met:9s} {d['point']:+.4f} [{d['ci_lo']:+.4f}, {d['ci_hi']:+.4f}] "
                      f"p={d['p_diff_le_0']}")
    return out


if __name__ == "__main__":
    rebuild()
