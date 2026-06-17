# Publication strategy & generalization brief

*Decision-ready synthesis (multi-agent research sweep, web-grounded) on where to publish the zoonotic honest-evaluation study and how it generalizes. Companion to PAPER.md.*

The numbers confirm the framing-strategy track's calibration precisely (15B *ties* host-generalism on PR-AUC: -0.011 n.s.; ties but trends positive on ROC: +0.126, p=0.091; loses on lift@50). The leakage gap and scaling trend are rock-solid (all p≈0). I have what I need.

---

# DECISION BRIEF: Honest-Eval Zoonotic Study

**One-sentence identity of the paper:** *Most genome-based zoonotic-risk skill is phylogenetic leakage; we built a falsification-oriented harness that proves it, and under that harness protein-LM scale—not architecture—recovers leakage-free signal up to a statistical tie with a one-line baseline.* Lead with the critique, carry the scaling result as payload, use the falsified pre-registration as the hook.

---

## 1. WHERE TO PUBLISH

### RECOMMENDED PRIMARY: **Communications Medicine** (Nature Portfolio)
- **Fit:** Published the direct predecessor ("Hidden challenges in evaluating spillover risk," 2025, `s43856-025-00903-w`); you are its quantified sequel, and you answer two questions it explicitly left open (do protein-level features beat nucleotide? — you test ESM-2; and it stops at phylogenetic *visualization* — you formalize it into a leakage-controlled benchmark). Explicitly null-tolerant, public-health scoped.
- **Framing:** Lead with public-health stakes, not ML internals. "Published ~0.91 ROC is largely phylogenetic leakage (gap +0.25 ROC, p<0.001); under honest family holdout a one-line host-generalism baseline beats every model ≤3B; scaling a frozen protein LM 35M→15B recovers real but *bounded* signal that only ties that baseline." Position the harness as a reusable surveillance-evaluation standard.

### BACKUP / FIRST FALLBACK: **Patterns** (Cell Press)
- **Fit:** Home of the Kapoor–Narayanan leakage canon (Patterns 2023) and "Avoiding common ML pitfalls." Frames your harness as a domain instantiation of REFORMS-style leakage auditing; rewards FAIR open data/code (your released harness is a first-class asset). Use if Comms Med wants a more biology-deliverable, less methods-general paper.
- **Framing:** Leakage as a generalizable ML pitfall + reusable honest-evaluation harness; foreground the registered-prediction reversal.

### THIRD: **Virus Evolution** (Oxford, fully OA)
- **Fit:** Most on-target *domain* venue—just published the identical task (sequence-based human-virus host prediction with cross-family validation, `veag009`, 2026). Reviewers grasp the contribution instantly. Evolution/ecology-forward framing: family holdout removes phylogenetic relatives, so the ESM-scaling gain *cannot* be same-family leakage; foreground the leakage-distance curve and the ecological information ceiling.

### FOURTH (methods-purist home): **PLOS Computational Biology**
- **Fit:** Native home if you want to foreground the harness + control ladder + clustered CIs + registered-prediction reversal as a methods contribution. Fair, fast-ish (~5wk first round), ~$2,477. The zoonotic application becomes the testbed.

**ML-venue note (separate audience, if you want an archival CS stamp):** **NeurIPS 2026 Evaluations & Datasets track** is a line-by-line fit (its 2026 rescope explicitly solicits benchmark-failure-mode analyses, leakage/overfitting studies, and negative results; abstract May 4 / paper+code May 6, 2026 AoE). **TMLR** is the safest archival home for the "honest number ties a baseline" story (no SOTA/novelty bar, rolling deadline). Use **MLCB** (deadline Jul 1, 2026) as a *complementary* domain talk—it allows work simultaneously under review elsewhere. **Avoid** ML main tracks (review culture punishes "ties-a-baseline") and **avoid Bioinformatics** (demands a SOTA-beating method; your honest result deliberately is not one).

**Pick one lane.** Biology-journal lane (Comms Med) and CS-archival lane (NeurIPS ED / TMLR) are mutually exclusive as *primary*; pursuing both risks dual-submission issues. Given the paper's public-health payload and the perfect predecessor lineage, **the biology lane via Communications Medicine is the higher fit×prestige product.**

### Minimal extra experiments reviewers WILL demand (do #1 and #3 pre-submission)
1. **A trainable head, not just frozen probes** (highest risk—frozen result is only a lower bound). Minimal sufficient version: one **attention-MIL head** (EvoMIL architecture, `pcbi.1012597`) on 15B embeddings + **one LoRA fine-tune** of a *small* ESM-2, both through the *same family-clustered harness*. You need NOT fine-tune 15B. Expected result (fine-tuning overfits under family holdout) *strengthens* your "overfitting trap" claim—cheap insurance converting major-revision → accept.
2. **A confirmatory second label** (medium risk): re-run the ladder's 35M-vs-15B endpoints on the mammal-infecting label (you already have the n=6,872 mammal cohort) under family holdout. Upgrades "one result" to "a pattern." Only strictly required if a reviewer pushes—but cheap given the pipeline exists.
3. **Explicit VirHostPRED reconciliation** (low effort, non-negotiable): closest prior art and a likely reviewer (`s41598-026-37765-8`, scales ESM-2 8M→15B to 0.914 AUC). State plainly: their split is not family-stratified; you reproduce the monotone scaling but show the honest ceiling. One paragraph + their numbers in your comparison table. This converts your biggest competitor into your motivating Exhibit A.

Do **not** pre-build: fine-tuning 15B, a brand-new benchmark dataset, or ecological-data fusion (keep as discussion).

---

## 2. HOW IT GENERALISES

### The crisp, defensible general claim
> For any genome-/protein-to-phenotype risk model where the input encodes phylogeny and the label correlates with it, a single reported AUC is uninterpretable. We propose a falsification-oriented harness—**whole-cluster holdout + a non-genomic control ladder the genome must beat + cluster-clustered bootstrap CIs + a performance-vs-distance leakage curve + a capacity-matched scaling ladder, all on one shared cohort**—that *decomposes* apparent skill into phylogenetic leakage, genuine cluster-transcending signal, and returns-to-scale, each with a significance test. Applied to viral zoonotic risk: ~0.91 ROC is mostly leakage (honest floor ~0.66, beaten by a one-line host-range baseline), yet scaling a frozen PLM 35M→15B recovers honest signal to a statistical *tie* with that baseline—falsifying our pre-registered prediction that scale would not help.

### What it transfers to (mechanical substitution: swap the cluster unit + the non-genomic control)
- **AMR from WGS** — clade/sequence-type holdout; resistance-prevalence/gene-presence control. (Population-structure confounding is independently documented, PLOS Biol 2025.)
- **Pathogenicity/virulence** — species/serovar holdout; host-range/metadata priors.
- **Drug response / DTI** — scaffold/target-family/patent-year holdout; activity-frequency priors. (Time-split CV already standard.)
- **Protein function (GO/EC) from PLMs** — sequence-family/structural-cluster/release-date holdout; sequence-identity-transfer control.

Holdout, distance curve, clustered CIs, and scaling ladder carry over unchanged.

### Genuinely novel vs. existing OOD tooling — the honest boundary
**Do NOT claim these primitives as novel (each has prior art; claiming them will be caught in review):**
- Cluster/homology-aware splits → DataSAIL, GraphPart, LoHi (solved, well-tooled).
- Leakage-distance curve → **hashFrag (bioRxiv Jan 2025) independently reports the same U-shaped perf-vs-homology pattern.** Your own curve is U-shaped too (AUC 0.916 nearest bin → ~0.635 mid → 0.776 far tail). **Claim confirmatory, not novel.**
- Cluster-aware bootstrap CIs → off-the-shelf (Felsenstein bootstrap, ClusterBootstrap).
- Simple controls beating DL → shown for single-cell perturbation (PMC 2025).

**Three defensible novelty claims:**
1. **The integration:** a single end-to-end protocol that makes leakage *falsifiable*, not merely *avoidable*. Existing tools are point solutions (a splitter, a detector, a baseline lesson); nobody composes holdout + control ladder + clustered CIs + distance curve + scaling ladder on one cohort to *attribute* a number to leakage vs. honest signal vs. scale. The in-domain critique (Comms Med 2025) diagnoses the disease but ships no instrument.
2. **The control-ladder × scaling-ladder crossing:** running a capacity sweep through an identical leakage-controlled harness where the *bar is a one-line non-genomic baseline*—headline result is a *statistical tie with a one-liner*, not a model win—is unreported.
3. **The pre-registered, falsified prediction** inside an OOD-eval harness is a rigor practice essentially absent from this literature.

---

## 3. THE GENERALISATION PHENOMENON — and what is NOT well-supported

### The crisp phenomenon claim (mechanism-bounded)
"Under a leakage-proof whole-family split, frozen PLM scale **monotonically** recovers honest host-compatibility signal that composition models provably lack (family-holdout ROC 0.624→0.757, PR-AUC 0.157→0.293; 15B−35M p≈0). This aligns with the narrow precedent that PLM embeddings carry alignment-free signal *specifically in the evolutionarily-distant regime* (EC-distant enzymes; beyond-homology GO transfer)—but it runs **counter to the field's more common pattern**, where model scale does not help, or hurts, OOD."

### ⚠️ FLAG — claims the research found are NOT well-supported (state these honestly, do not overclaim):
- **"Scaling recovers OOD signal" is NOT a general law.** It is a minority/outlier pattern. Contradicted by: single-cell FMs (Geneformer/scGPT lose to HVG and even random init), molecular property (MolFormer-XL on 1.1B molecules beaten 13/14 by a 250K-molecule model), twilight-zone homology, and—**most damaging because it's your sister task—ESM-2 fitness on ProteinGym *declines* with scale (PTEN: 150M Spearman 0.55 → 15B <0.3).** The general theoretical statement (materials OOD paper, arXiv:2406.06489): neural scaling laws are validated *only* for representationally-in-distribution data; model scaling can be *adverse* OOD. **Frame your monotonic curve as a task-specific positive outlier, not a rule. This actually strengthens your falsified pre-registration—you bet against scale because the field's prior says scale fails OOD.**
- **The genome does NOT beat the baseline on the deployment metric.** 15B vs host-generalism: PR-AUC −0.011 (n.s.), ROC +0.126 (p=0.091, *not* significant at 0.05), and lift@50 still *favours the baseline* (−1.02). The honest word is **"ties," never "beats."** Any "scale recovers signal" headline that implies a win will be shot down.
- **Do NOT claim "fails to flag SARS/H5."** Your hard-lineage probe is underpowered (n=1–5; SARS/MERS probed taxa are VIRION-labeled y=0; among true positives ebola ranks 98–99th pctile). Use only the **cohort-level** watchlist failure (family-holdout p@50=0.12 ≈ base rate 0.117). Cite Comms Med 2025 for documented lineage-specific failures.
- **The leakage-distance curve is U-shaped, not monotone**—don't sell it as clean monotonic decay; the honest reading (AUC lowest ~0.635 in mid-distance bins where most family-holdout viruses sit, recovering in the sparse far tail) is more defensible and matches hashFrag.

### The mechanistic next step: is interaction-modelling worth it?
**The `mechanistic` research track returned null**—there is no evidence base supporting an interaction-modelling claim, so **do not make one in this paper.** Decisively:
- **NOT this paper.** This paper's identity is evaluation-science (leakage decomposition + scaling-under-shift + harness). Adding a mechanistic interaction model would dilute the spine, invite a different reviewer pool, and rest on an evidence base you do not have.
- **As a follow-up, only conditionally.** The honest result establishes an *information ceiling*: the label is partly governed by ecology/exposure/sampling not written in the sequence, and the genome only ties cheap metadata. That implies the productive next paper is **not** a bigger sequence model but **host–virus interaction modelling that injects the off-sequence variables** (host phylogeny/receptor compatibility, ecological contact networks)—i.e., model the interaction the ceiling argument says is missing. Frame interaction-modelling as the *motivated future direction your ceiling result points to*, mentioned in Discussion, and pursued as a separate paper **only after** scoping whether the requisite interaction data clears the same family-holdout bar. Given the null evidence base, treat "is it worth it" as **unproven—a hypothesis the ceiling argument generates, not a result.**

---

### Relevant files
- `/Users/linus/coding/zoonotic/PAPER.md` (draft; currently leads with the scaling result—**recommend flipping the title to lead with the leakage critique**)
- `/Users/linus/coding/zoonotic/PAPER_FACTS.md` (canonical numbers—verified against this brief)
- `/Users/linus/coding/zoonotic/docs/discussion_section.md` (§8.5 lists three default practices—extend with the transfer table in §2)
- `/Users/linus/coding/zoonotic/models/eval_ladder.py` (scaling-ladder harness implementation)
- `/Users/linus/coding/zoonotic/results/ladder.csv`, `results/canonical_results.json`, `results/confidence_intervals.json` (backing data)
