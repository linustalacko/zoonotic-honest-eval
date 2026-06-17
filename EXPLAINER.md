# Can a virus's genome tell us if it will infect humans? What we did, from first principles — and what it means

*A plain-language companion to the technical paper (`PAPER.md`). No background assumed.*

---

## 1. The question, and why it matters

Most new human diseases come from animals — HIV, Ebola, influenza, SARS, COVID-19 all "spilled over" from a wildlife or livestock host. There are hundreds of thousands of animal viruses we've barely characterized. If we could look at a virus's **genome** — its raw genetic sequence — and predict *"could this one infect people?"*, we could prioritize which to study, surveil, or develop countermeasures against, before it ever reaches a human. That is the dream behind a decade of "genome → zoonotic risk" machine-learning papers, many reporting impressive accuracy (~90%).

This project asked a simpler, more skeptical question: **is that accuracy real, or is it an illusion of how the models are tested?** And then, unexpectedly, it found something more hopeful than we set out to.

---

## 2. The hidden trap: why 90% accuracy can mean almost nothing

Here is the single idea the whole project turns on.

Viruses come in **families** (coronaviruses, influenzas, herpesviruses…). Close relatives tend to share traits — including whether they infect humans. Now imagine you train a model and test it the usual way: shuffle all viruses, train on a random 80%, test on the other 20%.

The problem: a test virus almost always has a **close cousin sitting in the training set, with the same label**. So the model can score a near-perfect grade just by noticing *"this looks like that known human virus over there."* It never had to learn any biology. It learned **family resemblance**.

> **The analogy:** it's like testing a student with the exact questions they saw on the practice exam. They ace it — and have learned nothing. The real test is *new kinds of questions*.

We call this **phylogenetic leakage** ("phylogeny" = the family tree of life). The fix is the **honest test**: hold out **whole virus families** during training, then test on those families. Now the test virus has *no* cousin to lean on. The model must actually generalize to something genuinely new — which is exactly the situation you'd face with a newly discovered virus from an unfamiliar lineage.

Almost the entire field reports the easy (leaky) number. We measured both, with statistics, on open data.

---

## 3. What we built

**The data.** ~9,200 viruses from VIRION, an open public database. Each is labelled *positive* if it's ever been recorded infecting a human, *negative* otherwise. Only ~12% are positive. We fetched each virus's genome.

**Four ways to test, not one:**
- **Random split** — the easy, leaky test the field uses (our "looks-great" reference).
- **Family holdout** — hide whole families; the **honest** test (our headline).
- **Genus holdout** — stricter still.
- **Temporal** — train on old viruses, predict newer ones.

**A ladder of "controls" — cheats we make the genome beat.** A genome model only earns its keep if it beats dumb baselines that use *no biology*:
- the **base rate** (just guess the average),
- **taxonomy memorization** (predict from family alone),
- and the one that stings — **host generalism**: *a single number, how many different host species the virus is already known to infect.* (Generalist viruses jump species more.) One line of metadata, no genome at all.

**Honest statistics.** Because viruses in a family are correlated, we don't treat 9,200 viruses as 9,200 independent data points — the *effective* sample size is closer to the ~100 families. So every confidence interval is computed by **resampling whole families**, which is the honest unit. This stops us from calling noise a result.

**The representations — how the model "reads" the genome.** We went from simple to state-of-the-art:
- **Composition**: count patterns of letters (k-mers, dinucleotide bias) — cheap, classic.
- **ESM-2 protein language models**: think "GPT, but trained on hundreds of millions of protein sequences." It turns each viral protein into a rich numeric fingerprint. These come in sizes from 35 million to **15 billion** parameters. This is the representation the current SOTA is built on.

---

## 4. What we found

### Finding 1 — Most of the "90% accuracy" is leakage.
Our composition model scores **0.91** on the easy random test. On the honest family-holdout test it **collapses to 0.66** (barely above a coin flip, once you account for how rare positives are). The drop is large and statistically rock-solid. We proved it's leakage, not some easy-data artifact, by showing it survives even when we restrict to the genuinely hard mammal-only viruses, and by drawing a **"leakage curve"**: accuracy is almost entirely a function of *how close the test virus sits to a known relative*. Close cousin → 0.92. No cousin → ~0.64.

### Finding 2 — At normal scale, a one-line baseline beats the genome.
Under the honest test, the trivial **host-generalism** number (how many hosts the virus has) **matches or beats** both composition *and* a frozen 150M-parameter ESM-2, on the metric a real watchlist cares about (precision at the top of the ranked list). Reading the entire genome bought essentially nothing over one line of ecological metadata. Sobering.

**If we had stopped here, the paper would have been a clean negative result: "genome-based zoonotic prediction is mostly leakage, and a triviality beats it."** We expected the next finding to confirm that. It didn't.

### Finding 3 (the surprise) — Scale recovers real, honest signal.
We ran the *same honest test* across the full ESM-2 size ladder — 35M → 150M → 650M → 3B → 15B parameters — holding everything else fixed. The honest score climbed, **monotonically**, the whole way:

| ESM-2 size | honest ROC | honest PR-AUC |
|---|---|---|
| 35M | 0.624 | 0.157 |
| 150M | 0.648 | 0.169 |
| 650M | 0.664 | 0.178 |
| 3B | 0.708 | 0.207 |
| **15B** | **0.757** | **0.293** |

From 35M to 15B, the honest precision **nearly doubled** (0.157 → 0.293), and this jump is statistically airtight (p ≈ 0). **This cannot be leakage** — leakage can't help you on families you've never seen a relative of. So the bigger models are extracting *genuine* biology that the smaller ones (and composition) throw away — most likely functional and structural protein features that track adaptation to host machinery, not just ancestry.

### The crossover.
The host-generalism baseline that **beat every model up to 3B** is, by 15B, **drawn level**: the gap closes from −0.147 (35M) to −0.011 (a statistical tie) at 15B, and on overall ranking the 15B genome actually edges *ahead*. The triviality that humbled the genome no longer beats it once the representation is big enough.

*(See `docs/scaling_ladder.png` for the figure: the leaky line stays flat and high; the honest line climbs from the floor to meet the baseline.)*

---

## 5. What this means

**The honest ceiling is not fixed — it moves with scale.** The field's pessimism ("genomes can't honestly predict zoonosis") and our own first guess ("scale won't help") were both wrong. Honest, leakage-free signal *does* exist in the genome, and **more representation scale extracts more of it.** That is a genuinely new and hopeful result, and to our knowledge the first time it's been shown under a leakage-proof evaluation.

But two limits keep us honest:

1. **15B *ties* the one-line baseline; it doesn't *beat* it.** And in absolute terms the honest performance is still modest. We're matching a triviality, not delivering a deployable oracle — yet.

2. **The ecological ceiling.** Whether a virus is *recorded* infecting humans depends on molecular compatibility (which is in the genome) **and** on ecology — who is exposed to what, where, how often, and how hard anyone looked (which is **not** in the genome). No model, at any size, can read exposure off a sequence. So a real fraction of the answer is permanently invisible to a genome-only model.

There's also a methodological takeaway the field should adopt: **always report the honest (family-held-out) number with cluster-aware confidence intervals, benchmark against non-genomic baselines, and report performance *as a function of model scale*** — because, as we showed, the answer changes completely depending on which of those you do.

---

## 6. Would scaling to 100B get us to "SOTA"? Are we already there?

This is the sharpest question, and the answer depends entirely on **which SOTA** you mean — the same leaky-vs-honest split as everything above.

**SOTA-the-number (leaky, ~0.91 ROC).** Published models report this on random splits. We're **already past it** — 15B hits 0.918 on the random split, and plain composition already matched 0.910. But this number is **mostly leakage**: it's the score for recognizing relatives, not for predicting biology. Being "at SOTA" here is meaningless; it's the wrong target, and chasing it with more parameters just buys more of an artifact.

**SOTA-that-generalizes (honest).** Here almost no one else even measures, so the frontier is essentially what we just drew — and it's modest (0.757 ROC / 0.29 PR). Would 100B get us meaningfully further?

My honest read:

- **The curve hasn't flattened — it's steepening.** The biggest single jump is the *last* one (3B→15B added more than any step before it). So there is clearly more honest signal still to extract; we are not at the honest ceiling. A 100B-class model would, I'd bet, push honest ROC into the high-0.70s/low-0.80s and precision to maybe ~0.35–0.45 — possibly enough to **beat** the host-range baseline outright, not just tie it. That would be a real, useful improvement.

- **But it will never reach the leaky 0.91 honestly.** That figure is inflated by leakage and capped from above by the ecological ceiling. Scaling runs *into* that ceiling, not through it. Expect the honest curve to bend over and plateau somewhere well short of the headline number.

- **Two important caveats.** First, **there is no 100B ESM-2** — it stops at 15B. Going bigger means a *different* model (e.g. ESM-3, a different architecture and training recipe), so it's not a clean continuation of our curve. Second, we did a focused literature review of *which* levers would actually raise the honest score (saved as `docs/improvement_roadmap.md`), and it corrected an intuition we started with. **Fine-tuning the 15B is *not* the cheap win** — with only ~1,000 noisy positive examples, fine-tuning is the lever most likely to *overfit* (memorize families) and inflate the leaky number while doing little or nothing for the honest one; on the closest comparable tasks a frozen model actually beats a fine-tuned one. The one lever with a genuine path to a higher honest score is **fusing the genome model with off-genome information** (host-range breadth + ecology) — but that's no longer a pure genome model. Realistically, a determined honest effort tops out around **ROC ≈ 0.78, precision-AUC ≈ 0.33** — a little above where 15B already sits, and bounded by the ecological ceiling.

**So: we are at SOTA on the number that doesn't matter, and at the (still-rising) frontier on the number that does. More scale will keep helping, then plateau against ecology — it gets us to "genuinely beats the trivial baseline," not to "solved."**

---

## 7. What would actually move the needle

In rough order of bang-for-buck (full evidence in `docs/improvement_roadmap.md`):

1. **Fuse the genome with off-genome signals.** This is the *only* lever that adds genuinely new, family-transcending information: combine the genome model with host-range breadth and ecological traits. Expected honest gain ~+0.02 ROC / +0.03 PR — small, but real, and it's the one thing that isn't already baked into the sequence. (The catch: it's no longer a pure "genome" model.)
2. **Clean up the labels.** The "negatives" are partly just under-studied viruses. Re-weighting for that (using only information available for unseen families) adds a sliver more honest precision.
3. **Model the *interaction*, not the virus alone.** The deep reason virus-only models struggle: they implicitly ask "does this look like a human virus?" — a question whose only training signal is ancestry. The mechanistic question is "are this virus's proteins compatible with the **fixed** human machinery they must engage?" — receptors, proteases, immune factors. Promising in principle, but hard: predicted protein structures are least reliable for exactly the proteins that decide human infection, and a past attempt at receptor-binding prediction didn't beat a coin flip.
4. **What *won't* help much:** simply fine-tuning or scaling to a bigger model. Fine-tuning ~1,000 noisy examples mostly overfits (it inflates the *leaky* number, not the honest one); newer/bigger protein models encode the same family resemblance just as strongly. These re-weight signal the genome already contains — they don't add new signal.

The honest north star isn't a 0.99 AUC — the ecology forbids it. It's **the best leakage-free model we can build (now demonstrably improvable, to ~0.78, with scale and fusion) used as one input alongside watching the places where spillover actually happens.**
