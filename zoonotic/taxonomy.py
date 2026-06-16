"""Virus-name normalization and taxonomy joins.

VIRION, CLOVER, HP3 and ICTV each spell virus names slightly differently. We
normalize to a canonical key so the same virus lines up across sources. This is
deliberately conservative — it lowercases, collapses whitespace/punctuation, and
strips common decorations, but does *not* try to be a full taxonomic resolver
(that is ICTV's job, joined on explicitly where taxonomy matters).
"""

from __future__ import annotations

import re

_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[^a-z0-9 ]+")
# Strof suffixes/prefixes that carry no taxonomic meaning for matching.
_NOISE = re.compile(r"\b(virus|viruses|strain|isolate|complete|genome|sequence)\b")


def normalize_name(name: str | None) -> str:
    """Canonical, comparison-friendly virus name key.

    'Severe acute respiratory syndrome-related coronavirus' and
    'severe_acute_respiratory_syndrome related coronavirus' map to the same key.
    """
    if not isinstance(name, str) or not name:
        return ""
    s = name.lower().replace("_", " ")
    s = _PUNCT.sub(" ", s)
    s = _WS.sub(" ", s).strip()
    return s


def normalize_for_match(name: str | None) -> str:
    """Aggressive key for fuzzy cross-source matching (drops generic words)."""
    s = normalize_name(name)
    s = _NOISE.sub(" ", s)
    return _WS.sub(" ", s).strip()


# Canonical ICTV-style rank columns we standardize on everywhere.
RANK_COLUMNS = ("realm", "kingdom", "phylum", "class", "order", "family", "genus", "species")
