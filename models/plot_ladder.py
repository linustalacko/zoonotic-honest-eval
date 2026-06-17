"""The ESM-2 scaling-ladder figure: does scale buy *honest* signal?

Two panels over ESM-2 parameter count (log x), one shared cohort, one protocol
(top-8 proteins, mean+max pool, identical family-clustered harness):

  * LEFT  — ROC-AUC: the random-split (leaky) curve barely moves while the
    family-holdout (honest) curve climbs with scale; the leakage gap shrinks.
  * RIGHT — family-holdout PR-AUC: the honest curve rises monotonically toward
    the host-generalism baseline it could not touch at small scale, drawing level
    by 15B (the crossover).

    uv run python -m models.plot_ladder

Monochrome to match the project site. Reads ``results/ladder.csv`` (xgboost
probe). Reference lines (composition, host-generalism) are read from the
canonical metric CSVs so the figure can never drift from the tables.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

LADDER_CSV = Path("results/ladder.csv")


def _ref(rung: str, scheme: str, col: str) -> float:
    df = pd.read_csv(Path("results") / f"metrics_{rung}.csv")
    return float(df[df["scheme"] == scheme][col].iloc[0])


def render(probe: str = "xgboost", out_stem: str = "scaling_ladder") -> list[Path]:
    df = pd.read_csv(LADDER_CSV)
    df = df[df["probe"] == probe].sort_values("n_params_M")
    if df.empty:
        raise SystemExit(f"no '{probe}' rows in {LADDER_CSV}")

    x = df["n_params_M"].to_numpy()
    labels = df["scale"].tolist()

    comp_fam_roc = _ref("composition_xgb", "tax_family", "roc_auc")
    comp_rnd_roc = _ref("composition_xgb", "random", "roc_auc")
    gen_fam_roc = _ref("effort_only", "tax_family", "roc_auc")
    comp_fam_pr = _ref("composition_xgb", "tax_family", "pr_auc")
    gen_fam_pr = _ref("effort_only", "tax_family", "pr_auc")

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 4.8))

    # ---- LEFT: ROC, leaky vs honest ----
    axL.set_xscale("log")
    axL.axhline(comp_rnd_roc, color="0.65", ls=":", lw=1.0)
    axL.axhline(comp_fam_roc, color="0.65", ls=":", lw=1.0)
    axL.axhline(gen_fam_roc, color="0.65", ls="-.", lw=1.0)
    axL.text(x.max(), comp_rnd_roc + 0.006, "composition, random", ha="right", va="bottom", fontsize=7.5, color="0.45")
    axL.text(x.min(), comp_fam_roc + 0.005, "composition, family holdout", ha="left", va="bottom", fontsize=7.5, color="0.45")
    axL.text(x.max(), gen_fam_roc - 0.012, "host-generalism baseline", ha="right", va="top", fontsize=7.5, color="0.45")
    axL.plot(x, df["random_roc"], marker="o", color="black", lw=2.0, label="ESM-2, random split (leaky)")
    axL.plot(x, df["tax_family_roc"], marker="s", mfc="white", color="black", lw=2.0, ls="--",
             label="ESM-2, family holdout (honest)")
    axL.set_ylim(0.45, 0.97)
    axL.set_ylabel("ROC-AUC")
    axL.set_title("Scale lifts the honest score, not the leaky one", fontsize=10.5)
    axL.legend(loc="center right", fontsize=8, frameon=False)

    # ---- RIGHT: family-holdout PR-AUC crossover ----
    axR.set_xscale("log")
    axR.axhline(gen_fam_pr, color="black", ls="-.", lw=1.3)
    axR.axhline(comp_fam_pr, color="0.65", ls=":", lw=1.0)
    axR.text(x.max(), gen_fam_pr + 0.006, "host-generalism baseline (one line of metadata)",
             ha="right", va="bottom", fontsize=7.5, color="0.2")
    axR.text(x.max(), comp_fam_pr - 0.010, "composition (k-mer) baseline", ha="right", va="top", fontsize=7.5, color="0.45")
    axR.plot(x, df["tax_family_pr"], marker="s", color="black", lw=2.2, label="ESM-2, family holdout")
    axR.set_ylim(0.10, 0.34)
    axR.set_ylabel("PR-AUC (family holdout)")
    axR.set_title("The genome rises to meet the trivial baseline by 15B", fontsize=10.5)
    axR.legend(loc="upper left", fontsize=8, frameon=False)

    for ax in (axL, axR):
        ax.set_xlabel("ESM-2 parameters (log scale)")
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.tight_layout()

    outs = []
    for d in (Path("results"), Path("docs")):
        d.mkdir(parents=True, exist_ok=True)
        for ext in ("png", "svg"):
            p = d / f"{out_stem}.{ext}"
            fig.savefig(p, dpi=200, bbox_inches="tight")
            outs.append(p)
    plt.close(fig)
    print(f"refs: comp_fam_roc={comp_fam_roc:.3f} gen_fam_roc={gen_fam_roc:.3f} "
          f"comp_fam_pr={comp_fam_pr:.3f} gen_fam_pr={gen_fam_pr:.3f}")
    return outs


if __name__ == "__main__":
    for p in render():
        print("wrote", p)
