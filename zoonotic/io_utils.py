"""Download + caching helpers shared by every ``data/download_*.py`` script.

Design goals:
  * **Idempotent**: a completed download is never re-fetched (size-validated).
  * **Cached**: everything lands under ``data/raw`` and is safe to re-run.
  * **Resolvable**: Zenodo concept records and GitHub directories are resolved
    via their APIs at download time, so we pin to a *source*, not a brittle
    direct URL.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path

import requests

log = logging.getLogger("zoonotic.io")

_SESSION = requests.Session()
_SESSION.headers.update({"User-Agent": "zoonotic-v0 (research; contact via repo)"})

DEFAULT_TIMEOUT = 60
DEFAULT_RETRIES = 4


def _request(method: str, url: str, **kw) -> requests.Response:
    """HTTP with bounded exponential-backoff retries on transient failures."""
    kw.setdefault("timeout", DEFAULT_TIMEOUT)
    last_exc: Exception | None = None
    for attempt in range(DEFAULT_RETRIES):
        try:
            resp = _SESSION.request(method, url, **kw)
            if resp.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(f"{resp.status_code} for {url}")
            resp.raise_for_status()
            return resp
        except (requests.RequestException, requests.HTTPError) as exc:
            last_exc = exc
            wait = 2**attempt
            log.warning("request failed (%s), retry in %ss: %s", attempt + 1, wait, exc)
            time.sleep(wait)
    raise RuntimeError(f"request failed after {DEFAULT_RETRIES} attempts: {url}") from last_exc


def get_json(url: str, **kw) -> dict:
    return _request("GET", url, **kw).json()


def download_file(
    url: str,
    dest: Path,
    *,
    expected_size: int | None = None,
    force: bool = False,
) -> Path:
    """Stream ``url`` to ``dest`` with caching.

    Skips the download if ``dest`` already exists and (when known) matches
    ``expected_size``. Writes to a ``.part`` file and atomically renames on
    success so an interrupted download never looks complete.
    """
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and not force and dest.stat().st_size > 0:
        # Re-download only if we have a *reliable* expected size and the cached
        # file is smaller than it (i.e. a partial download). We never treat
        # "larger than expected" as an error: source-reported sizes (e.g. the
        # GitHub blob size) can legitimately differ from the decoded transfer.
        if expected_size is None or dest.stat().st_size >= expected_size:
            log.info("cached: %s", dest.name)
            return dest
        log.warning("cached %s smaller than expected (%s < %s); re-downloading",
                    dest.name, dest.stat().st_size, expected_size)

    tmp = dest.with_suffix(dest.suffix + ".part")
    with _request("GET", url, stream=True) as resp:
        # Truncation is only detectable against the server's own Content-Length —
        # and only when the body is *not* content-encoded. With gzip/br on the
        # wire, Content-Length is the compressed size while iter_content yields
        # decompressed bytes, so the two are not comparable.
        enc = resp.headers.get("Content-Encoding", "").lower().strip()
        cl = resp.headers.get("Content-Length")
        total = int(cl) if (cl is not None and enc in ("", "identity")) else None
        written = 0
        with open(tmp, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
                written += len(chunk)
        if total is not None and written != total:
            tmp.unlink(missing_ok=True)
            raise RuntimeError(f"truncated download for {url}: {written}/{total} bytes")
    tmp.replace(dest)
    log.info("downloaded: %s (%.1f MB)", dest.name, dest.stat().st_size / 1e6)
    return dest


def write_manifest(dest: Path, payload: dict) -> None:
    """Record what was downloaded (urls, sizes, resolved version) for provenance."""
    dest.write_text(json.dumps(payload, indent=2, default=str))
    log.info("wrote manifest: %s", dest.name)


# --------------------------------------------------------------------------- #
# Zenodo
# --------------------------------------------------------------------------- #
def zenodo_files(record_id: str) -> tuple[dict, list[dict]]:
    """Resolve a Zenodo record to (record_json, files).

    A *concept* record id resolves to the latest version. Each file dict has
    ``key`` (filename), ``size``, and a download ``links.self``.
    """
    rec = get_json(f"https://zenodo.org/api/records/{record_id}")
    # Concept records expose the latest version under links.latest.
    latest = rec.get("links", {}).get("latest")
    if latest and latest.rstrip("/").split("/")[-1] != str(rec.get("id")):
        rec = get_json(latest)
    files = rec.get("files", [])
    return rec, files


# --------------------------------------------------------------------------- #
# GitHub
# --------------------------------------------------------------------------- #
def github_list_dir(repo: str, path: str, ref: str = "main") -> list[dict]:
    """List a directory in a GitHub repo via the contents API.

    Returns entries with ``name``, ``type`` ('file'|'dir'), ``size``, and
    ``download_url``. Recurses into subdirectories.
    """
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
    entries = get_json(url)
    if isinstance(entries, dict):  # a single file was requested
        entries = [entries]
    out: list[dict] = []
    for e in entries:
        if e["type"] == "dir":
            out.extend(github_list_dir(repo, e["path"], ref))
        else:
            out.append(e)
    return out


def github_raw_url(repo: str, path: str, ref: str = "main") -> str:
    return f"https://raw.githubusercontent.com/{repo}/{ref}/{path}"
