"""Flat, append-only experiment log (sqlite).

Every training/eval run records its params and metrics here so results are
reproducible and comparable across splits. Intentionally schema-light: params
and metrics are stored as JSON blobs so new experiment shapes never require a
migration.
"""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path

from zoonotic.config import EXPERIMENTS_DB, ensure_dirs

_SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    run_id     TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    tag        TEXT,            -- short human label, e.g. "composition+gbm"
    split      TEXT,            -- "random" | "taxonomic_genus" | "temporal" | ...
    features   TEXT,            -- "composition" | "esm2" | "composition+meta" | ...
    model      TEXT,            -- "logreg" | "xgboost" | ...
    seed       INTEGER,
    params     TEXT NOT NULL,   -- JSON
    metrics    TEXT NOT NULL,   -- JSON
    notes      TEXT
);
"""


@contextmanager
def _connect():
    ensure_dirs()
    conn = sqlite3.connect(EXPERIMENTS_DB)
    try:
        conn.execute(_SCHEMA)
        yield conn
        conn.commit()
    finally:
        conn.close()


def log_run(
    *,
    run_id: str,
    tag: str,
    split: str,
    features: str,
    model: str,
    seed: int,
    params: dict,
    metrics: dict,
    notes: str = "",
) -> None:
    """Append one experiment record. ``run_id`` should be unique per run."""
    with _connect() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO runs VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                run_id,
                datetime.now(UTC).isoformat(),
                tag,
                split,
                features,
                model,
                seed,
                json.dumps(params, default=str),
                json.dumps(metrics, default=str),
                notes,
            ),
        )


def load_runs(db: Path | None = None):
    """Return all runs as a DataFrame (metrics/params left as JSON strings)."""
    import pandas as pd

    db = db or EXPERIMENTS_DB
    if not Path(db).exists():
        return pd.DataFrame()
    with sqlite3.connect(db) as conn:
        return pd.read_sql_query("SELECT * FROM runs ORDER BY created_at", conn)
