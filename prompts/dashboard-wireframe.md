# Prompt: Dashboard Brief → HTML Prototype

Convert a dashboard requirements brief into a working HTML prototype for stakeholder review.

---

## Prompt Template

```
You are a senior data visualization engineer. Build a working HTML dashboard prototype from the brief below.

**Dashboard name:** [e.g. Regional Ops Daily Scorecard]
**Audience:** [e.g. Regional Operations Manager]
**Primary question it answers:** [e.g. "How is each region performing vs target today?"]

**KPIs to show:**
[e.g.]
1. Revenue (Actual vs Target, % attainment)
2. Transaction Count
3. Speed of Service (SoS %)
4. Upsell Rate %
5. Active Outlets (reporting vs total)

**Breakdown dimensions:**
- By region (Jakarta, Surabaya, Bandung, Medan)
- By day (last 7 days trend)

**Layout requirements:**
- Mobile-friendly (used on phone by field managers)
- Status color coding: green >100% target, amber 90-100%, red <90%
- Summary row at top showing network total
- Show delta vs last week next to each KPI

**Data is static for the prototype — use realistic dummy numbers.**

**Tech constraints:** Pure HTML/CSS/JS only. No frameworks, no build step.
Must work when opened as a local file (no server needed).

Output: Single self-contained HTML file.
```

---

## Example Sections to Request

### Add a chart
```
Add a sparkline trend chart (last 7 days) for Revenue per region using Chart.js CDN.
```

### Add filters
```
Add a dropdown to filter by region. When "All" is selected, show network total.
When a specific region is selected, show outlet-level breakdown for that region.
```

### Add export
```
Add a "Download PDF" button that uses window.print() with a print-optimized stylesheet.
The PDF version should hide buttons and show a header with report date and company logo placeholder.
```

### Add alerts
```
Add an alert banner at the top that shows if any region is more than 10% below target.
The banner should list the region name, current attainment %, and gap to target.
```

---

## Tips
- Always start with the single-file constraint — it makes sharing easy
- Request realistic dummy data (not 100/100/100 — that looks fake)
- Ask for mobile-first layout if the audience is field-based
- Iterate: first get layout right, then add interactivity, then add data
