"""Uniform logging for scripts."""

from __future__ import annotations

import logging
import os


def setup_logging(level: str | int | None = None) -> None:
    """Configure root logging once, honoring ``$ZOONOTIC_LOGLEVEL``."""
    if level is None:
        level = os.environ.get("ZOONOTIC_LOGLEVEL", "INFO")
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-7s %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
