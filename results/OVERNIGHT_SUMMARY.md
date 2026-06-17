# Overnight generalisation search — FINAL VERDICT (morning)

Ran the full **9.0 hours** (23:02 → 08:03), **450 logged runs**. Detail in `generalization_journal.md`, numbers in `generalize_runs.csv`.

## Did it generalise beyond what we had? — Partly. Not in the strong sense.

**The deployment bar was NOT cleared.** No model — out of 450 — significantly beats the strong one-line host-range baseline (`effort_only`) on the watchlist metric (**lift@50**) under family OR genus holdout. Every contrast on lift@50 is a statistical tie. The honest ceiling holds, exactly as the first-principles ecological-ceiling argument and the lever-research (~0.33–0.40 PR) predicted.

**Real but modest progress (honest, verified):**
- The **deconfounding architecture** — fit a host-exposure base model, train the genome (ESM-15B PCA + composition) on the *residual* — gives the best honest family-holdout PR-AUC yet: **0.40** (with the host-species feature) / **0.35** fully de-entangled, up from **0.293** for 15B alone. Genus-holdout PR ~0.55–0.60.
- The genome **demonstrably adds signal on top of exposure**: `A_deconf_full` beats exposure-alone (`effort_only`) on PR (+0.10, CI>0) and ROC (+0.175, CI>0). The residual it predicts is clean (family holdout admits no relatives). This is the right way to fuse genome + ecology.
- Against a **de-entangled (host-class) baseline**, the clean genome model wins clearly (+0.18 PR, +0.29 ROC, CIs exclude 0).

**What I will NOT claim (honesty guardrails):**
- *Not* "the baseline was just an entanglement artefact." A coarse clean baseline (host-classes) is weak (PR 0.17), but switching species→classes conflates removing the +1-human tell with using a coarser feature, and the +1-human tell **cannot be cleanly removed** — every attempt recreates the collapse-to-zero leak (the de-humaning diagnostic spuriously jumped to 0.457). So the strong `effort_only` baseline stands, and the **fully-clean genome model only TIES it** (PR +0.048, CI crosses 0) — the same verdict as before.
- *Not* "we cracked generalisation." We didn't. We raised the honest number and confirmed the deconfounding lever, but did not beat the strong baseline on the metric that matters.

## Honest caveats on the run itself
- The **deepen loop was buggy**: it cycled through only 5 configs and re-ran them ~70× each, so ~8.5 h confirmed *stability* (low variance — useful, but not exploration). The genuine science was rounds A–C + ensembles in the first ~0.5 h. A smarter exploration round is the obvious next step.

## Bottom line
The genome carries real, leakage-free signal — it beats taxonomy and a coarse non-genomic baseline, and deconfounding lifts the honest PR-AUC to ~0.40 — but it still does **not** robustly beat the strongest one-line host-range baseline on a deployable watchlist under honest evaluation. We are sitting at the predicted honest ceiling. The path past it remains the one we can't build cheaply: viral×human **interaction modelling** (Bet #1) and better data — not more of the same.

## Suggested next steps (your call)
1. **Fold the verified wins into the paper**: the deconfounding result (genome adds beyond exposure; honest PR 0.29→0.40) and the 450-run robustness confirmation that nothing beats the baseline on lift@50.
2. **One smarter exploration round** (fix the deepen bug; try calibrated top-k training for lift, proper group-DRO/REx, engineered adaptation features) — but expect the ceiling to hold.
3. **Accept the ceiling** and write it up as the rigorous result it is.
