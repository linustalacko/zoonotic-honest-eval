#!/usr/bin/env python
"""Build per-virus "infects humans" labels from VIRION (+ CLOVER cross-check).

Label definition (documented here and in FINDINGS.md):
  * **Unit of analysis** = one VIRION-resolved virus taxon (``VirusTaxHashID``),
    carrying ICTV-style genus/family/order/class used for honest splits.
  * **Positive** = the virus has >=1 documented association with *Homo sapiens*.
  * **Negative** = the virus appears in VIRION with host associations but *none*
    to humans.

Critical biases this bakes in (kept explicit, not hidden):
  * *Absence of evidence != evidence of absence.* A "negative" may simply be
    understudied. This is the dominant label-noise source.
  * *Easy negatives.* Plant/insect viruses with no human link are trivial
    negatives that inflate AUC. We record host-class breadth
    (``has_mammal_host`` / ``has_vertebrate_host``) so downstream code can
    restrict negatives to a fair comparison set.

Output: ``data/processed/labels.parquet`` (+ a human-readable summary).
"""

from __future__ import annotations

import json
import logging

import pandas as pd

from zoonotic.config import PROCESSED_DIR, RAW_DIR, RESULTS_DIR, ensure_dirs
from zoonotic.logging_utils import setup_logging
from zoonotic.taxonomy import normalize_name

log = logging.getLogger("zoonotic.build_labels")

HUMAN_TAXID = 9606
VERTEBRATE_CLASSES = {
    "mammalia", "aves", "reptilia", "amphibia", "actinopterygii",
    "actinopteri", "chondrichthyes", "sarcopterygii", "myxini", "petromyzonti",
    "hyperoartia", "leptocardii", "ascidiacea",
}


def _load_virion() -> pd.DataFrame:
    """Return the VIRION association table with host+virus taxonomy joined in."""
    base = RAW_DIR / "virion"
    assoc = pd.read_csv(base / "virion.csv.gz", low_memory=False, encoding="latin-1")
    tax = pd.read_csv(base / "tax_table.csv.gz", low_memory=False)
    acc = pd.read_csv(base / "ncbi_accession.csv.gz", low_memory=False)

    tax_idx = tax.set_index("TaxHashID")
    host = tax_idx.add_prefix("Host")
    virus = tax_idx.add_prefix("Virus")
    df = assoc.merge(host, left_on="HostTaxHashID", right_index=True, how="left")
    df = df.merge(virus, left_on="VirusTaxHashID", right_index=True, how="left")
    df = df.merge(acc, on="AssocID", how="left")
    return df


def _clover_human_viruses() -> tuple[set[str], set[int]]:
    """Viruses with a documented human host in CLOVER, as (normalized names, taxids).

    We match VIRION<->CLOVER primarily on NCBI taxid (reliable) and fall back to
    normalized name (CLOVER ``Pathogen`` spellings differ from VIRION's).
    """
    f = RAW_DIR / "clover" / "CLOVER_1.0_Viruses_AssociationsFlatFile.csv"
    if not f.exists():
        log.warning("CLOVER virus file missing; skipping cross-check")
        return set(), set()
    c = pd.read_csv(f, low_memory=False, encoding="latin-1")
    human = c[c["Host"].astype(str).str.lower().eq("homo sapiens")]
    names = {normalize_name(n) for n in human["Pathogen"].dropna()}
    taxids = {int(t) for t in pd.to_numeric(human["PathogenTaxID"], errors="coerce").dropna()}
    return names, taxids


def build() -> pd.DataFrame:
    df = _load_virion()
    log.info("VIRION associations: %d rows", len(df))

    df["is_human"] = (
        df["HostScientificName"].astype(str).str.lower().eq("homo sapiens")
        | df["HostNCBITaxID"].eq(HUMAN_TAXID)
    )
    df["host_class_l"] = df["HostClass"].astype(str).str.lower()
    df["is_mammal"] = df["host_class_l"].eq("mammalia")
    df["is_vertebrate"] = df["host_class_l"].isin(VERTEBRATE_CLASSES)

    # earliest year we knew about this virus (for the temporal split)
    df["year"] = df["ReleaseYear"].fillna(df["CollectionYear"]).fillna(df["PublicationYear"])

    g = df.groupby("VirusTaxHashID", dropna=True)
    labels = pd.DataFrame({
        "virus_name": g["VirusScientificName"].first(),
        "ncbi_taxid": g["VirusNCBITaxID"].first(),
        "genus": g["VirusGenus"].first(),
        "family": g["VirusFamily"].first(),
        "order": g["VirusOrder"].first(),
        "class": g["VirusClass"].first(),
        "ictv_ratified": g["VirusICTVRatified"].first(),
        "label": g["is_human"].any().astype(int),
        "n_assoc": g.size(),
        "n_human_assoc": g["is_human"].sum().astype(int),
        "n_host_species": g["HostScientificName"].nunique(),
        "n_host_classes": g["HostClass"].nunique(),
        "has_mammal_host": g["is_mammal"].any(),
        "has_vertebrate_host": g["is_vertebrate"].any(),
        "first_year": g["year"].min(),
        # accessions for this virus (de-duplicated), for the genome-download fallback
        "accessions": g["NCBIAccession"].apply(
            lambda s: sorted({a for a in s.dropna().astype(str) if a and a != "nan"})
        ),
    }).reset_index().rename(columns={"VirusTaxHashID": "virus_taxhash"})

    labels["norm_name"] = labels["virus_name"].map(normalize_name)
    labels["n_accessions"] = labels["accessions"].map(len)
    labels["first_year"] = labels["first_year"].astype("Int64")

    # CLOVER cross-check (taxid-first, name fallback)
    clover_names, clover_taxids = _clover_human_viruses()
    by_name = labels["norm_name"].isin(clover_names)
    by_taxid = labels["ncbi_taxid"].astype("Int64").isin(clover_taxids)
    labels["clover_human"] = by_name | by_taxid

    return labels


def summarize(labels: pd.DataFrame) -> dict:
    fam = labels[labels["family"].notna()]
    mammal = labels[labels["has_mammal_host"]]
    pos = labels["label"].eq(1)
    summary = {
        "n_viruses": int(len(labels)),
        "n_positive": int(pos.sum()),
        "base_rate": round(float(pos.mean()), 4),
        "n_with_family": int(len(fam)),
        "base_rate_family_known": round(float(fam["label"].mean()), 4),
        "n_families": int(labels["family"].nunique()),
        "n_genera": int(labels["genus"].nunique()),
        "n_mammal_associated": int(len(mammal)),
        "base_rate_mammal_assoc": round(float(mammal["label"].mean()), 4),
        "n_with_taxid": int(labels["ncbi_taxid"].notna().sum()),
        "n_with_year": int(labels["first_year"].notna().sum()),
        "n_with_accession": int(labels["n_accessions"].gt(0).sum()),
        "clover_agreement_on_positives": round(
            float(labels.loc[pos, "clover_human"].mean()), 4
        ) if pos.any() else None,
    }
    return summary


def main() -> None:
    setup_logging()
    ensure_dirs()
    labels = build()
    summary = summarize(labels)

    out = PROCESSED_DIR / "labels.parquet"
    labels.to_parquet(out, index=False)
    # accessions is a list column; also drop a CSV without it for quick eyeballing
    labels.drop(columns=["accessions"]).to_csv(PROCESSED_DIR / "labels.csv", index=False)

    (RESULTS_DIR / "labels_summary.json").write_text(json.dumps(summary, indent=2))
    log.info("wrote %s (%d viruses)", out, len(labels))
    for k, v in summary.items():
        log.info("  %-28s %s", k, v)


if __name__ == "__main__":
    main()
