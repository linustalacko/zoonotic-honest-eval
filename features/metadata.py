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
    label = (df["n_human_assoc"] > 0).astype(int)  # used only to *remove* the human host

    nonhuman_assoc = (df["n_assoc"] - df["n_human_assoc"]).clip(lower=0)
    nonhuman_hosts = (df["n_host_species"] - label).clip(lower=0)

    out = pd.DataFrame(index=df.index)
    out["log_nonhuman_assoc"] = np.log1p(nonhuman_assoc)
    out["log_nonhuman_hosts"] = np.log1p(nonhuman_hosts)
    out["n_host_classes"] = df["n_host_classes"].astype(float)
    out.index.name = "virus_taxhash"
    return out
