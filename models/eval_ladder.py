"""Evaluate one ESM-2 scaling-ladder embedding the same way for every scale.

The scaling question is: as the protein language model grows (35M -> 15B), does
the *honest* (family-holdout) signal rise, or only the *leaky* (random-split)
signal? To answer it fairly every scale must go through an identical protocol:

  * same cohort  — restrict to viruses that also have composition features, the
    set every other rung is scored on;
  * same splits  — the persisted random / family / genus / temporal folds;
  * same probes  — a linear probe (logistic regression on frozen embeddings, the
    standard representation-quality readout) and a nonlinear probe (xgboost).

Run as the ladder embeddings land::

    uv run python -m models.eval_ladder \
        data/features_cache/esm_esm2_t48_15B_UR50D_top8_meanmax.parquet 15B

It appends one row per (scale, probe) to ``results/ladder.csv`` and persists OOF
predictions (``preds_<tag>_<scheme>.parquet``) so CIs/diagnostics need no retrain.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd

from models.dataset import build_dataset, load_labels
from models.evaluate import run_matrix
from models.hillclimb import make_estimator

LADDER_CSV = Path("results/ladder.csv")

# fair-esm checkpoint -> (params label, millions-of-params) for the x-axis.
_PARAMS = {
    "t6_8M": ("8M", 8), "t12_35M": ("35M", 35), "t30_150M": ("150M", 150),
    "t33_650M": ("650M", 650), "t36_3B": ("3B", 3000), "t48_15B": ("15B", 15000),
}


def _infer_scale(path: Path) -> tuple[str, int]:
    for key, val in _PARAMS.items():
        if key in path.name:
            return val
    m = re.search(r"(\d+)([MB])", path.name)
    if m:
        n = int(m.group(1)) * (1000 if m.group(2) == "B" else 1)
        return f"{m.group(1)}{m.group(2)}", n
    return path.stem, 0


def evaluate_embedding(parquet: Path, scale: str | None = None,
                       probes: tuple[str, ...] = ("logreg", "xgboost")) -> pd.DataFrame:
    esm = pd.read_parquet(parquet)
    label, n_params = _infer_scale(parquet)
    if scale:
        label = scale

    # Shared cohort: the viruses that also have composition features (what every
    # other rung is scored on). Keeps the ladder comparable to the baselines.
    from features.composition import featurize_viruses as comp_feat
    comp_idx = set(comp_feat(load_labels()).index)
    restrict = comp_idx & set(esm.index)

    ds = build_dataset(esm, restrict_to=restrict)
    rows = []
    for probe in probes:
        tag = f"esm{label}_{probe}"
        table = run_matrix(
            ds, lambda probe=probe: make_estimator(probe, {}),
            tag=tag, features=f"esm_{label}", model=probe, log_to_db=False,
        ).set_index("scheme")
        row = {
            "scale": label, "n_params_M": n_params, "probe": probe,
            "dims": int(esm.shape[1]), "n": int(ds.n), "n_pos": int(ds.y.sum()),
        }
        for scheme in ("random", "tax_family", "tax_genus", "temporal"):
            if scheme in table.index:
                row[f"{scheme}_roc"] = table.loc[scheme, "roc_auc"]
                row[f"{scheme}_pr"] = table.loc[scheme, "pr_auc"]
        rows.append(row)
        print(f"  {tag}: random_roc={row.get('random_roc')} "
              f"family_roc={row.get('tax_family_roc')} family_pr={row.get('tax_family_pr')}")

    out = pd.DataFrame(rows)
    LADDER_CSV.parent.mkdir(parents=True, exist_ok=True)
    if LADDER_CSV.exists():
        prev = pd.read_csv(LADDER_CSV)
        prev = prev[~((prev["scale"] == label) & (prev["probe"].isin(probes)))]
        out = pd.concat([prev, out], ignore_index=True)
    out.to_csv(LADDER_CSV, index=False)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("parquet", type=Path)
    ap.add_argument("scale", nargs="?", default=None)
    ap.add_argument("--probes", default="logreg,xgboost")
    args = ap.parse_args()
    df = evaluate_embedding(args.parquet, args.scale, tuple(args.probes.split(",")))
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
