# Can we break the composition ceiling? — research synthesis + decision

**Context.** Under honest family-holdout, whole-genome *composition* caps at
**~0.66 ROC-AUC / ~0.18 PR-AUC** on our data, CI-confirmed — and 60+ model/feature
configs (hill-climb rounds 1–4) fail to beat it significantly. The bottleneck is
*phylogenetic leakage + label noise*, not the model. This document asks, against
the 2024–2026 literature: **what actually raises the honest ceiling, and what is
just a higher-starting leak?** Then it states what we execute.

---

## The levers, with evidence

### 1. Protein language models (ESM) + multiple-instance learning — the SOTA representation
**Verdict: real improvement over composition, but it does NOT escape leakage.**

- **EvoMIL** (Liu et al., PLOS Comput Biol 2024) — ESM-1b (1280-d) embeddings per
  protein, **attention-based MIL** aggregating a virus's proteins into one bag-level
  prediction. Eukaryotic-host **binary AUC ≈ 0.85**; beats k-mer / AA / physicochemical
  features by ~2–16% F1. *But it self-reports the catch:* performance **"drops
  significantly at lower taxonomic ranks,"** viruses are **"misclassified as closely
  related hosts,"** and it **"exploits phylogenetic signal rather than host-specificity
  mechanisms directly."** Same collapse as composition — starting higher.
- **VirHostPRED** (Sci Rep 2026) — ESM-2 scaled 8M→**15B** + SVM-RBF → **0.914 AUC /
  0.852 acc** on a held-out test; bigger ESM helps monotonically. (Could not confirm
  the split is phylogeny-aware; given the field, likely identity-filtered, not
  family-holdout → inflated.)
- **ESM encodes phylogeny.** "Protein language models learn phylogenetic
  relationships" (bioRxiv 2022.03.29.486219; 2024.09.23.614642) and **"data leakage
  from pretraining consistently inflates performance"** (bioRxiv 2024.07.23.604678).
  So an ESM model under family holdout still has *phylogeny baked into its features* —
  it cannot fully escape the taxonomy confound; it can only mask it.
- **Our pending ESM run used mean-pooling** — the literature's *inferior* aggregation.
  MIL / max-pool is the documented upgrade.

### 2. Receptor-binding / structure (the "AlphaFold analog") — **rejected for general use**
**Verdict: pathogen-specific, poor generalization. Not a general ceiling-raiser.**

- ML predicts **spike↔ACE2** binding at ~87% (CCDC Weekly 2021), and AlphaFold2-based
  structural features help virus–host PPI prediction (Brief Bioinform 2025). But the
  honest test fails: **"no ACE2 representation … performed markedly better than a null
  model in predicting host susceptibility"** (eLife 2022;11:e80329). Receptor binding
  works *within* a studied system (SARS-CoV-2), not as a general virus→human predictor —
  and for most viruses the human receptor is unknown, so coverage is near-zero. **High
  cost, narrow payoff. Deprioritize.**

### 3. Label de-biasing — positive-unlabeled / propensity correction — **execute**
**Verdict: directly targets OUR specific finding (effort beats the genome).**

- **Dynamic PU-learning (DPU)** (Research Square rs-7187859, 2025) — extends PU learning
  with a **propensity model** that estimates the chance a true link is *observed*, then
  corrects for **research-effort / sampling bias**, evaluated on **VIRION**. This is the
  formal fix for our F2: the `effort_only` control beating the genome model is a *labeling
  artefact*; correcting it could change the verdict. Lightweight (works on existing
  features + a propensity model).

### 4. Better data — improved positive/negative sets — **adopt where cheap**
- "An Improved Dataset for Predicting Mammal-Infecting Viruses" (bioRxiv 2025.09.17.676952)
  rebuilds the mammal-virus label set. Data quality is the real ceiling — AlphaFold's
  foundation was 170k clean labels; we have ~1.1k noisy ones. Curation-heavy; our cheap
  version is the mammal-restricted fair cohort (already built) + the de-biasing above.

### 5. Nucleotide foundation models (Evo / Evo 2) — **deprioritize**
- Evo (Science 2024) — 7B params, 131kb context, but trained on **prokaryotic/phage**
  genomes; zero-shot strength is in prokaryotic function, not eukaryotic host range.
  Heavy, marginal for our task.

---

## Why "AlphaFold-level" is not reachable here (the honest boundary)

Every method that posts a high number — composition, ESM-MIL, nucleotide LLMs — is shown
(by its own authors or by the 2025 *Communications Medicine* critique) to **exploit
phylogeny and collapse on novel taxa.** AlphaFold worked because sequence→structure is a
near-deterministic, MSA-rich mapping with 170k clean labels. virus→human-infectivity is
**partly ecological** (exposure, reservoir overlap — irreducible noise) with ~1.1k noisy
labels. A model that shows >0.9 *under family holdout* would almost certainly be leaking —
the exact failure this project exists to catch. **The honest north star is the best
leakage-free model, ~0.70–0.80 AUC at most — not AlphaFold.**

---

## Decision — what we execute (in order)

1. **ESM-2 protein embeddings through the honest-eval ladder (the SOTA representation,
   rigorously tested).** Richer aggregation than mean-pool (mean+max+std, approximating
   MIL's "most-discriminative-protein" signal). Run it across random / family / genus /
   temporal with the `effort_only` control and **family-clustered bootstrap CIs**. The
   question only *our* harness answers cleanly: *does the protein-LM SOTA beat composition
   AND the effort control under family holdout, or does it collapse higher?* Either answer
   is a real result; the latter extends the leakage critique to the ESM-MIL SOTA.
2. **Label de-biasing (propensity-weighted / PU).** Estimate each virus's observation
   propensity from research-effort proxies; reweight/relabel; re-run the ladder to test
   whether the `effort_only`-beats-genome verdict is a labeling artefact.
3. **Report honestly** — including, most likely, that the SOTA also leaks. That is the
   contribution: not a magic number, but the rigorous map of the honest frontier.

Rejected: receptor/structure (poor generalization), Evo (marginal/heavy), and any pursuit
of an AlphaFold-level number (unreachable without leaking).

### Sources
- EvoMIL: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012597
- VirHostPRED (ESM-2 host range): https://www.nature.com/articles/s41598-026-37765-8
- PLMs learn phylogeny: https://www.biorxiv.org/content/10.1101/2024.09.23.614642 · pretraining leakage: https://www.biorxiv.org/content/10.1101/2024.07.23.604678
- ACE2 receptor null-model result: https://elifesciences.org/articles/80329
- Dynamic PU-learning on VIRION: https://www.researchsquare.com/article/rs-7187859/v1
- Improved mammal-virus dataset: https://www.biorxiv.org/content/10.1101/2025.09.17.676952
- Evo: https://www.science.org/doi/10.1126/science.ado9336
