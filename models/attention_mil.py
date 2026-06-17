"""Trainable attention pooling (gated attention-MIL) over per-protein ESM embeddings.

The current pipeline pools a virus's proteins with a fixed mean+max. This learns,
instead, an attention weight per protein — so the model can focus on the one
protein that carries the host-jump signal (e.g. the spike) instead of averaging it
away among housekeeping proteins. This is the Ilse et al. (2018) gated-attention MIL
head that EvoMIL uses.

Question: does *learned* pooling beat fixed mean/max at the same model scale (650M)
under honest family holdout? (Prior: a small gain at best — max-pooling already
grabs the most-distinctive protein.)

    uv run python -m models.attention_mil

Reads per-protein embeddings (one row per virus×protein) from the Volume-pulled
parquet, trains per family-holdout fold, writes standard OOF preds
(results/preds_attn650M_<scheme>.parquet) so the family-clustered bootstrap scores
it against the mean/max baseline (esm650M_xgboost) and the host-range baseline.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from models.dataset import load_labels, load_splits
from models.evaluate import RESULTS_DIR, compare_rungs, score_predictions

log = logging.getLogger("zoonotic.attn_mil")
SEED = 0
MAXP = 8
PERPROTEIN = "data/features_cache/esm_esm2_t33_650M_UR50D_top8_perprotein.parquet"
TAG = "attn650M"
SCHEMES = ("random", "tax_family")


def load_bags():
    """Return dict virus_taxhash -> np.array[n_prot, dim], plus dim."""
    df = pd.read_parquet(PERPROTEIN)
    ecols = sorted([c for c in df.columns if c.startswith("e")], key=lambda c: int(c[1:]))
    dim = len(ecols)
    bags = {}
    for vh, g in df.sort_values("prot_idx").groupby("virus_taxhash"):
        bags[vh] = g[ecols].to_numpy(dtype=np.float32)[:MAXP]
    log.info("loaded %d bags, dim=%d", len(bags), dim)
    return bags, dim


def _pad(bag_list):
    """Stack variable-length bags -> (X[N,MAXP,D], mask[N,MAXP])."""
    n, d = len(bag_list), bag_list[0].shape[1]
    X = np.zeros((n, MAXP, d), dtype=np.float32)
    M = np.zeros((n, MAXP), dtype=bool)
    for i, b in enumerate(bag_list):
        k = min(len(b), MAXP)
        X[i, :k] = b[:k]
        M[i, :k] = True
    return X, M


def _make_model(dim):
    import torch.nn as nn

    class GatedAttnMIL(nn.Module):
        def __init__(self, d, h=128, c=64, p=0.4):
            super().__init__()
            self.V = nn.Linear(d, h)
            self.U = nn.Linear(d, h)
            self.w = nn.Linear(h, 1)
            self.clf = nn.Sequential(nn.Linear(d, c), nn.ReLU(), nn.Dropout(p), nn.Linear(c, 1))

        def forward(self, x, mask):  # x:[B,P,D] mask:[B,P]
            import torch
            a = self.w(torch.tanh(self.V(x)) * torch.sigmoid(self.U(x))).squeeze(-1)  # [B,P]
            a = a.masked_fill(~mask, float("-inf"))
            a = torch.softmax(a, dim=1).unsqueeze(-1)  # [B,P,1]
            z = (a * x).sum(1)  # [B,D]
            return self.clf(z).squeeze(-1)  # [B]

    return GatedAttnMIL(dim)


def _train_predict(Xtr, Mtr, ytr, Xte, Mte, dim, epochs=40, bs=256):
    import torch
    from sklearn.preprocessing import StandardScaler

    torch.manual_seed(SEED)
    np.random.seed(SEED)
    # standardise on real (unmasked) training proteins
    sc = StandardScaler().fit(Xtr[Mtr])
    Xtr = (Xtr - sc.mean_) / (sc.scale_ + 1e-9) * Mtr[..., None]
    Xte = (Xte - sc.mean_) / (sc.scale_ + 1e-9) * Mte[..., None]

    model = _make_model(dim)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
    pos_w = torch.tensor([(ytr == 0).sum() / max((ytr == 1).sum(), 1)], dtype=torch.float32)
    lossf = torch.nn.BCEWithLogitsLoss(pos_weight=pos_w)

    Xt = torch.from_numpy(Xtr)
    Mt = torch.from_numpy(Mtr)
    yt = torch.from_numpy(ytr.astype(np.float32))
    n = len(yt)
    model.train()
    for _ in range(epochs):
        perm = torch.randperm(n)
        for i in range(0, n, bs):
            idx = perm[i:i + bs]
            opt.zero_grad()
            out = model(Xt[idx], Mt[idx])
            loss = lossf(out, yt[idx])
            loss.backward()
            opt.step()
    model.eval()
    with torch.no_grad():
        logits = model(torch.from_numpy(Xte), torch.from_numpy(Mte))
        return torch.sigmoid(logits).numpy()


def run():
    from zoonotic.logging_utils import setup_logging
    setup_logging()
    bags, dim = load_bags()
    lab = load_labels().set_index("virus_taxhash")
    spl = load_splits().set_index("virus_taxhash")
    idx = [v for v in bags if v in lab.index and v in spl.index]
    log.info("cohort with bags+labels+splits: %d", len(idx))
    y = lab.loc[idx, "label"].astype(int).to_numpy()
    fam = lab.loc[idx, "family"].fillna("NA").to_numpy()
    pos = {v: i for i, v in enumerate(idx)}

    for scheme in SCHEMES:
        col = {"random": "random_fold", "tax_family": "tax_family_fold"}[scheme]
        folds = spl.loc[idx, col]
        oof_v, oof_s, oof_f = [], [], []
        for k in sorted(folds.dropna().unique()):
            te_mask = (folds == k).fillna(False).to_numpy()
            tr_mask = folds.notna().to_numpy() & ~te_mask
            tr_i = np.where(tr_mask)[0]
            te_i = np.where(te_mask)[0]
            Xtr, Mtr = _pad([bags[idx[i]] for i in tr_i])
            Xte, Mte = _pad([bags[idx[i]] for i in te_i])
            s = _train_predict(Xtr, Mtr, y[tr_i], Xte, Mte, dim)
            oof_v.extend([idx[i] for i in te_i])
            oof_s.extend(s.tolist())
            oof_f.extend([int(k)] * len(te_i))
        oof = pd.DataFrame({"virus_taxhash": oof_v, "y_true": y[[pos[v] for v in oof_v]].astype(int),
                            "y_score": oof_s, "fold": oof_f,
                            "family": fam[[pos[v] for v in oof_v]]})
        oof.to_parquet(RESULTS_DIR / f"preds_{TAG}_{scheme}.parquet")
        m = score_predictions(oof["y_true"].to_numpy(), oof["y_score"].to_numpy())
        log.info("[%s] %-11s ROC=%.3f PR=%.3f lift@50=%.2f", TAG, scheme,
                 m.get("roc_auc", float("nan")), m.get("pr_auc", float("nan")), m.get("lift@50", float("nan")))

    print("\n=== attention-MIL vs mean/max baseline (650M) and host-range, family holdout ===")
    for base in ("esm650M_xgboost", "effort_only"):
        try:
            c = compare_rungs(TAG, base, "tax_family", metrics=("roc_auc", "pr_auc", "lift@50"))
            seg = "; ".join(f"{m} {d['point']:+.3f}[{d['ci_lo']:+.3f},{d['ci_hi']:+.3f}]"
                            f"{'BEATS' if d['ci_lo']>0 else ('loses' if d['ci_hi']<0 else 'ties')}"
                            for m, d in c.items())
            print(f"{TAG} - {base}: {seg}")
        except Exception as exc:  # noqa: BLE001
            print(f"{TAG} vs {base}: ERR {str(exc)[:100]}")


if __name__ == "__main__":
    run()
