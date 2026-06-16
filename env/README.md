# Environment notes

Python **3.11** (pinned). 3.13+ currently breaks parts of the ML stack and the
ESM-2 deps; 3.11 is the tested target.

```bash
uv venv --python 3.11
uv pip install -e .                 # base data + eval layer (CPU-only, light)
uv pip install -e ".[embeddings]"   # Phase 2: torch + fair-esm (MPS on Apple Silicon)
uv pip install -e ".[dev]"          # ruff + pytest
```

## R baseline (out of scope for v0)

The literal `zoonotic_rank` reproduction needs **R** (tidyverse, xgboost/ranger),
**NCBI BLAST+** on `PATH`, and **git-lfs** for the pretrained model. We skip it
for v0 and use a Python composition-feature GBM as "the baseline" instead. To add
it later: `brew install r blast git-lfs`, then clone
https://github.com/Nardus/zoonotic_rank into `baseline_zoonotic_rank/`.

## NCBI / Entrez

Genome downloads use Entrez. Set `NCBI_EMAIL` in `.env` (required) and optionally
`NCBI_API_KEY` (raises the rate limit 3→10 req/s). Without a key the full cohort
genome pull takes a couple of hours; it is cached and fully resumable.
