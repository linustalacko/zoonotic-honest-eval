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

# GPU image for the ESM-2 protein-embedding rung. torch + fair-esm; weights cached
# to the Volume (TORCH_HOME) so retries don't re-download.
gpu_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(*DEPS, "torch>=2.2", "fair-esm>=2.0")
    .env({
        "ZOONOTIC_DATA_DIR": DATA_MOUNT,
        "ZOONOTIC_RESULTS_DIR": f"{DATA_MOUNT}/results",
        "TORCH_HOME": f"{DATA_MOUNT}/torch_cache",
    })
    .add_local_python_source("zoonotic", "features", "models", "data")
)


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
def train(rung: str = "all", cohort: str = "genome") -> dict:
    """Run ladder rung(s) across all splits on ONE shared cohort; persist preds +
    metrics + family-clustered-bootstrap CIs (computed in-container, so no
    volume-read lag).

    rung   in {all, controls, genomes, esm, <single-rung>} (all = controls+genome)
    cohort in {genome (with-genome set, consistent n), mammal (fair cohort)}
    """
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    from features.composition import featurize_viruses
    from models.dataset import load_labels
    from models.evaluate import compare_rungs, gap_ci
    from models.train import CONTROL_RUNGS, ESM_RUNGS, GENOME_RUNGS, run_rung

    labels = load_labels()
    genome_idx = set(featurize_viruses(labels).index)  # also warms composition.parquet
    groups = {"controls": CONTROL_RUNGS, "genomes": GENOME_RUNGS, "esm": ESM_RUNGS,
              "all": CONTROL_RUNGS + GENOME_RUNGS}
    rungs = groups.get(rung, (rung,))

    if cohort == "mammal":
        mam = set(labels.loc[labels["has_mammal_host"], "virus_taxhash"])
        restrict, suffix = genome_idx & mam, "__mammal"
    else:
        restrict, suffix = genome_idx, ""

    metrics = {}
    for r in rungs:
        table = run_rung(r, restrict_to=restrict, tag=f"{r}{suffix}")
        metrics[f"{r}{suffix}"] = table.to_dict("records")

    # headline confidence intervals, computed from the preds just written
    xgb, eff = f"composition_xgb{suffix}", f"effort_only{suffix}"
    analysis = {
        "gap_composition_xgb": gap_ci(xgb),
        "xgb_vs_effort_tax_family": compare_rungs(xgb, eff, "tax_family"),
        "xgb_vs_effort_tax_genus": compare_rungs(xgb, eff, "tax_genus"),
        "xgb_vs_family_prior_tax_family": compare_rungs(xgb, f"family_prior{suffix}", "tax_family"),
    }
    volume.commit()
    return {"cohort": cohort, "n_restrict": len(restrict),
            "rungs": list(metrics.keys()), "metrics": metrics, "analysis": analysis}


@app.function(timeout=4 * 3600, gpu="a10g", image=gpu_image, volumes={DATA_MOUNT: volume})
def train_esm(model_name: str = "esm2_t30_150M_UR50D") -> dict:
    """Embed ORFs with ESM-2 (GPU), run the ESM rungs on the shared cohort, and
    compute paired CIs vs composition + effort. The one untested rung: does a
    protein language model shrink the family-holdout gap?"""
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    from features.composition import featurize_viruses as comp_feat
    from features.embeddings import featurize_viruses as esm_feat
    from models.dataset import load_labels
    from models.evaluate import compare_rungs, gap_ci
    from models.train import run_rung

    labels = load_labels()
    comp_idx = set(comp_feat(labels).index)              # warms composition cache
    esm = esm_feat(labels, model_name=model_name)        # GPU embed + cache to Volume
    restrict = comp_idx & set(esm.index)

    metrics = {}
    for r in ("esm_logreg", "esm_xgb"):
        metrics[r] = run_rung(r, restrict_to=restrict, tag=r).to_dict("records")

    analysis = {
        "gap_esm_xgb": gap_ci("esm_xgb"),
        "esm_xgb_vs_composition_xgb_family": compare_rungs("esm_xgb", "composition_xgb", "tax_family"),
        "esm_xgb_vs_effort_only_family": compare_rungs("esm_xgb", "effort_only", "tax_family"),
        "esm_xgb_vs_composition_xgb_genus": compare_rungs("esm_xgb", "composition_xgb", "tax_genus"),
    }
    volume.commit()
    return {"model": model_name, "n_esm": int(len(esm)), "dim": int(esm.shape[1]),
            "n_restrict": len(restrict), "metrics": metrics, "analysis": analysis}


@app.function(timeout=2 * 3600, **CPU_KW)
def hillclimb(specs: list) -> list:
    """Evaluate a batch of (features, model, params) specs on the shared cohort;
    return the leaderboard. Features are loaded once and reused across the batch."""
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    from features.composition import featurize_viruses
    from models.dataset import load_labels
    from models.hillclimb import run_specs

    genome_idx = set(featurize_viruses(load_labels()).index)
    return run_specs(specs, restrict=genome_idx)


@app.function(timeout=2 * 3600, **CPU_KW)
def diagnostics(rung: str = "composition_xgb") -> dict:
    """Leakage curve + hard-lineage probe + watchlist, from persisted OOF preds."""
    from zoonotic.logging_utils import setup_logging

    setup_logging()
    from features.composition import featurize_viruses
    from models import diagnostics as dg
    from models.dataset import build_dataset, load_labels
    from models.evaluate import load_preds

    labels = load_labels()
    feats = featurize_viruses(labels)
    ds = build_dataset(feats, restrict_to=set(feats.index))
    preds = {s: load_preds(rung, s) for s in ("random", "tax_family")}

    out: dict = {"leakage_curve": dg.leakage_curve(ds, preds)}
    pf = load_preds(rung, "tax_family")
    if pf is not None:
        out["watchlist_family_holdout"] = dg.watchlist(pf, labels, 50)
        out["hard_lineage_family_holdout"] = dg.hard_lineage_probe(pf, labels, {
            "sars_related": "respiratory syndrome.related coronavirus|sarbecovirus|sars",
            "mers": "middle east respiratory|merbecovirus",
            "influenza_a": "influenza a", "ebola": "ebola", "nipah": "nipah",
            "lyssavirus_rabies": "lyssavirus|rabies"})
    pr = load_preds(rung, "random")
    if pr is not None:
        out["watchlist_random"] = dg.watchlist(pr, labels, 50)
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
