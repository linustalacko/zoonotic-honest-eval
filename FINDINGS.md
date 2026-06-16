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
2. **Easy negatives are *non-mammal*, not "plant/insect".** VIRION is
   vertebrate-host-focused, so only **4.1% of cohort negatives are
   non-vertebrate** — the intuition that "half the cohort is plant/insect
   viruses" is wrong (measured, not assumed). The defensible easy-negative slice
   is **non-mammal** viruses (**28.7%** of negatives). We record `has_mammal_host`;
   the fair-comparison ablation restricts the cohort to mammal-associated viruses
   (**6,890 viruses, 1,080 positive, 15.7% base rate, 82 families**). Crucially,
   this does **not** rescue the family-holdout collapse — that is phylogenetic
   leakage, not a negative-set artifact (see the fair-cohort result below).
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

All rungs run on **one shared cohort** (n = 9,201 viruses with a fetched genome),
so every number is directly comparable. Cells: **ROC-AUC** / **PR-AUC** / **top-50
watchlist lift** (× over base rate). The `tax_family` column is the honest test.

| rung | random (leaky) | **tax_family (honest)** | tax_genus | temporal |
|---|---|---|---|---|
| `prior` | 0.50 / 0.12 / 1.2× | 0.42 / 0.10 / 0.5× | 0.49 / 0.15 / — | 0.50 / 0.05 / — |
| `family_prior` (taxonomy) | 0.78 / 0.38 / 5.8× | 0.42 / 0.10 / 0.5× | 0.63 / 0.29 / 0.8× | 0.82 / 0.30 / 7.8× |
| `effort_only` (research effort) | 0.71 / 0.28 / 5.1× | 0.52 / 0.22 / 5.1× | 0.59 / 0.27 / 3.7× | 0.14 / 0.06 / 3.0× |
| `composition_logreg` | 0.74 / 0.30 / 5.3× | 0.54 / 0.12 / 0.0× | 0.64 / 0.24 / 1.9× | 0.75 / 0.19 / 2.2× |
| `composition_xgb` | **0.91 / 0.73 / 8.4×** | **0.66** / 0.18 / 1.7× | **0.75 / 0.47 / 6.1×** | **0.89 / 0.68 / 18.6×** |

All CIs below are **paired family-clustered bootstraps** (2,000 resamples of whole
families — the correct unit, since within-family viruses are correlated; the
effective n is ~100 families, not 9,201 rows). See `results/confidence_intervals.json`.

### The gap (random → tax_family) — the number this repo exists to produce

`composition_xgb` collapses when whole families are held out, and the collapse is
large and **highly significant**:

| metric | random → family | gap Δ (95% CI) | p(Δ≤0) |
|---|---|---|---|
| ROC-AUC | 0.91 → 0.66 | **+0.25** [+0.15, +0.34] | <0.001 |
| PR-AUC | 0.73 → 0.18 | **+0.55** [+0.35, +0.65] | <0.001 |
| watchlist lift | 8.4× → 1.7× | **+6.7×** [+4.1, +9.8] | <0.001 |

A genome model that looks state-of-the-art on a random split is barely above chance
on genuinely novel families. **Most of the apparent skill was phylogenetic leakage.**

### Does it clear the double bar? (paired CIs, family holdout)

- **vs `family_prior` (taxonomy): YES, significantly.** The genome adds real signal
  beyond taxonomy memorisation (ROC 0.66 vs 0.42).
- **vs `effort_only` (research effort): it splits, significantly both ways.** Paired
  Δ (genome − effort) at family holdout:
  - ROC-AUC **+0.14** [+0.04, +0.23], p=0.002 — genome **wins** broad ranking.
  - watchlist lift **−3.4×** [−5.9, −1.5], p≈0.999 — genome **loses** the watchlist.
  - precision@50 **−0.40** [−0.60, −0.18] and PR-AUC **−0.04** [−0.11, −0.004] — genome **loses**.

  So this is not "indistinguishable": on the *deployable* metric (a top-50 watchlist),
  *counting how much a virus has been studied significantly beats reading its genome*
  under true family novelty. The genome's only significant edge is on whole-list
  ranking (ROC), which a surveillance team does not act on.

### Fair-cohort ablation (mammal-only) — leakage, not easy negatives

A reviewer's first objection: maybe the random-split 0.91 is just plant/insect vs
animal separation. We tested it — restricting to **mammal-associated viruses only**
(n = 6,875, 15.7% base rate, the genuinely-hard cohort):

| | random ROC | family-holdout ROC | gap (95% CI) |
|---|---|---|---|
| full cohort (9,201) | 0.908 | 0.660 | +0.25 [+0.15, +0.34] |
| **mammal-only (6,875)** | **0.907** | **0.666** | **+0.24 [+0.14, +0.34]** |

The random AUC **barely moves** (0.908 → 0.907) and the gap is unchanged. The
apparent skill is **phylogenetic leakage, not easy-negative separation** — removing
the easy negatives does nothing to it. The genome-vs-effort watchlist loss persists
(lift Δ −2.3× [−3.8, −0.7], p≈0.995). This kills the easy-negatives objection.

### What *does* generalise (corrected with CIs)

- **Genus holdout:** the genome significantly beats effort on **whole-list ranking**
  (ROC Δ +0.16 [+0.05, +0.24]) — but its *watchlist* edge over effort is **not
  significant** (lift Δ +2.4×, CI crosses 0). The earlier point claim "6.1× beats
  3.7×" does not survive a CI.
- **Temporal:** strong and the one clear genome win (18.6× lift, ROC 0.89) — because
  the split keeps families, so learned family-level signatures transfer forward,
  while `effort_only` *inverts* (ROC 0.14: recent spillovers are under-studied).

So composition learned real **family-level host-range signatures** that transfer
across genera (in ranking) and forward in time — but it does **not** extrapolate to
unseen families. This reproduces the Mollentze-era result (combined AUC ~0.77, never
family-stratified) and the 2025 "Hidden challenges" critique, on our pipeline, with
controls + CIs that make it legible.

### Diagnostics — the leakage, made visible (`results/diagnostics.json`)

**Leakage curve.** Binning every test virus by cosine distance to its nearest
*training* virus, AUC falls from **0.92** (closest bin) through 0.75, 0.66, 0.63 as
distance grows; family-holdout viruses sit at ~2× the distance of random-split ones
(median **0.21 vs 0.09**). The model's accuracy *is* proximity to a known relative.

**Hard-lineage probe (family holdout).** Would a watchlist have surfaced the
lineages that matter? Under family holdout the model ranks **SARS-related
coronaviruses at the 90th percentile** (score 0.43) and **influenza A at the 81st**
(0.26) — *neither makes a top-50 watchlist* — while it *does* flag **Ebola (99th)**.
This is exactly the 2025 "Hidden challenges" lineage-specific failure (SARS-CoV-2,
H5/flu missed), reproduced on our pipeline.

**Watchlist contents (family holdout).** Of the actual top-50, only **10 are
human-infecting (precision@50 = 0.20)**; the rest are animal hantaviruses and
paramyxoviruses whose *composition* resembles high-risk families but which are not
themselves human-infecting. The probe also surfaced a **label-noise case**: the same
virus appears once as positive and once as negative ("nipah henipavirus") — a
concrete instance of the absence-of-evidence problem in §2.

## Verdict (v0, composition)

**The signal is real but narrow, and the headline numbers in this literature are
mostly leakage — now shown with confidence intervals and a fair-cohort control.**
Genome composition beats taxonomy under family holdout (significant) and is a useful
**prioritisation prior for novel viruses within or near known families** (strong
genus-ranking and prospective performance). But on the **deployable watchlist metric**
under genuine family novelty, it is **significantly beaten by a research-effort
baseline that never sees a genome** — and that loss is robust to removing easy
negatives. Any deployment must (a) report the family-holdout number, not the random
one, and (b) be paired with the research-effort control, or it overstates its reach.

**Open question for the next run:** do ESM-2 protein embeddings shrink the
family-holdout gap? The literature (incl. the BERT-infect LLM) suggests not much —
foundation models inherited the same collapse — but it's the one untested rung.
