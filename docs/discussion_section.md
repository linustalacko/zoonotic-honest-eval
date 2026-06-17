## 8. Discussion

### 8.1 The ceiling is structural, not a tuning failure

Every feature available to a virus-only classifier — nucleotide composition,
dinucleotide bias, codon usage, *k*-mer spectra, and the protein-language-model
embedding alike — is a deterministic function of the genome sequence, and the
genome sequence is itself a near-perfect phylogenetic coordinate. Two viruses
that sit close together in any of these feature spaces do so because they are
evolutionarily related. A classifier trained on such features therefore
necessarily learns a decision boundary *in phylogenetic space*: in effect, "this
virus resembles known human-infecting viruses." Under a random split that
boundary is highly accurate, because most test viruses have a close relative in
the training set that shares their label — exactly the regime the leakage curve
makes visible, where discrimination is 0.92 for nearest-neighbour viruses and
decays toward the family-holdout level as that relative is removed. Under family
holdout the boundary has nothing to anchor to, and accuracy falls to the level of
the weak, family-transcending correlates that remain.

This is an identifiability problem, not a capacity problem: no number of
additional parameters can recover information the representation does not contain.
Our scaling ladder makes the point empirically — from 35M to 15B parameters the
family-holdout AUC is flat, even as the random-split AUC and the model's general
protein-modelling ability grow. The protein-language model has learned a great
deal about proteins; what it has learned about *human-infection potential*, under
genuine taxonomic novelty, is the same phylogenetic signal that nucleotide
composition already captured. This is consistent with reports that PLM embeddings
linearly encode taxonomy: a bigger phylogenetic coordinate is still a
phylogenetic coordinate.

### 8.2 What the residual signal is, and why it is not deployable

Family-holdout discrimination is not zero, and we are careful not to claim it is.
Composition exceeds pure taxonomy memorisation by a small but statistically
significant margin (ROC +0.23, PR-AUC +0.07; both *p* < 0.001), so some genuinely
family-transcending sequence correlates of human infection do exist — plausibly
signatures such as CpG/UpA dinucleotide suppression that track adaptation to
vertebrate antiviral pressure rather than ancestry alone. But that residual is
small, and on the metrics that actually govern a surveillance watchlist —
precision and lift among the top-ranked candidates — it does not exceed, and is in
fact beaten by, a one-line non-genomic baseline: the breadth of a virus's known
host range. For the operational task of ranking which novel viruses to prioritise,
counting how many host species a virus has already been observed in is at least as
informative as reading its genome (host-generalism family-holdout PR-AUC 0.30 vs
composition's 0.18; ΔPR-AUC −0.13, 95% CI [−0.23, −0.06]). This is a sobering
result for genome-first triage, and a useful one: it says the marginal value of
the sequence, *over cheap ecological metadata*, is approximately nil under genuine
novelty.

### 8.3 The reframe that could carry generalisable signal

The failure mode suggests its own remedy. A virus-only model implicitly asks "does
this sequence look like a human virus?" — a question whose only training signal is
phylogenetic. The mechanistic question is different: "are this virus's proteins
compatible with the human molecular machinery they must engage?" — receptor usage,
entry and protease processing, replication-complex compatibility, and evasion of
human innate-immune and restriction factors. Crucially, the *human* side of that
interaction is fixed and shared across all candidate viruses: the same receptors,
the same proteases, the same restriction factors. A model that scores a viral
protein against those fixed human targets has an invariant to extrapolate from,
and is not forced to route its prediction through "which known family does this
most resemble." This is interaction modelling (viral protein × human protein)
rather than virus-alone classification, and it is where structure- and
docking-based methods and protein–protein-interaction models are most likely to
add value beyond the phylogenetic ceiling. We did not build such a model here; our
contribution is to show, with controls and confidence intervals, that the
virus-alone framing has reached its ceiling, and *why*.

### 8.4 An information ceiling: why "AlphaFold-level" is the wrong aspiration

Even a perfect molecular-compatibility model would be bounded. Whether a virus is
recorded infecting humans is determined jointly by molecular compatibility and by
ecology — the degree of contact between the reservoir host and people, geography,
host abundance, sampling effort — and the ecological terms are not written in the
viral genome. The label we predict ("has been observed to infect humans") is a
noisy, exposure-confounded readout of that joint process. AlphaFold succeeds
because protein structure is, to good approximation, a closed deterministic
function of sequence: the input contains the answer. Human-infection potential is
an open ecological outcome only partially determined by the genome, so a
substantial fraction of its variance is, in principle, not recoverable from
sequence at any model scale. The right aspiration is therefore not a single high
AUC but a *calibrated molecular-compatibility score that is honest about the
ecological variance it cannot see* — paired with an evaluation protocol, like the
one used here, that does not let phylogenetic leakage masquerade as that score.

### 8.5 Implications for reported performance in the field

Our results do not impugn the published models as software. Composition and PLM
features genuinely separate human- from non-human-associated viruses at ROC ≈ 0.9
— on a random split. The point is that this number answers the wrong question for
the deployment setting, because it is dominated by interpolation among already
known families. We suggest the field adopt three practices as defaults: report
family- (or, better, clade-) stratified performance with cluster-aware confidence
intervals as the *primary* metric; benchmark every genome model against the
non-genomic controls used here (taxonomy and host-range breadth), crediting the
genome only where it beats them; and treat the random-split number as an
upper-bound diagnostic of leakage, not as a capability claim. The 2025
*Communications Medicine* critique made this case qualitatively for a single
model; we quantify it, attach confidence intervals to it, and show that it
survives the strongest representation currently available.
