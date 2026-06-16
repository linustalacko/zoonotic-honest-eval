"""Control estimators that aren't standard feature-vector models.

``GroupRateClassifier`` is the **taxonomy-memorisation control**: it predicts a
virus's human-infection probability as the *training* base rate of its group
(family). It is the formal statement of "guess from taxonomy alone."

Why it matters: under a **family holdout** split, every test family is absent
from training, so the classifier falls back to the global base rate and
collapses to the ``prior``. That collapse *is* the leakage demonstration — any
genome model worth keeping must beat this under holdout.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin


class GroupRateClassifier(BaseEstimator, ClassifierMixin):
    """Predict P(y=1) = smoothed training positive-rate of the row's group.

    Expects a single-column X holding the group key (e.g. family). Unseen groups
    fall back to the global training rate. Smoothing shrinks small groups toward
    the global rate so a 1-virus family doesn't predict 0 or 1 outright.
    """

    def __init__(self, smoothing: float = 5.0):
        self.smoothing = smoothing

    def fit(self, X, y):
        groups = np.asarray(X)[:, 0]
        y = np.asarray(y).astype(float)
        self.global_rate_ = float(y.mean()) if len(y) else 0.0
        g = pd.Series(y).groupby(groups)
        cnt, pos = g.count(), g.sum()
        self.rates_ = {
            grp: float((pos[grp] + self.smoothing * self.global_rate_) / (cnt[grp] + self.smoothing))
            for grp in cnt.index
        }
        self.classes_ = np.array([0, 1])
        return self

    def predict_proba(self, X):
        groups = np.asarray(X)[:, 0]
        p = np.array([self.rates_.get(grp, self.global_rate_) for grp in groups], dtype=float)
        return np.column_stack([1.0 - p, p])

    def predict(self, X):
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)
