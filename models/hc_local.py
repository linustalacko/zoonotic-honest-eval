"""Local hill-climb round runner — the engine the self-paced loop calls.

Runs a batch of specs entirely on the local machine (features cached on disk),
appends to ``results/leaderboard.csv``, and returns the frontier sorted by the
honest objective (family-holdout PR-AUC). No Modal.
"""

from __future__ import annotations

import csv
import json
import os
import warnings

import pandas as pd

from features.composition import featurize_viruses
from models.dataset import load_labels
from models.hillclimb import run_specs

warnings.filterwarnings("ignore")  # sklearn deprecation noise during the search

LEADERBOARD = "results/leaderboard.csv"
BASELINE_FAM_PRAUC = 0.180  # composition_xgb, the bar to beat


def cohort() -> set:
    """The shared with-genome cohort (composition index) — keeps all specs comparable."""
    return set(featurize_viruses(load_labels()).index)


def _append(round_name: str, rows: list[dict]) -> None:
    is_new = not os.path.exists(LEADERBOARD)
    with open(LEADERBOARD, "a", newline="") as fh:
        w = csv.writer(fh)
        if is_new:
            w.writerow(["round", "label", "features", "model", "params", "n", "dims",
                        "fam_prauc", "fam_roc", "fam_lift", "rand_roc"])
        for r in rows:
            if "error" in r:
                continue
            w.writerow([round_name, r["label"], r["features"], r["model"],
                        json.dumps(r["params"]), r["n"], r["dims"],
                        r["fam_prauc"], r["fam_roc"], r["fam_lift"], r["rand_roc"]])


def run_round(specs: list[dict], round_name: str, restrict: set | None = None) -> list[dict]:
    restrict = restrict if restrict is not None else cohort()
    rows = run_specs(specs, restrict=restrict)
    _append(round_name, rows)
    ok = [r for r in rows if "error" not in r]
    ok.sort(key=lambda r: (r.get("fam_prauc") or 0), reverse=True)
    return ok


def leaderboard(top: int = 15) -> pd.DataFrame:
    if not os.path.exists(LEADERBOARD):
        return pd.DataFrame()
    df = pd.read_csv(LEADERBOARD)
    df = df.drop_duplicates(subset=["features", "model", "params"], keep="last")
    return df.sort_values("fam_prauc", ascending=False).head(top)


def show(rows: list[dict], round_name: str) -> None:
    print(f"\n{round_name}: {len(rows)} specs. baseline composition_xgb fam_PR={BASELINE_FAM_PRAUC}\n")
    print(f"{'label':28} {'feat':30} {'famPR':>6} {'famROC':>6} {'famLift':>7} {'randROC':>7}")
    for r in rows:
        beat = " BEATS" if (r["fam_prauc"] or 0) > BASELINE_FAM_PRAUC and "effort" not in r["features"] else ""
        print(f"{r['label'][:28]:28} {r['features'][:30]:30} {r['fam_prauc']:>6.3f} "
              f"{r['fam_roc']:>6.3f} {r['fam_lift']:>7.2f} {r['rand_roc']:>7.3f}{beat}")
