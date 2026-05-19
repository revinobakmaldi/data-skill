# Prompt: KPI Data → Executive Narrative

Turn a table of numbers or KPIs into a concise, decision-ready executive summary.

---

## Prompt Template

```
You are a senior data analyst writing an executive briefing. Convert the data below into a clear, actionable narrative.

**Audience:** [e.g. VP of Operations / C-suite / Regional managers]
**Report period:** [e.g. Week 20, 2026 (12–18 May)]
**Business context:** [e.g. QSR restaurant chain, tracking daily ops KPIs]

**Data:**
[Paste your table, CSV, or bullet list of KPIs here, e.g.:]

| Region | Revenue | vs LW | vs Target | SoS | Upsell Rate |
|--------|---------|-------|-----------|-----|-------------|
| Jakarta | 1.24B | +3.2% | -1.8% | 92% | 18.4% |
| Surabaya | 890M | -1.1% | +2.3% | 88% | 21.2% |
| Bandung | 670M | +5.6% | +4.1% | 95% | 16.8% |

**Output requirements:**
- Max 3 paragraphs
- Lead with the single most important signal (positive or negative)
- Paragraph 2: what's driving it (root cause if visible in data)
- Paragraph 3: recommended action or watch item
- Tone: direct, data-backed, no filler
- Do NOT restate every number — highlight only outliers and trends
- End with 1 bullet: "Watch this week:" with the #1 risk or opportunity
```

---

## Example Output

> Jakarta leads the network this week at Rp 1.24B revenue but remains 1.8% below target — the only region in the red against plan. Surabaya recovered week-on-week but continues to outperform target by 2.3%, driven by strong upsell conversion at 21.2%.
>
> Bandung shows the strongest momentum with +5.6% WoW growth and 95% Speed of Service — the highest in the network. This suggests Bandung's recent staffing changes are taking hold.
>
> Priority action: investigate Jakarta's target shortfall. With SoS at 92% and upsell at 18.4%, the issue is likely transaction volume, not execution. Review traffic data and promo coverage for the week.
>
> **Watch this week:** Jakarta target gap — if it persists into W21, escalate to regional review.

---

## Variants

### For weekly ops reports
Add to prompt: *"Include a 'Green/Amber/Red' status for each region based on target attainment."*

### For data science outputs
Add to prompt: *"The data comes from a model output. Explain what the model found in plain English, then state what action it implies."*

### For board-level
Add to prompt: *"One paragraph only. No numbers in the opening sentence. Start with the business implication."*
