"""Non-genomic *control* features: research-effort proxies and taxonomy.

These power the control rungs of the ladder. A genome model only earns its keep
if, under taxonomic holdout, it beats both of these — otherwise its apparent
skill is really (a) taxonomy memorisation or (b) research-effort bias.
See docs/prior_work_and_fixes.md §F1–F2.

**Leakage discipline (important).** Several label-adjacent columns are
mechanically implied by the target and must NOT be used as "effort":
  * ``n_human_assoc`` *is* the label source (label = n_human_assoc > 0).
  * ``n_accessions`` ≈ ``n_assoc`` and is inflated by human-derived sequences.
  * ``has_mammal_host`` / ``has_vertebrate_host`` are TRUE for every positive
    (humans are mammalian vertebrates), so they encode the label.
We therefore build effort from **non-human** signal only: associations and host
breadth with the human contribution removed.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _by_taxhash(viruses: pd.DataFrame) -> pd.DataFrame:
    return viruses.set_index("virus_taxhash") if "virus_taxhash" in viruses.columns else viruses


def constant_features(viruses: pd.DataFrame) -> pd.DataFrame:
    """A single constant column — for the ``prior`` rung (model ignores X)."""
    df = _by_taxhash(viruses)
    out = pd.DataFrame({"const": np.ones(len(df))}, index=df.index)
    out.index.name = "virus_taxhash"
    return out


def family_features(viruses: pd.DataFrame) -> pd.DataFrame:
    """A single ``family`` column — for the ``family_prior`` (group-rate) rung."""
    df = _by_taxhash(viruses)
    out = pd.DataFrame({"family": df["family"].fillna("__unknown__").astype(str)}, index=df.index)
    out.index.name = "virus_taxhash"
    return out


def effort_features(viruses: pd.DataFrame) -> pd.DataFrame:
    """Research-effort + host-breadth proxies, with the human signal removed.

    Columns (all non-genomic, all label-decontaminated):
      * ``log_nonhuman_assoc``  — log1p(total associations − human associations)
      * ``log_nonhuman_hosts``  — log1p(distinct host species − the human host)
      * ``n_host_classes``      — distinct host taxonomic classes (host breadth)
    """
    df = _by_taxhash(viruses)

    # The least label-entangled non-genomic baseline: host-range BREADTH
    # (generalism), which is also a genuine biological predictor of zoonosis
    # (Olival 2017). We deliberately do NOT use association/sequence COUNTS:
    #   * ``n_assoc`` includes the human detections, so it is partly the label;
    #   * ``n_assoc - n_human_assoc`` collapses human-only viruses to 0 — a
    #     near-deterministic tell a flexible model exploits (effort+xgb hit 0.80
    #     family-PR via exactly this leak; see docs/raising_the_ceiling.md).
    # Host counts include the human host (+1 for positives) — a mild, documented
    # residual entanglement, far smaller than the count-based leaks.
    out = pd.DataFrame(index=df.index)
    out["log_host_species"] = np.log1p(df["n_host_species"])
    out["n_host_classes"] = df["n_host_classes"].astype(float)
    out.index.name = "virus_taxhash"
    return out
