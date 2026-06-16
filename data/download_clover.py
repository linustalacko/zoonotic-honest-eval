#!/usr/bin/env python
"""Download CLOVER — reconciled host-virus associations (HP3+GMPD2+EID2+Shaw).

Used to cross-check / supplement VIRION human-infection labels. Resolved via the
GitHub contents API so we pin to a ref and grab whatever CSVs the directory holds
without hardcoding fragile filenames.
"""

from __future__ import annotations

import logging

from zoonotic.config import RAW_DIR, SOURCES, ensure_dirs
from zoonotic.io_utils import download_file, github_list_dir, write_manifest
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.download.clover")


def main() -> None:
    setup_logging()
    ensure_dirs()
    src = SOURCES["clover"]
    out_dir = RAW_DIR / "clover"
    out_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict] = []
    for path in src.github_paths:
        try:
            entries.extend(github_list_dir(src.github_repo, path, src.github_ref))
        except Exception as exc:  # noqa: BLE001
            log.warning("could not list %s/%s: %s", src.github_repo, path, exc)

    csvs = [e for e in entries if e["name"].lower().endswith((".csv", ".csv.gz"))]
    if not csvs:
        log.error(
            "No CSVs found under %s. Check the repo layout at https://github.com/%s",
            src.github_paths,
            src.github_repo,
        )

    downloaded = []
    for e in csvs:
        dest = out_dir / e["name"]
        download_file(e["download_url"], dest, expected_size=e.get("size"))
        downloaded.append({"name": e["name"], "path": e["path"], "size": e.get("size")})

    write_manifest(
        out_dir / "MANIFEST.json",
        {
            "source": src.name,
            "license": src.license,
            "repo": src.github_repo,
            "ref": src.github_ref,
            "files": downloaded,
        },
    )
    log.info("CLOVER done: %d CSV(s) in %s", len(downloaded), out_dir)


if __name__ == "__main__":
    main()
