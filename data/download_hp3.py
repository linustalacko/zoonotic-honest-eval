#!/usr/bin/env python
"""Download HP3 (Olival 2017) — mammal host-virus associations + traits.

Provides optional trait features (host taxonomy, virus genome type, etc.) for the
metadata-fusion ablation. Resolved via the GitHub contents API.
"""

from __future__ import annotations

import logging

from zoonotic.config import RAW_DIR, SOURCES, ensure_dirs
from zoonotic.io_utils import download_file, github_list_dir, write_manifest
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.download.hp3")

WANTED = (".csv", ".csv.gz", ".tsv")


def main() -> None:
    setup_logging()
    ensure_dirs()
    src = SOURCES["hp3"]
    out_dir = RAW_DIR / "hp3"
    out_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict] = []
    for path in src.github_paths:
        try:
            entries.extend(github_list_dir(src.github_repo, path, src.github_ref))
        except Exception as exc:  # noqa: BLE001
            log.warning("could not list %s/%s: %s", src.github_repo, path, exc)

    wanted = [e for e in entries if e["name"].lower().endswith(WANTED)]
    downloaded = []
    for e in wanted:
        # preserve subdirectory structure under data/
        rel = e["path"]
        dest = out_dir / rel.split("/", 1)[-1] if "/" in rel else out_dir / e["name"]
        download_file(e["download_url"], dest, expected_size=e.get("size"))
        downloaded.append({"name": e["name"], "path": rel, "size": e.get("size")})

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
    log.info("HP3 done: %d file(s) in %s", len(downloaded), out_dir)


if __name__ == "__main__":
    main()
