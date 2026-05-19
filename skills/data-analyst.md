# Skill: data-analyst

Analyze a data file or pasted table and answer a business question about it.
No API key needed — runs inside Claude Code.

## Trigger phrases
- "analyze this data: ..."
- "what does this data show?"
- "find trends in this table"
- "flag anomalies in..."
- "summarize this dataset"

## Instructions

When invoked with data (CSV, table, JSON, or bullet list of numbers):

1. Parse the structure — identify columns, grain, and data type of each field
2. Answer the question asked, or if no question is given: surface the top 3 most interesting signals
3. Call out any anomalies, outliers, or data quality issues you notice
4. End with one actionable recommendation if the data supports it

### Output format

**Signal:** [1-sentence answer to the question or top finding]

**Details:**
- [bullet points with specific numbers from the data]
- [comparisons, deltas, or trends]
- [any anomalies]

**Recommendation:** [1 specific action, or "no action needed" if data looks healthy]

### Rules
- Always quote exact numbers from the data — no vague "some rows have issues"
- If the data has a time dimension, always check for trends or seasonality
- If a column has nulls >10%, flag it
- If a numeric column has outliers (>3x median), name them specifically
- Keep the output under 200 words unless the dataset is complex

## Example invocation

User pastes:
```
date, outlet, revenue, transactions
2026-05-12, Jakarta-01, 1240000, 312
2026-05-12, Jakarta-02, 890000, 198
2026-05-12, Surabaya-01, 2100000, 441
2026-05-12, Bandung-01, 450000, 88
```

With question: "Any outliers?"

Expected response:
> **Signal:** Surabaya-01 is a significant outlier — 69% above the group average in revenue and 41% above in transactions.
>
> **Details:**
> - Average revenue (ex. Surabaya-01): ~860K. Surabaya-01: 2.1M.
> - Average ticket: Jakarta-01 = 3,974 | Jakarta-02 = 4,495 | Surabaya-01 = 4,762 | Bandung-01 = 5,114
> - Bandung-01 has the lowest transaction count (88) but highest avg ticket — worth investigating if it's a different outlet format.
>
> **Recommendation:** Verify Surabaya-01 data is not duplicated or double-counted before using in reports.
