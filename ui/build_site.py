#!/usr/bin/env python
"""Generate the published report site (docs/index.html) for GitHub Pages.

Monochrome, Helvetica, everything a multiple of 4. Self-contained single page,
data read from results/metrics_*.csv. Re-run after new rungs to refresh.

    python ui/build_site.py    # -> docs/index.html
"""

from __future__ import annotations

import glob
import json
from datetime import datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
OUT = ROOT / "docs" / "index.html"

# (rung key, friendly label) — friendly labels keep the table readable.
LADDER = [
    ("prior", "base rate"),
    ("family_prior", "taxonomy only"),
    ("effort_only", "research effort"),
    ("composition_logreg", "genome · linear"),
    ("composition_xgb", "genome · boosted"),
]
SCHEMES = [("random", "Random"), ("tax_family", "Family holdout"),
           ("tax_genus", "Genus holdout"), ("temporal", "Temporal")]


def load_metrics() -> dict:
    out: dict[str, dict] = {}
    for f in glob.glob(str(RESULTS / "metrics_*.csv")):
        rung = Path(f).stem.replace("metrics_", "")
        out[rung] = {r["scheme"]: r for _, r in pd.read_csv(f).iterrows()}
    return out


def load_json(name: str) -> dict:
    p = RESULTS / name
    return json.loads(p.read_text()) if p.exists() else {}


def matrix_html(M: dict) -> str:
    head = "<th>model</th>" + "".join(
        f'<th class="{"hon" if k=="tax_family" else ""}">{lab}</th>' for k, lab in SCHEMES)
    body = ""
    for rung, label in LADDER:
        cells = ""
        for k, _ in SCHEMES:
            hon = " hon" if k == "tax_family" else ""
            m = M.get(rung, {}).get(k)
            if m is None:
                cells += f'<td class="{hon.strip()}">&mdash;</td>'.replace("&mdash;", "·")
                continue
            lift, roc = float(m["lift@50"]), float(m["roc_auc"])
            cells += (f'<td class="{hon.strip()}"><span class="big">{lift:.1f}&times;</span>'
                      f'<span class="sml">{roc:.2f}</span></td>')
        body += f'<tr><td class="name">{label}</td>{cells}</tr>'
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def build() -> str:
    M = load_metrics()
    labels = load_json("labels_summary.json")
    splits = load_json("splits_summary.json")
    genomes = load_json("genomes_summary.json")
    g_found = genomes.get("found", 0)
    g_tgt = genomes.get("targets", splits.get("cohort_size", 1)) or 1
    g_cov = genomes.get("coverage") or (g_found / g_tgt)

    def val(rung, scheme, field):
        row = M.get(rung, {}).get(scheme)
        return float(row[field]) if row is not None else 0.0

    return TEMPLATE.format(
        random_auc=f"{val('composition_xgb','random','roc_auc'):.2f}",
        family_auc=f"{val('composition_xgb','tax_family','roc_auc'):.2f}",
        random_lift=f"{val('composition_xgb','random','lift@50'):.1f}",
        family_lift=f"{val('composition_xgb','tax_family','lift@50'):.1f}",
        n_viruses=f"{labels.get('n_viruses',0):,}",
        n_pos=f"{labels.get('n_positive',0):,}",
        base=f"{labels.get('base_rate',0)*100:.0f}",
        cohort=f"{splits.get('cohort_size',0):,}",
        n_fam=labels.get("n_families", 0),
        n_gen=labels.get("n_genera", 0),
        genomes_found=f"{g_found:,}",
        genomes_cov=f"{g_cov*100:.1f}",
        matrix=matrix_html(M),
        gen=datetime.now().strftime("%B %Y"),
    )


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Does genome-based zoonotic prediction generalise?</title>
<meta name="description" content="An honest evaluation of whether viral genome models predict human-infection potential, or just memorise taxonomy.">
<style>
/* every value here is a multiple of 4 */
body{{background:#fff;color:#000;margin:0;padding:32px;font-size:16px;line-height:24px;
font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:720px;margin:0 auto}}
h1{{font-size:32px;line-height:40px;margin:0 0 8px;letter-spacing:-0.4px}}
h2{{font-size:20px;line-height:28px;margin:48px 0 12px}}
p{{margin:0 0 20px}}
a{{color:#000}}
.sub{{color:#666;margin:0 0 40px}}
.headline{{display:flex;align-items:baseline;gap:16px;margin:0 0 12px}}
.num{{font-size:64px;line-height:64px;font-weight:700;letter-spacing:-2px}}
.arrow{{font-size:32px;color:#999}}
.cap{{color:#666;margin:0 0 40px}}
.facts{{list-style:none;padding:0;margin:0 0 20px;border-top:1px solid #e4e4e4}}
.facts li{{display:flex;justify-content:space-between;gap:16px;padding:8px 0;
border-bottom:1px solid #e4e4e4}}
.facts .k{{color:#666}} .facts .v{{font-weight:700}}
.tablewrap{{overflow-x:auto;margin:0 0 12px}}
table{{width:100%;border-collapse:collapse;font-size:16px;line-height:20px}}
th,td{{padding:12px 8px;text-align:center;border-bottom:1px solid #e4e4e4;white-space:nowrap}}
th{{font-size:12px;line-height:16px;color:#666;font-weight:400;border-bottom:1px solid #000;vertical-align:bottom}}
th:first-child,td:first-child{{text-align:left}}
th.hon{{color:#000;font-weight:700}} td.hon{{background:#f4f4f4}}
td.name{{color:#666}}
.big{{display:block;font-weight:700;font-size:20px;line-height:24px}}
.sml{{display:block;font-size:12px;line-height:16px;color:#666}}
.keyline{{font-weight:700}}
.foot{{margin:48px 0 0;padding:16px 0 0;border-top:1px solid #000;color:#666;font-size:12px;line-height:20px}}
.foot a{{color:#666}}
@media(max-width:480px){{.num{{font-size:48px;line-height:48px}}}}
</style></head>
<body><div class="wrap">

<h1>Does genome-based zoonotic prediction generalise?</h1>
<p class="sub">An honest evaluation of whether a virus's genome predicts its potential
to infect humans, or whether the model just memorises which families we've already seen.</p>

<div class="headline">
<span class="num">{random_auc}</span><span class="arrow">&rarr;</span><span class="num">{family_auc}</span>
</div>
<p class="cap">Best genome model (boosted composition), ROC-AUC: random split &rarr; novel-family
holdout. The watchlist signal collapses harder, {random_lift}&times; &rarr; {family_lift}&times;.
Most of the apparent skill was phylogenetic leakage.</p>

<h2>The task</h2>
<p>Given a viral genome, predict whether it can infect humans. This is a real, published
task (Mollentze &amp; Streicker, 2021). The label comes from surveillance records, not the
genome, so the genome is what we hope predicts it. It is not predicting pandemics,
transmissibility, or severity, only human-infection capability.</p>

<h2>The trap</h2>
<p>The naive version trains on random splits and reports a high score. But test viruses are
close relatives of training viruses, so the model wins by recognising the family, not by
learning biology. A model at 0.9 on a random split can be near-useless on a genuinely novel
virus. The whole point is to measure the gap once that leakage is removed.</p>

<h2>The data</h2>
<ul class="facts">
<li><span class="k">Viruses (VIRION)</span><span class="v">{n_viruses}</span></li>
<li><span class="k">Infect humans</span><span class="v">{n_pos} ({base}%)</span></li>
<li><span class="k">Modelable cohort</span><span class="v">{cohort}</span></li>
<li><span class="k">Genomes fetched</span><span class="v">{genomes_found} ({genomes_cov}%)</span></li>
<li><span class="k">Families / genera</span><span class="v">{n_fam} / {n_gen}</span></li>
</ul>

<h2>The test</h2>
<p>The same model is evaluated four ways. <b>Random</b> leaks relatives into training.
<b>Family holdout</b> removes whole families, so test viruses have no training relatives,
the honest test. <b>Genus holdout</b> is stricter within families. <b>Temporal</b> trains
on viruses known before 2020 and tests on later ones. We also build controls: a base-rate
floor, a taxonomy-only guess, and a research-effort baseline that uses no genome at all.
A genome model is only interesting if it beats those under family holdout.</p>

<h2>Results</h2>
<div class="tablewrap">{matrix}</div>
<p class="cap">Each cell: top-50 watchlist lift over the base rate, with ROC-AUC below.
The shaded <b>Family holdout</b> column is the honest test.</p>

<h2>The gap</h2>
<p>The genome model drops from <b>{random_auc} to {family_auc}</b> ROC-AUC, and its watchlist
from <b>{random_lift}&times; to {family_lift}&times;</b>, when whole families are held out.
A model that looks state-of-the-art on a random split is barely above chance on novel families,
and its watchlist is beaten by simply counting how much a virus has been studied.</p>

<h2>The verdict</h2>
<p class="keyline">The signal is real but narrow, and the headline numbers in this literature
are mostly leakage.</p>
<p>Genome composition beats pure taxonomy under family holdout, so it learns something real.
But it loses the watchlist to a research-effort baseline, and it does not extrapolate to
families it has never seen. It does generalise across genera within known families, and
forward in time. So it is a useful prioritisation prior for novel relatives of known viruses,
not a crystal ball for the next pandemic from an unknown lineage. This reproduces the
Mollentze-era result and the 2025 "hidden challenges" critique, on our own pipeline, with the
controls that make it legible.</p>

<h2>What it cannot do</h2>
<p>This predicts only whether a virus can infect a human. It says nothing about whether it
spreads between humans, or whether it is deadly or harmless. Rabies and the common cold are
both positives here. Those are separate, harder problems with far sparser data.</p>

<div class="foot">
v0, exploratory. Composition features only; the protein-embedding model is pending. Open data
only (VIRION, CLOVER, HP3, ICTV, NCBI RefSeq); no GISAID. Built to learn whether the signal is
real, not to ship a product. Code and full findings:
<a href="https://github.com/linustalacko/zoonotic-honest-eval">github.com/linustalacko/zoonotic-honest-eval</a>.
Generated {gen}.
</div>

</div></body></html>"""


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build())
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
