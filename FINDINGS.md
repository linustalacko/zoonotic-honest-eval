# FINDINGS — does genome-based zoonotic-potential signal generalize?

> **Status: initial run complete (composition).** Data layer + honest-eval
> harness built; control rungs + composition models trained across all splits on
> ~9,197 genomes (99.7% cohort coverage, missingness unbiased w.r.t. label). ESM-2
> rung still pending (GPU step). The verdict below is the v0 answer.

## The one question

Under **taxonomic** and **temporal** holdout, does any model meaningfully beat
(a) the base-rate **prior**, (b) a **taxonomy-memorisation control**, and (c) a
**research-effort control** — or does apparent skill collapse once test viruses
are no longer close relatives of training viruses? **The headline is the gap
between the random split and the taxonomic-family holdout.**

> See [`docs/prior_work_and_fixes.md`](docs/prior_work_and_fixes.md) for the
> literature teardown — why published models (Mollentze `zoonotic_rank` combined
> AUC ≈ 0.773, *not* family-stratified; the 2025 "Hidden challenges" critique
> showing even LLMs miss SARS-CoV-2-related and H5 lineages) don't generalise,
> and how each failure mode maps to a fix here.

## Data & labels (built)

- **Source:** VIRION (Zenodo concept record `15643003`, resolved to the latest
  version at download time), cross-checked against CLOVER.
- **Unit of analysis:** one VIRION-resolved virus taxon (`VirusTaxHashID`).
- **Label:** positive = ≥1 documented *Homo sapiens* association; negative =
  has host associations but none human.
- **Counts:** 10,804 viruses total, **1,124 positive (10.4% base rate)**.
- **Modelable cohort** (family + release-year known + fetchable genome):
  **9,227 viruses, 1,080 positive (11.7%)**, across **102 families / 597 genera**.

### Known label biases (do not ignore)

1. **Absence of evidence ≠ evidence of absence.** A "negative" may be merely
   understudied. This is the dominant label-noise source.
2. **Easy negatives.** Plant/insect viruses with no plausible human route are
   trivial negatives that inflate AUC. We record `has_mammal_host` /
   `has_vertebrate_host`; a fair-comparison ablation should restrict negatives to
   mammal- or vertebrate-associated viruses (base rate among mammal-associated
   viruses is **14.3%**, vs 10.4% overall).
3. **CLOVER agreement on positives is ~30%** — not a contradiction but a coverage
   gap: CLOVER is the older, smaller mammal-focused reconciliation; VIRION
   subsumes far more GenBank-derived associations.
4. **Research-effort bias.** Positives track *study intensity* — well-sampled
   viruses look more zoonotic because they've been looked at more (the
   Orthomyxoviridae literature is 97% influenza A/B). We add an **`effort_only`
   control rung** (predict from cite counts / #associations / #sequences alone):
   a genome model that can't beat it under holdout is measuring attention, not
   biology. See [`docs/prior_work_and_fixes.md`](docs/prior_work_and_fixes.md) §F2.

## Split design (built; leakage-checked)

All schemes run on the **same cohort** so cross-split numbers are comparable.

| Scheme | Construction | Honest? | Notes |
|---|---|---|---|
| `random` | stratified 5-fold | ❌ leaky | the optimistic number |
| `tax_family` | stratified-group 5-fold, **whole families held out** | ✅ | the headline test |
| `tax_genus` | stratified-group 5-fold, **whole genera held out** | ✅ (stricter) | genus resolved for 6,118 viruses only |
| `temporal` | train `release_year < 2020`, test `≥ 2020` | ✅ (prospective) | see caveat |

- **Leakage check passes:** no family/genus appears in more than one fold.
- **Positives per fold:** random folds are even (216 each); family folds are
  lumpy (167–395) because positives cluster in ~53 of 102 families — this
  lumpiness is exactly what makes the family split hard and honest.
- **Temporal caveat:** the "year" is the earliest GenBank *sequence-release*
  year (deposition), not virus discovery — a proxy, so read temporal results as
  indicative, not definitive.

## Results (composition; ESM pending)

Cells below: **ROC-AUC** / **PR-AUC** / **top-50 watchlist lift** (× over base rate).
Best per column in **bold**. The `tax_family` column is the honest test.

| rung | random (leaky) | **tax_family (honest)** | tax_genus | temporal |
|---|---|---|---|---|
| `prior` | 0.50 / 0.12 / 1.2× | 0.42 / 0.10 / 0.7× | 0.49 / 0.15 / 0.8× | 0.50 / 0.05 / 0.8× |
| `family_prior` (taxonomy) | 0.78 / 0.38 / 5.8× | 0.42 / 0.10 / 0.7× | 0.64 / 0.29 / 0.9× | 0.82 / 0.30 / 8.2× |
| `effort_only` (research effort) | 0.71 / 0.28 / 5.1× | 0.52 / **0.22** / **5.1×** | 0.59 / 0.27 / 3.7× | 0.14 / 0.06 / 3.0× |
| `composition_logreg` | 0.74 / 0.30 / 5.3× | 0.54 / 0.12 / 0.0× | 0.64 / 0.24 / 1.9× | 0.75 / 0.19 / 2.2× |
| `composition_xgb` | **0.91 / 0.73 / 8.4×** | **0.66** / 0.18 / 1.7× | **0.75 / 0.47 / 6.1×** | **0.89 / 0.68 / 18.6×** |

### The gap (random → tax_family) — the number this repo exists to produce

`composition_xgb` drops from **0.91 → 0.66 ROC-AUC**, **0.73 → 0.18 PR-AUC**, and
**8.4× → 1.7× watchlist lift** when whole families are held out. **Most of the
apparent skill was phylogenetic leakage.** A 0.91-AUC genome model that looks
state-of-the-art on a random split is a 0.66 on genuinely novel families — and
its top-50 watchlist (1.7×) is *worse than a research-effort baseline's* (5.1×).

### Does it clear the double bar (beat BOTH controls under family holdout)?

- **vs `family_prior` (taxonomy): YES.** 0.66 vs 0.42 ROC; the genome adds real
  signal beyond pure taxonomy memorisation.
- **vs `effort_only` (research effort): NO, on the metric that matters.** Effort
  wins the watchlist (PR-AUC 0.22 vs 0.18; lift 5.1× vs 1.7×). The genome wins only
  on broad ranking (ROC 0.66 vs 0.52). For a "top-50 to investigate" list under
  genuine family-novelty, *counting how much a virus has been studied beats reading
  its genome.* And that effort win is itself the confound (well-studied → known
  human pathogen), so the honest read is: **under true family novelty, nothing
  produces a watchlist far above the biases.**

### The important nuance — *what* generalises

The collapse is specific to **novel families**. The genome model generalises well:
- **across genera within known families** (`tax_genus`: 6.1× lift, beats effort's 3.7×), and
- **forward in time within known families** (`temporal`: 18.6× lift, ROC 0.89 —
  crushing `effort_only`, which *inverts* to ROC 0.14 because recent human
  spillovers are freshly-discovered and under-studied).

So composition has learned real **family-level host-range signatures** that transfer
across genera and into the future — but it does **not** extrapolate to families it
has never seen. This is exactly the Mollentze-era result (combined AUC ~0.77, never
family-stratified) and the 2025 "Hidden challenges" critique, reproduced on our own
data with proper controls.

## Verdict (v0, composition)

**The signal is real but narrow, and the headline numbers in this literature are
mostly leakage.** Genome composition is a genuinely useful **prioritisation prior
for novel viruses within or near known families** (strong genus-holdout and
prospective performance). It is **not** a generaliser to novel families, and under
that honest test it does not beat a dumb research-effort baseline on the watchlist
metric that a real surveillance team would use. Any deployment must (a) report the
family-holdout number, not the random one, and (b) be paired with the
research-effort control, or it will overstate its reach.

**Open question for the next run:** do ESM-2 protein embeddings shrink the
family-holdout gap? The literature (incl. the BERT-infect LLM) suggests not much —
foundation models inherited the same collapse — but it's the one untested rung.
