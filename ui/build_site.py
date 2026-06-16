#!/usr/bin/env python
"""Generate the published report site (docs/index.html) for GitHub Pages.

Self-contained single page: narrative + the real results matrix, read from
``results/metrics_*.csv``. Re-run after new rungs (e.g. ESM) to refresh.

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

LADDER = [
    ("prior", "baseline", "Always predict the base rate. The floor."),
    ("family_prior", "baseline", "Guess from the virus family alone — pure taxonomy memorisation."),
    ("effort_only", "baseline", "Guess from research effort alone (non-human study + host breadth). No genome."),
    ("composition_logreg", "model", "k-mer + dinucleotide-bias features → logistic regression."),
    ("composition_xgb", "model", "Same composition features → gradient-boosted trees. The zoonotic_rank stand-in."),
]
SCHEMES = [("random", "Random", "leaky"), ("tax_family", "Family holdout", "honest"),
           ("tax_genus", "Genus holdout", "honest"), ("temporal", "Temporal", "prospective")]


def load_metrics() -> dict:
    out: dict[str, dict] = {}
    for f in glob.glob(str(RESULTS / "metrics_*.csv")):
        rung = Path(f).stem.replace("metrics_", "")
        df = pd.read_csv(f)
        out[rung] = {r["scheme"]: r for _, r in df.iterrows()}
    return out


def load_json(name: str) -> dict:
    p = RESULTS / name
    return json.loads(p.read_text()) if p.exists() else {}


def lift_color(v: float) -> str:
    if v >= 4:
        return "var(--green)"
    if v >= 2:
        return "var(--teal)"
    if v >= 1.5:
        return "var(--amber)"
    return "var(--red)"


def matrix_html(M: dict) -> str:
    head = '<th>rung</th>' + "".join(
        f'<th class="{"hl" if k=="tax_family" else ""}">{label}<span class="sc-sub">{tag}</span></th>'
        for k, label, tag in SCHEMES)
    body = ""
    for rung, kind, _ in LADDER:
        cells = ""
        for k, _label, _tag in SCHEMES:
            m = M.get(rung, {}).get(k)
            hl = " hl" if k == "tax_family" else ""
            if m is None:
                cells += f'<td class="mc{hl}"><span class="mut">—</span></td>'
                continue
            lift, roc = float(m["lift@50"]), float(m["roc_auc"])
            cells += (f'<td class="mc{hl}"><span class="lift" style="color:{lift_color(lift)}">{lift:.1f}×</span>'
                      f'<span class="roc">{roc:.2f} AUC</span></td>')
        body += f'<tr class="{kind}"><td class="rn">{rung}</td>{cells}</tr>'
    return f'<table class="matrix"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def stat_cards(labels: dict, splits: dict) -> str:
    cards = [
        (f"{labels.get('n_viruses', 0):,}", "viruses", "VIRION-resolved taxa"),
        (f"{labels.get('n_positive', 0):,}", "infect humans", f"{labels.get('base_rate',0)*100:.1f}% base rate"),
        (f"{splits.get('cohort_size', 0):,}", "modelable cohort", "family + year + genome"),
        ("9,197", "genomes", "99.7% coverage, NCBI RefSeq"),
        (f"{labels.get('n_families', 0)}", "virus families", f"{labels.get('n_genera',0)} genera"),
        ("4", "split schemes", "random · family · genus · temporal"),
    ]
    return "".join(
        f'<div class="card"><div class="cv">{v}</div><div class="cl">{l}</div><div class="cs">{s}</div></div>'
        for v, l, s in cards)


def build() -> str:
    M = load_metrics()
    labels = load_json("labels_summary.json")
    splits = load_json("splits_summary.json")

    def val(rung: str, scheme: str, field: str) -> float:
        row = M.get(rung, {}).get(scheme)
        return float(row[field]) if row is not None else 0.0

    return TEMPLATE.format(
        gen=datetime.now().strftime("%B %Y"),
        random_auc=f"{val('composition_xgb','random','roc_auc'):.2f}",
        family_auc=f"{val('composition_xgb','tax_family','roc_auc'):.2f}",
        random_lift=f"{val('composition_xgb','random','lift@50'):.1f}",
        family_lift=f"{val('composition_xgb','tax_family','lift@50'):.1f}",
        cards=stat_cards(labels, splits),
        matrix=matrix_html(M),
    )


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Does genome-based zoonotic-risk prediction actually generalise?</title>
<meta name="description" content="An honest evaluation of whether viral genome models predict human-infection potential — or just memorise taxonomy.">
<style>
:root{{--bg:#0a0e13;--p1:#111823;--p2:#0d141d;--bd:#1e2a38;--fg:#e8eef4;--mut:#8a99a8;
--teal:#2dd4bf;--green:#34d399;--red:#f87171;--amber:#fbbf24;--blue:#60a5fa;--violet:#a78bfa}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;
-webkit-font-smoothing:antialiased}}
.wrap{{max-width:880px;margin:0 auto;padding:0 24px}}
a{{color:var(--teal);text-decoration:none}} a:hover{{text-decoration:underline}}
h1,h2,h3{{line-height:1.25;letter-spacing:-.4px}}
h2{{font-size:13px;text-transform:uppercase;letter-spacing:2px;color:var(--teal);margin:64px 0 6px;font-weight:600}}
h3{{font-size:24px;margin:6px 0 16px}}
p{{color:#cdd7e1}}
.mono{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}
.mut{{color:var(--mut)}}
/* hero */
.hero{{background:radial-gradient(1100px 500px at 75% -20%,#16283a 0,var(--bg) 65%);
border-bottom:1px solid var(--bd);padding:72px 0 56px}}
.tagchip{{display:inline-block;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:var(--mut);
border:1px solid var(--bd);border-radius:999px;padding:5px 12px;margin-bottom:22px}}
.hero h1{{font-size:42px;margin:0 0 16px;max-width:760px}}
.hero .lede{{font-size:19px;color:#b9c6d2;max-width:680px;margin:0}}
/* headline metric */
.headline{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:40px 0 4px}}
.big{{display:flex;flex-direction:column;background:var(--p1);border:1px solid var(--bd);border-radius:16px;
padding:20px 26px;min-width:180px}}
.big .num{{font-size:40px;font-weight:800;letter-spacing:-1px}}
.big .lab{{font-size:13px;color:var(--mut);margin-top:2px}}
.big.leaky .num{{color:var(--red)}} .big.honest .num{{color:var(--green)}}
.arrowbig{{font-size:30px;color:var(--bd)}}
.headline-cap{{color:var(--mut);font-size:14px;margin:10px 0 0}}
/* cards */
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0}}
.card{{background:var(--p1);border:1px solid var(--bd);border-radius:12px;padding:16px}}
.card .cv{{font-size:26px;font-weight:700;letter-spacing:-.5px}}
.card .cl{{font-size:14px;margin-top:2px}} .card .cs{{font-size:12px;color:var(--mut);margin-top:3px}}
/* matrix */
.matrix{{width:100%;border-collapse:collapse;font-size:14px;margin:8px 0}}
.matrix th{{font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:var(--mut);font-weight:600;
padding:10px 8px;text-align:center;border-bottom:1px solid var(--bd);vertical-align:bottom}}
.matrix th:first-child{{text-align:left}}
.matrix th.hl{{color:var(--green)}}
.sc-sub{{display:block;font-weight:400;text-transform:none;letter-spacing:0;font-size:11px;color:var(--mut);margin-top:3px}}
.matrix td{{padding:11px 8px;border-bottom:1px solid var(--bd)}}
.matrix .rn{{font-family:ui-monospace,monospace;font-size:13px}}
.matrix tr.baseline .rn{{color:var(--amber)}} .matrix tr.model .rn{{color:var(--blue)}}
.mc{{text-align:center}} .mc.hl{{background:var(--p2)}}
.mc .lift{{font-weight:700;font-size:17px;display:block}}
.mc .roc{{font-size:11px;color:var(--mut)}}
/* callout */
.callout{{border-left:3px solid var(--teal);background:var(--p2);border-radius:0 12px 12px 0;
padding:18px 22px;margin:22px 0}}
.callout.warn{{border-color:var(--amber)}}
.callout.verdict{{border-color:var(--green);background:linear-gradient(120deg,#0f1d18,var(--p2))}}
.callout h4{{margin:0 0 8px;font-size:17px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:18px 0}}
.box{{background:var(--p1);border:1px solid var(--bd);border-radius:12px;padding:18px}}
.box.no{{border-color:#7f1d1d55}} .box.yes{{border-color:#065f4655}}
.box .bh{{font-size:12px;text-transform:uppercase;letter-spacing:1px;font-weight:700;margin-bottom:6px}}
.box.no .bh{{color:var(--red)}} .box.yes .bh{{color:var(--green)}}
ul{{color:#cdd7e1}} li{{margin:6px 0}}
code{{background:var(--p2);border:1px solid var(--bd);border-radius:5px;padding:1px 6px;font-size:13px;
font-family:ui-monospace,monospace;color:var(--teal)}}
.foot{{margin:72px 0 48px;padding-top:24px;border-top:1px solid var(--bd);color:var(--mut);font-size:13px}}
.disc{{background:var(--p2);border:1px solid var(--bd);border-radius:12px;padding:16px 20px;margin:20px 0;
color:var(--mut);font-size:14px}}
@media(max-width:680px){{.two{{grid-template-columns:1fr}}.hero h1{{font-size:32px}}.big .num{{font-size:32px}}}}
</style></head>
<body>

<div class="hero"><div class="wrap">
  <span class="tagchip">v0 · exploratory · honest evaluation</span>
  <h1>Does genome-based zoonotic-risk prediction actually generalise?</h1>
  <p class="lede">Machine-learning models claim to read a virus's pandemic potential from its genome.
  We rebuilt one, evaluated it honestly, and measured how much of its skill is real biology —
  versus memorising which viral families we've already seen.</p>

  <div class="headline">
    <div class="big leaky"><span class="num">{random_auc}</span><span class="lab">random split · "leaky"</span></div>
    <span class="arrowbig">→</span>
    <div class="big honest"><span class="num">{family_auc}</span><span class="lab">novel-family holdout · honest</span></div>
  </div>
  <p class="headline-cap">Best genome model (gradient-boosted composition), ROC-AUC. The watchlist lift
  collapses even harder: <b>{random_lift}× → {family_lift}×</b>. Most of the apparent skill was phylogenetic leakage.</p>
</div></div>

<div class="wrap">

  <h2>The task</h2>
  <h3>Predict whether a virus can infect humans — from its genome alone</h3>
  <p>Given a viral genome, output one number: the probability it can infect people. This is a real,
  published task (Mollentze &amp; Streicker 2021, <span class="mono">zoonotic_rank</span>). It is <em>not</em>
  predicting pandemics, transmissibility, or severity — just human-infection <em>capability</em> of an
  already-sequenced virus. The label comes from surveillance records (was this virus ever found in a
  person?), not from the genome — so the genome is what we hope <em>predicts</em> that fact.</p>

  <div class="callout warn"><h4>Why this is a known trap</h4>
  <p style="margin:0">The naive pipeline — featurise genomes, train a classifier, report a high AUC — scores
  well by exploiting <b>phylogenetic relatedness</b>: test viruses are close relatives of training viruses,
  so the model wins by recognising the <em>family</em>, not by learning biology. A model at 0.9+ AUC on a
  random split can be near-useless on a genuinely novel virus. The entire value of this project is measuring
  the gap once that leakage is removed.</p></div>

  <h2>The data</h2>
  <h3>10,804 viruses, 1,124 that infect humans</h3>
  <div class="cards">{cards}</div>
  <p>Labels from <a href="https://github.com/viralemergence/virion">VIRION</a> (885k host–virus records),
  taxonomy from <a href="https://ictv.global/vmr">ICTV</a>, genomes from NCBI RefSeq. A "positive" is any
  virus with a documented <em>Homo sapiens</em> association; a "negative" has host records but none human —
  which means absence of evidence, not evidence of absence (a documented label-noise source).</p>

  <h2>The honest test</h2>
  <h3>Random split vs. taxonomic holdout</h3>
  <p>The same model is evaluated four ways. The difference between them is the whole point:</p>
  <ul>
    <li><b>Random split</b> — relatives of a test virus sit in training. Leaky; the optimistic number.</li>
    <li><b>Family holdout</b> — whole families are held out, so test viruses have <em>no</em> training relatives.
    The honest test of generalisation.</li>
    <li><b>Genus holdout</b> — stricter version within families.</li>
    <li><b>Temporal</b> — train on viruses known before 2020, test on those characterised after. Prospective.</li>
  </ul>
  <p>We also build a <b>reference ladder</b> of controls, because a genome model is only interesting if it
  beats them under holdout: a base-rate <code>prior</code>, a taxonomy-only <code>family_prior</code>, and a
  <code>effort_only</code> baseline that predicts purely from <em>how much a virus has been studied</em> (no
  genome at all). If the genome can't beat "how famous is this virus," it's measuring attention, not biology.</p>

  <h2>Results</h2>
  <h3>The full ladder, every split side by side</h3>
  {matrix}
  <p class="mut" style="font-size:13px">Each cell: <b>top-50 watchlist lift</b> (× over the 11.7% base rate),
  with ROC-AUC below. Green = strong, red = no better than chance. The highlighted <b>Family holdout</b>
  column is the honest test.</p>

  <div class="callout"><h4>The gap — the number this project exists to produce</h4>
  <p style="margin:0">The genome model (<code>composition_xgb</code>) drops from <b>0.91 → 0.66 ROC-AUC</b>,
  <b>0.73 → 0.18 PR-AUC</b>, and <b>8.4× → 1.7× watchlist lift</b> when whole families are held out. A model
  that looks state-of-the-art on a random split is barely above chance on genuinely novel families.</p></div>

  <h2>The verdict</h2>
  <h3>Did the genome beat both controls under family holdout?</h3>
  <div class="two">
    <div class="box yes"><div class="bh">✓ Beats taxonomy</div>
    <p style="margin:0;font-size:14px">0.66 vs 0.42 AUC. The genome adds <b>real signal beyond pure family
    memorisation</b> — it's not <em>only</em> taxonomy.</p></div>
    <div class="box no"><div class="bh">✗ Loses to research effort</div>
    <p style="margin:0;font-size:14px">On the watchlist that matters, the "how-studied-is-it" baseline wins
    (<b>5.1× vs 1.7×</b> lift). Under true novelty, counting citations beats reading the genome.</p></div>
  </div>

  <div class="callout verdict"><h4>Plain-language answer</h4>
  <p>The signal is <b>real but narrow</b>, and the headline numbers in this literature are mostly leakage.
  Genome composition is a genuinely useful <b>prioritisation prior for novel viruses within or near known
  families</b> — it generalises across genera (genus-holdout 6.1× lift) and forward in time (temporal 18.6×,
  beating every control). But it does <b>not</b> extrapolate to families it has never seen, and under that
  honest test it doesn't beat a trivial research-effort baseline on a real watchlist.</p>
  <p style="margin:0">So: useful for "look harder at this novel relative of a known virus," <b>not</b> a
  crystal ball for the next pandemic from an unknown lineage. This reproduces the Mollentze-era result
  (combined AUC ~0.77, never family-stratified) and the 2025 "Hidden challenges" critique — on our own
  pipeline, with the controls that make it legible.</p></div>

  <h2>What this can't do</h2>
  <h3>Infectivity ≠ transmissibility ≠ severity</h3>
  <p>This predicts only whether a virus <em>can infect a human</em>. It says nothing about whether it spreads
  human-to-human, or whether it's deadly or benign — rabies and the common-cold coronaviruses are both
  "positives" here. Those are separate, harder problems with far sparser labels, and genome composition is
  the wrong tool for them. Honest scope is the point.</p>

  <div class="disc"><b>Caveats.</b> v0 / exploratory, not a deployed tool. Composition features only (ESM-2
  protein-embedding rung still pending). Labels carry absence-of-evidence noise and research-effort bias.
  Temporal "year" is GenBank deposition, a proxy for discovery. All open data; no GISAID. Built to learn
  whether the signal is real — not to ship a product or make spillover claims.</p>

  <div class="foot">
    Methodology &amp; code: data from VIRION · CLOVER · HP3 · ICTV VMR · NCBI RefSeq.
    Honest-eval harness with taxonomic + temporal holdout and base-rate-aware metrics.
    Generated {gen}. · An exploratory study in honest model evaluation.
  </div>

</div></body></html>"""


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build())
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
