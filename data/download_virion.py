#!/usr/bin/env python
"""Download VIRION — the primary host-virus association table.

VIRION is the main label source: a virus "infects humans" iff it has a
documented association with *Homo sapiens*. We resolve the Zenodo concept record
(citable, immutable) and cache the association table under ``data/raw/virion/``.

Idempotent: re-running skips files already present at the expected size.
"""

from __future__ import annotations

import logging

from zoonotic.config import RAW_DIR, SOURCES, ensure_dirs
from zoonotic.io_utils import download_file, write_manifest, zenodo_files
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.download.virion")

# VIRION distributes the full association table plus component tables. We want
# the merged association file (and taxonomy), which are the large CSV/.csv.gz.
WANTED_SUFFIXES = (".csv.gz", ".csv", ".tsv.gz", ".tsv")


def main() -> None:
    setup_logging()
    ensure_dirs()
    src = SOURCES["virion"]
    out_dir = RAW_DIR / "virion"
    out_dir.mkdir(parents=True, exist_ok=True)

    rec, files = zenodo_files(src.zenodo_record)
    version = rec.get("metadata", {}).get("version") or rec.get("id")
    log.info("VIRION Zenodo record %s (version %s): %d files", rec.get("id"), version, len(files))

    downloaded = []
    for f in files:
        key = f["key"]
        if not key.lower().endswith(WANTED_SUFFIXES):
            log.info("skip (not a table): %s", key)
            continue
        url = f.get("links", {}).get("self") or f.get("links", {}).get("download")
        dest = out_dir / key
        download_file(url, dest, expected_size=f.get("size"))
        downloaded.append({"key": key, "size": f.get("size"), "url": url})

    if not downloaded:
        log.error(
            "No table files found on the Zenodo record. Inspect the record at "
            "https://zenodo.org/records/%s and adjust WANTED_SUFFIXES.",
            rec.get("id"),
        )

    write_manifest(
        out_dir / "MANIFEST.json",
        {
            "source": src.name,
            "license": src.license,
            "zenodo_record": rec.get("id"),
            "version": version,
            "doi": rec.get("doi"),
            "files": downloaded,
        },
    )
    log.info("VIRION done: %d table file(s) in %s", len(downloaded), out_dir)


if __name__ == "__main__":
    main()
