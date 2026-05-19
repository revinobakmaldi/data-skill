# Skill: insight-writer

Turn raw data or KPI tables into executive-ready narratives and summaries.

## Trigger phrases
- "write a narrative for this data"
- "summarize these KPIs"
- "write the insight for..."
- "turn this into a report summary"
- "executive summary of..."

## Instructions

When invoked with data (table, CSV, bullets, or numbers):
1. Identify the audience (default: operations leadership)
2. Find the single most important signal in the data
3. Write the narrative following the structure below

### Narrative structure

**Paragraph 1 — Lead with the signal**
Start with the most important fact. Positive or negative, make it specific and quantified.
Do NOT start with "This week" or "The data shows" — lead with the insight itself.

**Paragraph 2 — Root cause or driver**
What explains the signal? Connect it to a metric, region, or period visible in the data.

**Paragraph 3 — Action or watch item**
One recommendation OR what to monitor next. Keep it specific.

**Watch this:** (bullet) — The single #1 risk or opportunity for the next period.

### Writing rules
- Max 150 words total (3 short paragraphs + 1 bullet)
- Numbers must appear in the copy — no vague "some regions underperformed"
- Use % changes, not just absolute numbers unless context is clear
- Amber/Red regions get named specifically
- Do not hedge with "may", "could", "might" — be direct
- No passive voice in the lead sentence

### Output example (given sales data)

> Jakarta remains the only region below plan at 98.2% attainment (−1.8%), despite leading the network in absolute revenue at Rp 1.24B. Surabaya and Bandung both exceeded targets this week, with Bandung posting the strongest WoW growth at +5.6%.
>
> Bandung's surge is driven by Speed of Service improving to 95% — the highest in the network — suggesting the recent crew scheduling change is working. Jakarta's gap is not an execution issue (SoS: 92%, Upsell: 18.4%); it's a traffic/volume problem.
>
> Recommended action: audit Jakarta's promo coverage and footfall for W20. If traffic data confirms the shortfall, accelerate the planned Ramadan recovery promo to W21.
>
> **Watch this week:** Jakarta target gap — W21 is the decision point for promo escalation.

## Variants

Append to prompt based on context:
- **Ops report**: "Add a RAG status (🟢🟡🔴) for each region."
- **Board deck**: "One sentence only. Start with the business implication, not the metric."
- **Data science output**: "Explain the model finding in plain English, then state the action it implies."
- **Slack digest**: "Keep it under 80 words. Use bullet points."
