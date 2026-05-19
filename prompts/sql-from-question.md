# Prompt: SQL from Business Question

Convert a plain-language business question into production-ready SQL.

---

## Prompt Template

```
You are a senior data analyst. Convert the business question below into SQL.

**Database dialect:** [BigQuery / PostgreSQL / Snowflake / DuckDB]
**Schema context:**
[Paste table schemas or descriptions here, e.g.:]
- orders(order_id, customer_id, outlet_id, created_at, status, total_amount)
- customers(customer_id, name, segment, region)
- outlets(outlet_id, name, city, region)

**Business question:**
[e.g. "What are the top 10 outlets by revenue in the last 30 days, broken down by region?"]

**Requirements:**
- Use CTEs for readability
- Add inline comments for non-obvious logic
- Include a WHERE clause to filter out nulls or cancelled orders unless relevant
- Format amounts with 2 decimal places
- Output: SQL only, no explanation needed
```

---

## Example Usage

**Input:**
> What percentage of orders from each region were completed vs cancelled in Q1 2026?

**Expected output structure:**
```sql
WITH order_summary AS (
  SELECT
    o.region,
    s.status,
    COUNT(*) AS order_count
  FROM orders s
  JOIN outlets o ON s.outlet_id = o.outlet_id
  WHERE s.created_at BETWEEN '2026-01-01' AND '2026-03-31'
  GROUP BY 1, 2
),
totals AS (
  SELECT region, SUM(order_count) AS total FROM order_summary GROUP BY 1
)
SELECT
  os.region,
  os.status,
  os.order_count,
  ROUND(100.0 * os.order_count / t.total, 2) AS pct
FROM order_summary os
JOIN totals t ON os.region = t.region
ORDER BY 1, 2
```

---

## Tips
- Always provide schema context — the more specific, the better the SQL
- Mention any business rules (e.g. "exclude test outlets", "only count first orders")
- For complex joins, add a note about relationships between tables
