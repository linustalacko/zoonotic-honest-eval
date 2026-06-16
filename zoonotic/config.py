"""Central configuration: paths, seeds, and the version-pinned source registry.

Everything that another module might need to agree on (where data lives, what
seed to use, where a dataset comes from) is defined here exactly once.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # read .env if present (NCBI_EMAIL, NCBI_API_KEY)

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
REPO_ROOT = Path(__file__).resolve().parent.parent

# Data + results roots are env-overridable so the *same* code runs locally or on
# a Modal Volume. On Modal we set ZOONOTIC_DATA_DIR=/data (the mounted Volume) and
# nothing else touches the laptop. Locally they default under the repo.
DATA_DIR = Path(os.environ.get("ZOONOTIC_DATA_DIR", REPO_ROOT / "data"))
RAW_DIR = DATA_DIR / "raw"  # cached downloads
PROCESSED_DIR = DATA_DIR / "processed"  # derived tables (labels, splits)
CACHE_DIR = DATA_DIR / "cache"  # per-record scratch
GENOME_DIR = RAW_DIR / "genomes"  # downloaded FASTA

FEATURES_CACHE = Path(os.environ.get("ZOONOTIC_FEATURES_DIR", DATA_DIR / "features_cache"))
MODELS_ARTIFACTS = DATA_DIR / "models_artifacts"
RESULTS_DIR = Path(os.environ.get("ZOONOTIC_RESULTS_DIR", REPO_ROOT / "results"))

EXPERIMENTS_DB = RESULTS_DIR / "experiments.sqlite"


def ensure_dirs() -> None:
    """Create all gitignored working directories. Idempotent."""
    for d in (
        RAW_DIR,
        PROCESSED_DIR,
        CACHE_DIR,
        GENOME_DIR,
        FEATURES_CACHE,
        RESULTS_DIR,
        MODELS_ARTIFACTS,
    ):
        d.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------- #
# Determinism
# --------------------------------------------------------------------------- #
RANDOM_SEED = 42

# --------------------------------------------------------------------------- #
# Label definition (documented; biases discussed in FINDINGS.md)
# --------------------------------------------------------------------------- #
HUMAN_HOST_NAMES = (
    "homo sapiens",
    "homo_sapiens",
    "human",
)
# Taxonomic rank at which a "virus" is one labeled unit. Species is the ICTV
# unit and the granularity at which RefSeq reference genomes are curated.
VIRUS_UNIT_RANK = "species"

# --------------------------------------------------------------------------- #
# NCBI / Entrez
# --------------------------------------------------------------------------- #
NCBI_EMAIL = os.environ.get("NCBI_EMAIL", "")
NCBI_API_KEY = os.environ.get("NCBI_API_KEY", "")
# Entrez allows 3 req/s without a key, 10 req/s with one.
ENTREZ_RATE_LIMIT = 10.0 if NCBI_API_KEY else 3.0


# --------------------------------------------------------------------------- #
# Source registry (version-pinned where the source supports it)
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Source:
    """One external data source.

    Resolution strategy is intentionally layered: prefer a Zenodo concept
    record (immutable, citable) when available, fall back to a GitHub ref. The
    download scripts in ``data/`` know how to resolve each ``kind``.
    """

    name: str
    kind: str  # "zenodo" | "github_dir" | "url" | "ictv_vmr" | "ncbi"
    license: str
    # kind-specific resolution hints:
    zenodo_record: str | None = None  # numeric record id (concept or version)
    github_repo: str | None = None  # "owner/repo"
    github_ref: str | None = None  # tag/branch/commit — pin to a commit when stable
    github_paths: tuple[str, ...] = ()  # files/dirs of interest within the repo
    url: str | None = None  # direct download (kind="url")
    notes: str = ""
    extra: dict = field(default_factory=dict)


SOURCES: dict[str, Source] = {
    "virion": Source(
        name="VIRION",
        kind="zenodo",
        license="ODbL-1.0",
        zenodo_record="15643003",  # concept DOI 10.5281/zenodo.15643003
        github_repo="viralemergence/virion",
        github_ref="main",
        notes="Host-virus association network. Primary 'infects humans' label source.",
    ),
    "clover": Source(
        name="CLOVER",
        kind="github_dir",
        license="ODbL-1.0",
        github_repo="viralemergence/clover",
        github_ref="main",
        github_paths=("clover/clover_1.0_allpathogens",),
        notes="Reconciled HP3+GMPD2+EID2+Shaw host-virus associations. Label cross-check.",
    ),
    "hp3": Source(
        name="HP3",
        kind="github_dir",
        license="MIT",
        github_repo="ecohealthalliance/HP3",
        github_ref="master",
        github_paths=("data",),
        notes="Olival 2017 mammal host-virus + traits. Trait feature source.",
    ),
    "ictv_vmr": Source(
        name="ICTV VMR",
        kind="ictv_vmr",
        license="CC BY 4.0",
        url="https://ictv.global/vmr",  # landing page; resolver scrapes the .xlsx link
        notes="Authoritative virus taxonomy. Drives taxonomy-aware splitting.",
    ),
    "ncbi_genomes": Source(
        name="NCBI Virus",
        kind="ncbi",
        license="public-domain",
        notes="Genome sequences pulled per-species via Entrez (RefSeq-preferred).",
    ),
}
