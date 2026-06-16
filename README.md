# zoonotic-v0

Honest evaluation of **genome-based human-infection prediction** ("zoonotic
potential"). Given a viral genome, predict the probability that the virus can
infect humans — and, more importantly, **measure whether that signal
generalizes to genuinely novel viruses or is mostly memorizing taxonomy.**

> This is a v0 / exploratory **signal-probing and conviction-building** exercise,
> not production IP. The goal is an honest answer to one question:
> *under phylogenetic and temporal holdout, does any model meaningfully beat
> (a) random and (b) the simplest composition baseline?* See
> [`FINDINGS.md`](FINDINGS.md) — that is the deliverable that matters.

## Why this is methodologically tricky (read first)

The naive pipeline — featurize genomes, train a classifier, report a high AUC —
is a known trap. Models score well by exploiting **phylogenetic relatedness**
(test viruses are close relatives of training viruses) rather than learning
generalizable biology. A model at 0.95 AUC on a random split can be near-useless
on a novel virus family. **The entire value of this repo is the gap between the
random split and the taxonomic-holdout split.** We optimize for honest
evaluation, not for a high number.

## Pipeline

```
download_* (data/)      raw association tables + taxonomy + genomes  -> data/raw/
  -> build_labels.py    VIRION/CLOVER -> per-virus "infects humans" label
  -> build_splits.py    random / taxonomic (genus,family) / temporal splits
  -> features/          composition (k-mer, dinuc) | ESM-2 embeddings | +metadata
  -> models/            train.py (regularized linear, gradient boosting)
  -> models/evaluate.py base-rate-aware metrics across every split, side by side
  -> results/           metrics tables + plots per split
```

## Status (v0 scaffold)

| Phase | What | State |
|---|---|---|
| Data layer | idempotent, cached download scripts | ✅ scaffolded |
| Labels | VIRION/CLOVER → human-infection labels | ✅ scaffolded |
| Splits | random / taxonomic / temporal (ICTV-aware) | ✅ scaffolded |
| Eval harness | base-rate-aware metrics, precision@k, per-split | ✅ scaffolded |
| Features | composition; ESM-2 embeddings (optional) | ✅ scaffolded |
| Models | linear / gradient boosting | ✅ scaffolded (training deferred) |
| Baseline (R) | literal `zoonotic_rank` reproduction | ⏭️ out of scope for v0 (see note) |

**Note on the R baseline:** for v0 we *skip* the literal R + BLAST+ reproduction
of [`zoonotic_rank`](https://github.com/Nardus/zoonotic_rank) and instead treat a
composition-feature gradient-boosted model as "the baseline," reimplemented in
Python so it runs inside the same honest-eval harness. The published pipeline
remains the eventual ground-truth anchor.

## Setup

```bash
# Python 3.11 env (3.13+ breaks the ML stack; ESM-2 deps want <3.13)
uv venv --python 3.11
uv pip install -e .                 # base data/eval layer
uv pip install -e ".[embeddings]"   # + torch / fair-esm for Phase 2 (optional)

cp .env.example .env                # set NCBI_EMAIL (+ NCBI_API_KEY if you have one)
```

## Run the data layer

```bash
# 1. Download association tables + taxonomy (fast, cached, idempotent)
python data/download_virion.py
python data/download_clover.py
python data/download_ictv_vmr.py
python data/download_hp3.py

# 2. Build labels + splits (fast)
python data/build_labels.py
python data/build_splits.py

# 3. Download representative genomes for labeled viruses (slow, resumable)
python data/download_genomes.py
```

All downloads cache under `data/raw/` and are safe to re-run. Derived tables land
in `data/processed/`.

## Conventions

- Deterministic seeds everywhere (`zoonotic.config.RANDOM_SEED`).
- Every experiment logged (params + metrics) to `results/experiments.sqlite` via
  `zoonotic.experiment`.
- Downloads are idempotent, cached, and version-pinned (`zoonotic.config.SOURCES`).
- Scripts + thin notebooks for viz only — no notebook-only logic.

## Data sources & licensing

| Source | Use | License |
|---|---|---|
| [VIRION](https://github.com/viralemergence/virion) | primary human-infection labels | ODbL-1.0 (share-alike) |
| [CLOVER](https://github.com/viralemergence/clover) | label cross-check | ODbL-1.0 |
| [HP3](https://github.com/ecohealthalliance/HP3) | host/virus trait features | MIT |
| [ICTV VMR](https://ictv.global/vmr) | taxonomy for honest splits | CC BY 4.0 |
| [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/) | genome sequences | public domain |

VIRION/CLOVER are **ODbL share-alike**: fine for training and internal use; any
redistributed derived dataset must stay open. **No GISAID** in v0 (gated DUA).
