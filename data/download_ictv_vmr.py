#!/usr/bin/env python
"""Download the ICTV Virus Metadata Resource (VMR) — authoritative taxonomy.

The VMR is an .xlsx whose filename changes every release
(``VMR_MSL41.v1.20260320.xlsx`` …). We scrape the VMR landing page for all VMR
spreadsheet links and pick the newest by Master-Species-List (MSL) number, so
the script keeps working across releases without edits.

Why we need it: taxonomy-aware splitting (holding out whole genera/families) is
the honest-evaluation core, and ICTV is the authoritative grouping.
"""

from __future__ import annotations

import logging
import re

from zoonotic.config import RAW_DIR, SOURCES, ensure_dirs
from zoonotic.io_utils import _request, download_file, write_manifest
from zoonotic.logging_utils import setup_logging

log = logging.getLogger("zoonotic.download.ictv")

VMR_PAGE = "https://ictv.global/vmr"
BASE = "https://ictv.global"
# Capture MSL number + version so we can sort to the newest release.
LINK_RE = re.compile(r'href="(/[^"]*VMR_MSL(\d+)[._]v?(\d+)[^"]*\.xlsx)"', re.I)


def resolve_latest_vmr() -> tuple[str, int, int]:
    """Return (absolute_url, msl, version) for the newest VMR spreadsheet."""
    html = _request("GET", VMR_PAGE).text
    matches = LINK_RE.findall(html)
    if not matches:
        raise RuntimeError(f"No VMR .xlsx links found on {VMR_PAGE}; page layout changed.")
    # sort by (MSL number, version) descending
    matches.sort(key=lambda m: (int(m[1]), int(m[2])), reverse=True)
    href, msl, ver = matches[0]
    return BASE + href, int(msl), int(ver)


def main() -> None:
    setup_logging()
    ensure_dirs()
    src = SOURCES["ictv_vmr"]
    out_dir = RAW_DIR / "ictv"
    out_dir.mkdir(parents=True, exist_ok=True)

    url, msl, ver = resolve_latest_vmr()
    fname = url.rsplit("/", 1)[-1]
    log.info("latest VMR: MSL%d v%d -> %s", msl, ver, fname)
    dest = out_dir / fname
    download_file(url, dest)

    # stable symlink/copy name so downstream code doesn't hardcode the release
    stable = out_dir / "VMR_latest.xlsx"
    stable.unlink(missing_ok=True)
    stable.write_bytes(dest.read_bytes())

    write_manifest(
        out_dir / "MANIFEST.json",
        {
            "source": src.name,
            "license": src.license,
            "url": url,
            "msl": msl,
            "version": ver,
            "file": fname,
            "stable_alias": "VMR_latest.xlsx",
        },
    )
    log.info("ICTV VMR done: %s (-> VMR_latest.xlsx)", fname)


if __name__ == "__main__":
    main()
