# Why genome-based zoonotic-risk models don't generalize — and how we fix it

A literature-grounded teardown of the models this project reproduces, the
documented reasons they fail in prospective use, and the concrete design
responses baked into (or planned for) this pipeline. Read alongside
[`FINDINGS.md`](../FINDINGS.md).

---

## 1. The models, and what they actually score

| Model | Approach | Reported headline | The catch |
|---|---|---|---|
| **Mollentze, Babayan & Streicker 2021** (PLOS Biology) — `zoonotic_rank` | genome composition + phylogenetic-neighbourhood + taxonomy → bagged GBM, 861 species / 277 human-infecting | **combined AUC ≈ 0.773**; composition-only 0.69–0.70; similarity-only 0.56; taxonomy-only 0.60 | the "good" number is **0.77, not 0.95** — and they state they *"were unable to additionally stratify training set selection by virus family due to the small numbers of species in many families."* No family holdout. |
| **"Hidden challenges…" 2025** (Communications Medicine; bioRxiv 2024.04.25.591033) — BERT-infect + survey | nucleotide LLM over 26 families | median **PR-AUC > 0.75**; LLM beats prior models on most families | **failed to flag SARS-CoV-2-related viruses and H5 influenza** (>900 human infections) despite high aggregate scores |
| **Host-prediction k-mer models** (Young/Mock et al. 2020, PLOS Comp Biol) | 4-mer SVM | weighted **F1 0.79** for hosts of *unknown genera* (vs 0.72 di/tri-nt, 0.68 tBLASTx) | accuracy collapses at lower taxonomic ranks (species/genus) — i.e. exactly where novelty lives |
| **Wardeh et al.** (Lancet Microbe 2021; Comm. Biol. 2022) | host–virus network link prediction | high recall on held-out links | only predicts for hosts/viruses with **existing data**; favours well-sampled species |
| **Olival 2017 / Grange SpillOver / Han** | host & virus traits → boosted regression / risk scores | ranked watchlists | trait availability is itself an artefact of research effort |

**Takeaway:** even the best honest published number is **moderate (~0.77 AUC) and was not family-stratified.** The field's "it works" rests on splits that leak taxonomy.

---

## 2. Why they fail (six mechanisms, each cited)

### F1 — Phylogenetic / taxonomic leakage *(the dominant one)*
Random train/test splits put close relatives of a test virus in training, so the
model can score by recognising the **family**, not by learning zoonotic biology.
Host-prediction work that explicitly withholds **whole families** shows predictive
features *"contain signals reflecting both the evolutionary relationship between
viruses infecting related hosts, and host-mimicry"* (Young/Mock 2020) — i.e. the
signal is **part biology, part taxonomy**, and the two are entangled. Difficulty
*"is most apparent at lower taxonomic ranks of species and genus."* Mollentze
themselves could not stratify by family.

### F2 — Label noise: absence-of-evidence negatives + research-effort bias
"Not observed in humans" ≠ "cannot infect humans." Negatives *"may represent
unrealized, undocumented, or genuinely nonzoonotic species"* (Mollentze 2021).
Worse, positives track **study intensity**: *"there is a significant relationship
between the number of viral species and the number of zoonotic viral species in a
particular host"*, so models *"may simply be demonstrating which host taxa have
been studied most extensively"* ("How accurately can we assess zoonotic risk?",
PLOS Biology 2021). Concretely: *97% of Orthomyxoviridae papers consider only
influenza A and B*; many hantaviruses are *described once with no follow-up*.

### F3 — Base-rate / metric inflation
Spillover-capable viruses are rare, so ROC-AUC flatters: a model can post a high
AUC while its top-ranked watchlist is mostly false positives. The honest metrics
are **PR-AUC** and **precision@k / top-N watchlist precision** — and even at
"PR-AUC > 0.75" the 2025 critique shows the watchlist misses the lineages that
matter.

### F4 — Composition is blind to small functional changes
Host jumps often hinge on **a few amino-acid changes** (SARS-CoV-2 spike; H5
influenza). The 2025 study: infectivity *"changed by limited mutations, mainly in
the spike protein,"* which nucleotide-composition models *cannot* capture, and
genera with *"frequent shifts in infectivity during evolution"* (Flavivirus,
F1 ≈ 0.6) defeat them. Six families are consistently hard: **Circoviridae,
Coronaviridae, Flaviviridae, Hepeviridae, Rhabdoviridae, Hantaviridae.**

### F5 — Target leakage / label–objective mismatch
Labels are usually defined by *the host the sequence was isolated from*, so the
model is trained on *"a fundamental mismatch between training objectives and real
biological infectivity"* (2025). It also can't separate **infectivity** (can it
enter human cells) from **transmissibility** (can it spread human-to-human).

### F6 — Foundation models don't rescue it
BERT-infect (a nucleotide LLM) *"outperformed existing models across most viral
families"* yet **still failed on SARS-CoV-2-related viruses and H5** — bigger
models inherit the same leakage and label problems. Embeddings help at the
*margin*, not at the *mechanism*.

---

## 3. Fixes → mapped to this pipeline

Legend: ✅ already built · 🟡 partially built · ⬜ proposed (model-plan phase)

| # | Failure | Fix | Status here |
|---|---|---|---|
| F1 | taxonomic leakage | **Hold out whole families/genera** (StratifiedGroupKFold by family; genus variant). Report random vs holdout side by side; the **gap** is the result. | ✅ `build_splits.py` |
| F1 | leakage is a gradient, not binary | **Distance-to-nearest-training-virus** as an *eval axis*: bin test viruses by composition/phylo distance to the closest training virus and plot performance decay. Also usable as a feature to expose the model's reliance on relatives. | ⬜ proposed |
| F2 | absence-of-evidence negatives | Treat as **positive-unlabeled (PU)** learning, not clean 0/1; or at minimum report sensitivity to negative definition. Restrict the cohort to **mammal-associated** viruses (the real easy-negative lever: 28.7% of negatives are non-mammal; only 4.1% are non-vertebrate). Fair cohort = 6,890 viruses / 15.7% base rate. | 🟡 host-class flags in `build_labels.py`; PU ⬜ |
| F2 | research-effort bias | **Research-effort baseline + control feature**: study-effort proxies (PubMed/WoK cites from HP3; #associations, #sequences, #hosts from VIRION). New ladder rung — *does the genome model beat a study-effort-only predictor?* If not, it's measuring attention, not biology. | ⬜ proposed (HP3 has `vPubMedCites`/`vWOKcites`) |
| F3 | AUC inflation | **PR-AUC, precision@k, lift@k**, per-split. | ✅ `models/evaluate.py` |
| F3 | watchlist realism | Show what a **top-50 watchlist** actually contains under holdout. | 🟡 p@k built; explicit watchlist dump ⬜ |
| F4 | composition blind to point mutations | **Protein-level features (ESM-2)** to test whether amino-acid signal helps on the cases composition misses — *framed honestly*: the literature shows it's not a silver bullet. Report it as an ablation, not a headline. | 🟡 `features/embeddings.py` scaffolded |
| F4 | hard lineages | **Hard-lineage probe**: per-family metrics + an explicit check of whether known hard cases (SARS-CoV-2-related, H5) would be flagged at the operating threshold. | ⬜ proposed |
| F5 | label = host-of-detection | Document the infectivity-vs-transmissibility and detection-host caveats; keep the label definition explicit and versioned. | ✅ documented in `build_labels.py` / FINDINGS |
| F6 | FM hype | Treat embeddings as an **ablation that must shrink the holdout gap to earn its place**, not a default. | ✅ that's the ladder design |

---

## 4. The reference ladder, revised in light of the literature

The original ladder (`prior → family_prior → composition → ESM`) gets **two new
control rungs** that the research says are essential:

0. `prior` — base rate floor.
1. `family_prior` — **taxonomy-memorisation control**. Collapses to prior under family holdout.
2. **`effort_only`** *(new)* — predict from **research-effort proxies alone** (cites, #associations, #sequences). If the genome model can't beat this under holdout, it's tracking study bias (F2).
3. `composition + logreg` / `composition + xgboost` — the zoonotic_rank stand-in.
4. `esm + classifier` — must **shrink the family-holdout gap** vs composition to justify itself (F4/F6).
5. *(diagnostic, not a model)* **leakage curve** — performance vs distance-to-nearest-training-virus (F1).

A genome model is only interesting if, **under family holdout**, it beats *both*
`family_prior` *and* `effort_only`. That double control is the bar the literature
implies and almost no published model clears cleanly.

---

## 5. Honest scope (the verdict this reframes)

The research forces a narrower, more defensible claim than "predict the next
pandemic":

- Genome composition captures **broad, family-level host-range signal**. It is
  useful for **triaging novel viruses from under-studied families** into "worth a
  closer look" — a coarse prior.
- It **cannot** resolve **single-mutation host jumps** (the SARS-CoV-2/H5 cases)
  — that needs protein structure/function and experimental virology, and even
  LLMs fail it today.
- Any deployable output is a **surveillance-prioritisation prior**, not a verdict,
  and should be paired with interface surveillance at the animal–human boundary
  (the standing recommendation of the critique literature).

So the v0 question stands, sharpened: *under family holdout, does composition (or
ESM) beat both the taxonomy control and the effort control — and by enough to
change which 50 viruses you'd actually look at?*

---

## Sources

- Mollentze, Babayan & Streicker (2021). *Identifying and prioritizing potential human-infecting viruses from their genome sequences.* PLOS Biology. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001390
- *Hidden challenges in evaluating spillover risk of zoonotic viruses using machine learning models* (2025). Communications Medicine. https://www.nature.com/articles/s43856-025-00903-w · preprint https://www.biorxiv.org/content/10.1101/2024.04.25.591033v1
- *How accurately can we assess zoonotic risk?* (2021). PLOS Biology. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001135
- Young, Mock et al. (2020). *Predicting host taxonomic information from viral genomes: a comparison of feature representations.* PLOS Comp Biol. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007894
- *Prediction of virus–host associations using protein language models and multiple instance learning* (2024). PLOS Comp Biol. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012597
- *The effect of taxonomic, host-dependent features and sample bias on virus host prediction…* (2025). Scientific Reports. https://www.nature.com/articles/s41598-025-17123-w
- Wardeh et al. (2021). *Optimizing predictive models to prioritize viral discovery in zoonotic reservoirs.* Lancet Microbe. https://www.thelancet.com/journals/lanmic/article/PIIS2666-5247(21)00245-7/fulltext
