"""NCBI Entrez helpers for pulling representative viral genomes.

We fetch genomes at the **species** granularity (one labeled unit = one species)
and prefer **RefSeq** reference sequences, which are curated one-per-species and
far cleaner than bulk GenBank. Segmented viruses (influenza, bunyaviruses, …)
have multiple RefSeq segments; we keep all of them as a multi-FASTA per virus,
which is exactly what composition features want anyway.

All calls are rate-limited and every per-virus result is cached to disk, so the
genome download is fully resumable.
"""

from __future__ import annotations

import logging
import re
import threading
import time
from pathlib import Path

from Bio import Entrez

from zoonotic.config import (
    ENTREZ_RATE_LIMIT,
    GENOME_DIR,
    NCBI_API_KEY,
    NCBI_EMAIL,
)

log = logging.getLogger("zoonotic.ncbi")

# How many RefSeq records to keep per virus (covers multi-segment genomes).
MAX_RECORDS_PER_VIRUS = 12


def configure_entrez() -> None:
    """Set Entrez identity. NCBI requires an email; an API key raises the rate."""
    if not NCBI_EMAIL:
        raise RuntimeError(
            "NCBI_EMAIL is not set. Copy .env.example to .env and set NCBI_EMAIL "
            "(and optionally NCBI_API_KEY) before downloading genomes."
        )
    Entrez.email = NCBI_EMAIL
    if NCBI_API_KEY:
        Entrez.api_key = NCBI_API_KEY


# --------------------------------------------------------------------------- #
# Rate limiting (thread-safe token spacing)
# --------------------------------------------------------------------------- #
_lock = threading.Lock()
_min_interval = 1.0 / ENTREZ_RATE_LIMIT
_last_call = 0.0


def _throttle() -> None:
    global _last_call
    with _lock:
        now = time.monotonic()
        wait = _min_interval - (now - _last_call)
        if wait > 0:
            time.sleep(wait)
        _last_call = time.monotonic()


def _entrez(func, **kw):
    """Call an Entrez.* function with throttling + a couple of retries."""
    for attempt in range(3):
        _throttle()
        try:
            handle = func(**kw)
            data = handle.read()
            handle.close()
            return data
        except Exception as exc:  # noqa: BLE001 — Entrez raises a grab-bag of errors
            log.warning("entrez %s failed (try %s): %s", getattr(func, "__name__", func), attempt + 1, exc)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"entrez call failed: {func}")


def safe_name(name: str) -> str:
    """Filesystem-safe stem for a virus name. Non-strings (NaN) -> 'unknown'."""
    if not isinstance(name, str):
        return "unknown"
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip()).strip("_")[:120] or "unknown"


def genome_path(virus_name: str) -> Path:
    return GENOME_DIR / f"{safe_name(virus_name)}.fasta"


def _esearch_ids(term: str, retmax: int = 20) -> list[str]:
    import xml.etree.ElementTree as ET

    data = _entrez(Entrez.esearch, db="nuccore", term=term, retmax=retmax)
    root = ET.fromstring(data)
    return [e.text for e in root.findall(".//IdList/Id") if e.text]


def find_refseq_records(taxid: int | None, name: str | None) -> list[str]:
    """Find candidate genome record IDs for a virus, RefSeq-first.

    Falls back from (RefSeq complete genome) → (RefSeq any) → (GenBank complete)
    so we still get *something* for species without a RefSeq reference.
    """
    if taxid:
        organism = f"txid{int(taxid)}[Organism:exp]"
    elif name:
        organism = f'"{name}"[Organism]'
    else:
        return []

    queries = [
        f'{organism} AND srcdb_refseq[PROP] AND ("complete genome"[Title] OR "complete sequence"[Title])',
        f"{organism} AND srcdb_refseq[PROP]",
        f'{organism} AND ("complete genome"[Title] OR "complete sequence"[Title])',
    ]
    for q in queries:
        ids = _esearch_ids(q, retmax=MAX_RECORDS_PER_VIRUS)
        if ids:
            return ids
    return []


def fetch_fasta(record_ids: list[str]) -> str:
    """efetch FASTA for a list of nuccore IDs (returned as one multi-FASTA)."""
    if not record_ids:
        return ""
    return _entrez(
        Entrez.efetch,
        db="nuccore",
        id=",".join(record_ids),
        rettype="fasta",
        retmode="text",
    )


def fetch_genome_for_virus(
    virus_name: str,
    taxid: int | None = None,
    *,
    fallback_accessions: list[str] | None = None,
    force: bool = False,
) -> Path | None:
    """Fetch + cache a representative genome (multi-FASTA) for one virus.

    Resolution order: RefSeq reference by taxid/name -> any RefSeq -> complete
    genome -> VIRION's own ``fallback_accessions`` (the sequences that documented
    the host associations). Returns the FASTA path, or None if nothing was found.

    Resumable: an existing non-empty cache file is returned untouched; a virus
    with no hit gets an empty ``.empty`` marker so it is not re-queried.
    """
    out = genome_path(virus_name)
    marker = out.with_suffix(".empty")
    if out.exists() and out.stat().st_size > 0 and not force:
        return out
    if marker.exists() and not force:
        return None

    ids = find_refseq_records(taxid, virus_name)
    fasta = fetch_fasta(ids).strip()

    # Fallback: VIRION accessions (often partial genes, but better than nothing).
    if (not fasta or not fasta.startswith(">")) and fallback_accessions:
        fasta = fetch_fasta(fallback_accessions[:MAX_RECORDS_PER_VIRUS]).strip()

    if not fasta or not fasta.startswith(">"):
        marker.write_text("")  # negative cache
        return None

    out.write_text(fasta + "\n")
    return out
