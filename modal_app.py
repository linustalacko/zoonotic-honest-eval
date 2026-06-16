"""Run the whole zoonotic data + feature pipeline on Modal — nothing on the laptop.

Everything persists to a Modal Volume (``zoonotic-data``) mounted at ``/data``.
The same code that runs locally runs here unchanged: ``zoonotic.config`` reads
``ZOONOTIC_DATA_DIR`` / ``ZOONOTIC_RESULTS_DIR`` (set on the image) so all paths
point at the Volume instead of the repo.

Typical use (from the repo root, where the package dirs live):

    modal run modal_app.py::prep                 # downloads + labels + splits
    modal run modal_app.py --stage genomes       # sharded genome download
    modal run modal_app.py::coverage             # how many genomes landed
    modal run modal_app.py                        # full pipeline (prep -> genomes)

Pull the small derived tables back when you want them locally:

    modal volume get zoonotic-data /processed/labels.parquet ./data/processed/
    modal volume get zoonotic-data /results ./results
"""

from __future__ import annotations

import modal

APP_NAME = "zoonotic"
DATA_MOUNT = "/data"
# NCBI creds (email + API key) live in a Modal Secret, not baked into the image.
# Create/update with:
#   modal secret create ncbi NCBI_EMAIL=you@example.com NCBI_API_KEY=... --force
# The key raises Entrez 3 -> 10 req/s, so one polite worker pulls all genomes in
# ~30-40 min with no throttling.
NCBI_SECRET = modal.Secret.from_name("ncbi")

DEPS = [
    "numpy>=1.26", "pandas>=2.1", "pyarrow>=15.0", "scikit-learn>=1.4",
    "xgboost>=2.0", "biopython>=1.83", "requests>=2.31", "openpyxl>=3.1",
    "python-dotenv>=1.0", "tqdm>=4.66", "pyyaml>=6.0",
]

app = modal.App(APP_NAME)
volume = modal.Volume.from_name("zoonotic-data", create_if_missing=True)

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(*DEPS)
    .env({
        "ZOONOTIC_DATA_DIR": DATA_MOUNT,
        "ZOONOTIC_RESULTS_DIR": f"{DATA_MOUNT}/results",
    })
    # Mount our local packages at runtime (fast: no rebuild on code edits).
    .add_local_python_source("zoonotic", "features", "models", "data")
)

CPU_KW = dict(image=image, volumes={DATA_MOUNT: volume})


@app.function(timeout=1800, **CPU_KW)
def prep() -> dict:
    """Download tabular sources, then build labels + splits onto the Volume."""
    from data import (
        build_labels, build_splits, download_clover, download_hp3,
        download_ictv_vmr, download_virion,
    )

    download_virion.main()
    download_clover.main()
    download_hp3.main()
    download_ictv_vmr.main()
    build_labels.main()
    build_splits.main()
    volume.commit()

    import pandas as pd

    from zoonotic.config import PROCESSED_DIR
    labels = pd.read_parquet(PROCESSED_DIR / "labels.parquet")
    splits = pd.read_parquet(PROCESSED_DIR / "splits.parquet")
    return {"viruses": len(labels), "positives": int(labels.label.sum()),
            "cohort": len(splits)}


@app.function(timeout=3 * 3600, retries=3, secrets=[NCBI_SECRET], **CPU_KW)
def genomes_shard(shard_index: int, num_shards: int) -> dict:
    """Fetch one strided shard of genomes, checkpointing to the Volume."""
    from data.download_genomes import run
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    return run(
        shard_index=shard_index, num_shards=num_shards,
        commit_every=200, commit_cb=volume.commit,
    )


@app.function(timeout=2 * 3600, **CPU_KW)
def featurize_composition() -> dict:
    """Build composition features for every virus with a genome on the Volume."""
    from features.composition import featurize_viruses
    from models.dataset import load_labels
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    feats = featurize_viruses(load_labels(), force=True)
    volume.commit()
    return {"viruses_featurized": int(len(feats)), "dims": int(feats.shape[1])}


@app.function(timeout=2 * 3600, **CPU_KW)
def train(rung: str = "controls") -> dict:
    """Run ladder rung(s) across all splits on the Volume; write metrics_*.csv.

    rung in {controls, genomes, all, <single-rung-name>}. 'controls' needs no
    genomes; genome rungs require featurize_composition to have run first.
    """
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    from models.train import CONTROL_RUNGS, ESM_RUNGS, GENOME_RUNGS, run_rung

    rungs = {"controls": CONTROL_RUNGS, "genomes": GENOME_RUNGS,
             "esm": ESM_RUNGS}.get(rung, (rung,))
    out = {}
    for r in rungs:
        table = run_rung(r)
        out[r] = table.to_dict("records")
    volume.commit()
    return out


@app.function(timeout=600, **CPU_KW)
def coverage() -> dict:
    """Report genome coverage currently on the Volume."""
    from zoonotic.config import GENOME_DIR
    volume.reload()
    fasta = list(GENOME_DIR.glob("*.fasta"))
    empty = list(GENOME_DIR.glob("*.empty"))
    return {"genomes": len(fasta), "misses": len(empty),
            "total_attempted": len(fasta) + len(empty)}


@app.function(timeout=600, **CPU_KW)
def coverage_bias() -> dict:
    """Is genome-missingness random, or correlated with label/family?"""
    import pandas as pd

    from zoonotic.config import PROCESSED_DIR
    from zoonotic.ncbi import genome_path
    volume.reload()
    labels = pd.read_parquet(PROCESSED_DIR / "labels.parquet").set_index("virus_taxhash")
    splits = pd.read_parquet(PROCESSED_DIR / "splits.parquet")
    coh = labels.loc[labels.index.intersection(splits["virus_taxhash"])].copy()
    coh["has_genome"] = [
        isinstance(n, str) and genome_path(n).exists() and genome_path(n).stat().st_size > 0
        for n in coh["virus_name"]
    ]
    fam = coh.groupby("family")["has_genome"].agg(["mean", "size"])
    fam = fam[fam["size"] >= 20].sort_values("mean").head(8)
    return {
        "cohort": int(len(coh)),
        "with_genome": int(coh["has_genome"].sum()),
        "coverage": round(float(coh["has_genome"].mean()), 4),
        "pos_coverage": round(float(coh.loc[coh.label == 1, "has_genome"].mean()), 4),
        "neg_coverage": round(float(coh.loc[coh.label == 0, "has_genome"].mean()), 4),
        "n_pos": int((coh.label == 1).sum()),
        "n_neg": int((coh.label == 0).sum()),
        "worst_families": {f: {"cov": round(float(r["mean"]), 3), "n": int(r["size"])}
                           for f, r in fam.iterrows()},
    }


@app.local_entrypoint()
def main(stage: str = "all", num_shards: int = 1) -> None:
    """Drive the pipeline. stage in {all, prep, genomes, features, coverage}.

    num_shards defaults to 1: NCBI rate-limits by IP and Modal containers share
    egress, so parallel shards trip HTTP 429. A single worker (10 req/s with an
    API key) is both fast enough and polite. Only raise num_shards if you've
    confirmed distinct egress IPs.
    """
    if stage in ("all", "prep"):
        print("prep:", prep.remote())
    if stage in ("all", "genomes"):
        results = list(genomes_shard.map(range(num_shards), [num_shards] * num_shards))
        found = sum(r["found"] for r in results)
        missing = sum(r["missing"] for r in results)
        print(f"genomes: found={found} missing={missing} across {num_shards} shards")
    if stage == "features":
        print("features:", featurize_composition.remote())
    if stage in ("all", "coverage"):
        print("coverage:", coverage.remote())
