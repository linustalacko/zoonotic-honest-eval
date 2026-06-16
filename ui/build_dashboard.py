#!/usr/bin/env python
"""Generate a self-contained dashboard for the zoonotic pipeline.

Reads the small JSON summaries (+ any ``metrics_*.csv``) from ``results/`` and
writes a single standalone ``ui/dashboard.html`` — no server, no CDN, no build
step. Open it in a browser, or re-run after each training run to refresh.

    python ui/build_dashboard.py            # -> ui/dashboard.html

It visualizes three things: how the pipeline fits together, *the* honest-eval
question (random vs taxonomic holdout), and the results once models have run.
"""

from __future__ import annotations

import glob
import json
from datetime import datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
OUT = ROOT / "ui" / "dashboard.html"


def _load(name: str) -> dict:
    p = RESULTS / name
    return json.loads(p.read_text()) if p.exists() else {}


def _metrics() -> pd.DataFrame:
    frames = []
    for f in sorted(glob.glob(str(RESULTS / "metrics_*.csv"))):
        df = pd.read_csv(f)
        df["model"] = Path(f).stem.replace("metrics_", "")
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


# --------------------------------------------------------------------------- #
# component renderers
# --------------------------------------------------------------------------- #
def pct(x: float) -> str:
    return f"{x*100:.1f}%"


def stat_card(value, label, sub="") -> str:
    sub_html = f'<div class="sub">{sub}</div>' if sub else ""
    return f'<div class="card"><div class="val">{value}</div><div class="lbl">{label}</div>{sub_html}</div>'


def pipeline_flow(status: dict) -> str:
    nodes = []
    for s in status.get("stages", []):
        state = s["state"]
        extra = ""
        if s.get("target"):
            done, tgt = s.get("done", 0), s["target"]
            extra = f'<div class="prog"><span style="width:{min(100,done/tgt*100):.0f}%"></span></div><div class="sub">{done:,}/{tgt:,}</div>'
        nodes.append(
            f'<div class="node {state}">'
            f'<div class="dot"></div>'
            f'<div class="nlabel">{s["label"]}</div>'
            f'<div class="ndetail">{s["detail"]}</div>{extra}</div>'
        )
    arrow = '<div class="arrow">→</div>'
    return arrow.join(nodes)


def honest_eval_panel(splits: dict) -> str:
    rfold = splits.get("positives_per_random_fold", {})
    ffold = splits.get("positives_per_family_fold", {})
    maxv = max([*rfold.values(), *ffold.values()], default=1)

    def bars(d, cls):
        return "".join(
            f'<div class="bwrap"><div class="bar {cls}" style="height:{v/maxv*100:.0f}%" title="fold {k}: {v} positives"></div><div class="bx">{k}</div></div>'
            for k, v in d.items()
        )

    return f"""
    <div class="split-grid">
      <div class="split-card leaky">
        <div class="tag">RANDOM SPLIT · leaky</div>
        <p>Relatives of a test virus sit in the training set. The model can win by
        recognising the <em>family</em>, not the biology. Positives spread evenly
        across folds:</p>
        <div class="bars">{bars(rfold, "leaky")}</div>
        <div class="caption">positives per fold — flat (216 each)</div>
      </div>
      <div class="split-card honest">
        <div class="tag">FAMILY HOLDOUT · honest</div>
        <p>Whole families are held out, so test viruses have <em>no</em> training
        relatives. This is the real test of generalisation. Positives clump,
        because they cluster in a few families:</p>
        <div class="bars">{bars(ffold, "honest")}</div>
        <div class="caption">positives per fold — lumpy (167–395)</div>
      </div>
    </div>
    <div class="thesis">The headline of the whole project is the <b>gap</b> between these two
    columns once models run. A large drop = the model was memorising taxonomy.</div>
    """


LADDER = [
    ("prior", "Constant = base rate", "The floor any model must beat.", "baseline"),
    ("family_prior", "Score = family's training human-rate", "Pure taxonomy memorisation. Collapses to the prior under family holdout — the leakage demo.", "baseline"),
    ("effort_only", "cites · #associations · #sequences", "Research-effort control. Beat this under holdout or the model tracks study bias, not biology.", "baseline"),
    ("composition + logreg", "k-mer + dinucleotide-bias → linear", "Is there <em>linear</em> compositional signal?", "model"),
    ("composition + xgboost", "same features → gradient boosting", "Non-linear composition; the zoonotic_rank stand-in.", "model"),
    ("ESM-2 + classifier", "protein-LM embeddings of ORFs", "Must <em>shrink the family-holdout gap</em> vs composition to earn its place.", "model"),
]


def ladder_panel() -> str:
    rows = ""
    for i, (name, how, tests, kind) in enumerate(LADDER):
        rows += (
            f'<div class="rung {kind}"><div class="rn">{i}</div>'
            f'<div class="rbody"><div class="rname">{name}</div>'
            f'<div class="rhow">{how}</div><div class="rtests">{tests}</div></div></div>'
        )
    return rows


LADDER_ORDER = ["prior", "family_prior", "effort_only",
                "composition_logreg", "composition_xgb", "esm_logreg"]
SCHEME_ORDER = ["random", "tax_family", "tax_genus", "temporal"]
SCHEME_LABEL = {"random": "Random", "tax_family": "Family holdout",
                "tax_genus": "Genus holdout", "temporal": "Temporal"}


def _lift_color(lift: float) -> str:
    if lift >= 4:
        return "var(--green)"
    if lift >= 2:
        return "var(--teal)"
    if lift >= 1.5:
        return "var(--amber)"
    return "var(--red)"


def results_panel(metrics: pd.DataFrame) -> str:
    if metrics.empty:
        return """
        <div class="empty">
          <div class="eicon">▱▱▱</div>
          <div>No model has run yet. Once training completes, this fills with
          watchlist lift / ROC-AUC for every split — with the
          <b>random → family-holdout gap</b> front and centre.</div>
        </div>"""

    done = set(metrics["model"])
    present = [r for r in LADDER_ORDER if r in done]
    pending = [r for r in LADDER_ORDER if r not in done]

    def cell(model: str, scheme: str) -> str:
        row = metrics[(metrics["model"] == model) & (metrics["scheme"] == scheme)]
        if not len(row):
            return '<td class="mc"><span class="mut">—</span></td>'
        r = row.iloc[0]
        lift, roc = float(r["lift@50"]), float(r["roc_auc"])
        hl = ' style="background:var(--panel)"' if scheme == "tax_family" else ""
        return (f'<td class="mc"{hl}><span class="lift" style="color:{_lift_color(lift)}">{lift:.1f}×</span>'
                f'<span class="roc">{roc:.2f}</span></td>')

    head = '<th>rung</th>' + "".join(
        f'<th class="{"hl" if s=="tax_family" else ""}">{SCHEME_LABEL[s]}</th>' for s in SCHEME_ORDER)
    body = ""
    for rung in present:
        kind = "baseline" if rung in ("prior", "family_prior", "effort_only") else "model"
        body += (f'<tr class="{kind}"><td class="rn-name">{rung}</td>'
                 + "".join(cell(rung, s) for s in SCHEME_ORDER) + "</tr>")
    for rung in pending:
        body += (f'<tr class="pend"><td class="rn-name">{rung}</td>'
                 f'<td class="mc" colspan="4"><span class="mut">awaiting genomes → features</span></td></tr>')

    note = ('<div class="rcap">Cells: <b>top-50 watchlist lift</b> (× over base rate) · '
            'ROC-AUC below. <b>Family holdout</b> is the honest test. A rung is only '
            'interesting if it beats <span class="mono">family_prior</span> AND '
            '<span class="mono">effort_only</span> there.</div>')
    return (f'<table class="resmatrix"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>{note}')


# --------------------------------------------------------------------------- #
# assembly
# --------------------------------------------------------------------------- #
def build() -> str:
    labels = _load("labels_summary.json")
    splits = _load("splits_summary.json")
    status = _load("pipeline_status.json")
    metrics = _metrics()

    base = labels.get("base_rate", 0)
    cards = "".join([
        stat_card(f"{labels.get('n_viruses', 0):,}", "viruses", "VIRION-resolved taxa"),
        stat_card(f"{labels.get('n_positive', 0):,}", "infect humans", f"base rate {pct(base)}"),
        stat_card(f"{splits.get('cohort_size', 0):,}", "modelable cohort", f"{splits.get('cohort_positives',0)} positive"),
        stat_card(labels.get("n_families", 0), "virus families", f"{labels.get('n_genera',0)} genera"),
        stat_card(pct(labels.get("base_rate_mammal_assoc", 0)), "base rate (mammal hosts)", "vs 10.4% overall"),
        stat_card(pct(labels.get("clover_agreement_on_positives", 0)), "CLOVER agreement", "coverage gap, not error"),
    ])

    # positive/negative balance bar
    npos, ntot = labels.get("n_positive", 0), labels.get("n_viruses", 1)
    bal = f'<div class="balance"><span class="pos" style="width:{npos/ntot*100:.1f}%"></span></div>' \
          f'<div class="balcap"><span>● {npos:,} human-infecting</span><span>{ntot-npos:,} not ●</span></div>'

    gen = datetime.now().strftime("%Y-%m-%d %H:%M")
    return TEMPLATE.format(
        flow=pipeline_flow(status),
        cards=cards,
        balance=bal,
        honest=honest_eval_panel(splits),
        ladder=ladder_panel(),
        results=results_panel(metrics),
        runtime=status.get("runtime", "local"),
        generated=gen,
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>zoonotic-v0 · dashboard</title>
<style>
:root{{
  --bg:#0b0f14; --panel:#121821; --panel2:#0e141c; --bd:#1f2a37;
  --fg:#e6edf3; --mut:#8b9aa9; --teal:#2dd4bf; --green:#34d399;
  --red:#f87171; --amber:#fbbf24; --blue:#60a5fa; --violet:#a78bfa;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:radial-gradient(1200px 600px at 70% -10%,#13202b 0,var(--bg) 60%);
  color:var(--fg);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1100px;margin:0 auto;padding:32px 24px 64px}}
h1{{font-size:24px;margin:0;letter-spacing:-.4px}}
h2{{font-size:13px;text-transform:uppercase;letter-spacing:1.5px;color:var(--mut);
  margin:40px 0 14px;font-weight:600}}
.sub{{color:var(--mut);font-size:12px}}
.mono{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}
.head{{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}}
.mission{{color:var(--mut);max-width:620px;margin:8px 0 0}}
.pill{{display:inline-flex;align-items:center;gap:7px;background:var(--panel);border:1px solid var(--bd);
  border-radius:999px;padding:6px 12px;font-size:12px;color:var(--mut)}}
.pill .live{{width:8px;height:8px;border-radius:50%;background:var(--amber);box-shadow:0 0 0 0 var(--amber);
  animation:pulse 1.8s infinite}}
@keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(251,191,36,.5)}}70%{{box-shadow:0 0 0 8px rgba(251,191,36,0)}}100%{{box-shadow:0 0 0 0 rgba(251,191,36,0)}}}}

/* pipeline flow */
.flow{{display:flex;align-items:stretch;gap:6px;overflow-x:auto;padding:4px}}
.node{{flex:1;min-width:128px;background:var(--panel);border:1px solid var(--bd);border-radius:12px;
  padding:14px 12px;position:relative}}
.node .dot{{width:9px;height:9px;border-radius:50%;background:var(--mut);margin-bottom:9px}}
.node.done .dot{{background:var(--green)}}
.node.running .dot{{background:var(--amber);animation:pulse 1.6s infinite}}
.node.pending{{opacity:.55}}
.nlabel{{font-weight:600;font-size:13px}}
.ndetail{{color:var(--mut);font-size:11px;margin-top:3px;line-height:1.35}}
.prog{{height:5px;background:var(--panel2);border-radius:3px;margin-top:9px;overflow:hidden}}
.prog span{{display:block;height:100%;background:linear-gradient(90deg,var(--teal),var(--green))}}
.arrow{{display:flex;align-items:center;color:var(--bd);font-size:18px}}

/* cards */
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}}
.card{{background:var(--panel);border:1px solid var(--bd);border-radius:12px;padding:16px}}
.card .val{{font-size:24px;font-weight:700;letter-spacing:-.5px}}
.card .lbl{{color:var(--fg);font-size:13px;margin-top:2px}}
.card .sub{{margin-top:4px}}
.balance{{height:12px;border-radius:6px;background:#223;overflow:hidden;margin:14px 0 6px;border:1px solid var(--bd)}}
.balance .pos{{display:block;height:100%;background:linear-gradient(90deg,var(--red),#fb7185)}}
.balcap{{display:flex;justify-content:space-between;color:var(--mut);font-size:12px}}

/* honest eval */
.split-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.split-card{{border:1px solid var(--bd);border-radius:14px;padding:18px;background:var(--panel)}}
.split-card p{{color:var(--mut);font-size:13px}}
.split-card.leaky{{border-color:#7f1d1d55}}
.split-card.honest{{border-color:#065f4655}}
.tag{{font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:10px}}
.leaky .tag{{color:var(--red)}} .honest .tag{{color:var(--green)}}
.bars{{display:flex;align-items:flex-end;gap:10px;height:90px;margin-top:12px}}
.bwrap{{flex:1;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end}}
.bar{{width:100%;border-radius:5px 5px 0 0;min-height:4px}}
.bar.leaky{{background:linear-gradient(180deg,#fb7185,#7f1d1d)}}
.bar.honest{{background:linear-gradient(180deg,#34d399,#065f46)}}
.bx{{color:var(--mut);font-size:11px;margin-top:5px}}
.caption{{color:var(--mut);font-size:11px;margin-top:8px;text-align:center}}
.thesis{{margin-top:16px;padding:14px 16px;border-left:3px solid var(--teal);background:var(--panel2);
  border-radius:0 10px 10px 0;color:var(--fg)}}

/* ladder */
.ladder{{display:flex;flex-direction:column;gap:8px}}
.rung{{display:flex;gap:14px;align-items:center;background:var(--panel);border:1px solid var(--bd);
  border-radius:12px;padding:12px 16px}}
.rung.baseline{{border-left:3px solid var(--amber)}}
.rung.model{{border-left:3px solid var(--blue)}}
.rn{{font-family:ui-monospace,monospace;color:var(--mut);font-size:18px;width:22px;text-align:center}}
.rname{{font-weight:600}}
.rhow{{color:var(--mut);font-size:12px;margin-top:1px}}
.rtests{{color:var(--teal);font-size:12px;margin-top:3px}}

/* results */
.metrics{{width:100%;border-collapse:collapse;font-size:13px}}
.metrics th,.metrics td{{padding:9px 12px;text-align:left;border-bottom:1px solid var(--bd)}}
.metrics th{{color:var(--mut);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.5px}}
.resmatrix{{width:100%;border-collapse:collapse;font-size:13px}}
.resmatrix th{{color:var(--mut);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.5px;
  padding:8px 10px;text-align:center;border-bottom:1px solid var(--bd)}}
.resmatrix th:first-child{{text-align:left}}
.resmatrix th.hl{{color:var(--green)}}
.resmatrix td{{padding:8px 10px;border-bottom:1px solid var(--bd)}}
.rn-name{{font-family:ui-monospace,monospace;font-size:12px}}
.resmatrix tr.baseline .rn-name{{color:var(--amber)}}
.resmatrix tr.model .rn-name{{color:var(--blue)}}
.resmatrix tr.pend{{opacity:.5}}
.mc{{text-align:center}}
.mc .lift{{font-weight:700;font-size:15px}}
.mc .roc{{display:block;color:var(--mut);font-size:11px;margin-top:1px}}
.mut{{color:var(--mut)}}
.rcap{{margin-top:12px;color:var(--mut);font-size:12px;line-height:1.5}}
.empty{{display:flex;gap:18px;align-items:center;background:var(--panel);border:1px dashed var(--bd);
  border-radius:14px;padding:24px;color:var(--mut)}}
.eicon{{font-family:ui-monospace,monospace;font-size:22px;color:var(--bd);letter-spacing:3px}}
.foot{{margin-top:48px;color:var(--mut);font-size:12px;border-top:1px solid var(--bd);padding-top:16px;
  display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}
@media(max-width:720px){{.split-grid{{grid-template-columns:1fr}}}}
</style></head>
<body><div class="wrap">
  <div class="head">
    <div>
      <h1>zoonotic-v0 <span class="sub mono">· genome → human-infection</span></h1>
      <p class="mission">Predict whether a viral genome can infect humans — and honestly
      measure whether that signal generalises to genuinely novel viruses, or just
      memorises taxonomy.</p>
    </div>
    <div class="pill"><span class="live"></span> running on {runtime}</div>
  </div>

  <h2>Pipeline</h2>
  <div class="flow">{flow}</div>

  <h2>Data at a glance</h2>
  <div class="cards">{cards}</div>
  {balance}

  <h2>The question that matters · random vs taxonomic holdout</h2>
  {honest}

  <h2>The model · a reference ladder, built bottom-up</h2>
  <div class="ladder">{ladder}</div>

  <h2>Results</h2>
  {results}

  <div class="foot">
    <span>Sources: VIRION · CLOVER · HP3 · ICTV VMR · NCBI RefSeq</span>
    <span class="mono">generated {generated}</span>
  </div>
</div></body></html>"""


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
