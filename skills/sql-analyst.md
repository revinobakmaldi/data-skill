# Skill: sql-analyst

Answer business questions with production-ready BigQuery SQL.

## Trigger phrases
- "write SQL for..."
- "give me a query to..."
- "how do I query..."
- "SQL to find..."

## Instructions

When invoked:
1. Identify the business question
2. If schema context is missing, ask for it (table names + key columns)
3. Generate SQL using BigQuery dialect
4. Explain the logic briefly after the code block

### SQL standards to follow

- Use CTEs, not nested subqueries
- snake_case aliases
- Explicit column list (no `SELECT *`)
- Add inline comments for non-obvious logic
- Filter nulls at the source CTE level
- Use `DATE_TRUNC`, `FORMAT_DATE`, `TIMESTAMP_DIFF` for time operations (BigQuery)
- Round monetary values to 2 decimal places
- Use `SAFE_DIVIDE()` for any division to avoid zero-division errors

### Output format

```sql
-- [Brief description of what this query answers]
-- Grain: [e.g. one row per outlet per day]

with orders as (
    select
        order_id,
        outlet_id,
        date(created_at) as order_date,
        status,
        total_amount
    from `analytics_mart.fct_orders`
    where status != 'test'
      and created_at >= date_sub(current_date(), interval 30 day)
),

summary as (
    select
        outlet_id,
        sum(total_amount) as revenue,
        count(order_id) as order_count,
        safe_divide(sum(total_amount), count(order_id)) as avg_ticket
    from orders
    group by 1
)

select
    o.outlet_id,
    d.outlet_name,
    d.region,
    s.revenue,
    s.order_count,
    round(s.avg_ticket, 2) as avg_ticket
from summary s
join `analytics_mart.dim_outlets` d using (outlet_id)
order by s.revenue desc
limit 20
```

## Common patterns to know

### Week-over-week comparison
```sql
with current_week as (...where date between date_trunc(current_date(), week) and current_date()),
prev_week as (...where date between date_sub(date_trunc(current_date(), week), interval 7 day) and date_sub(current_date(), interval 7 day))
select ..., safe_divide(current - prev, prev) * 100 as wow_pct
```

### Running total
```sql
sum(revenue) over (partition by region order by order_date rows unbounded preceding) as cumulative_revenue
```

### Latest record per group (dedup)
```sql
with ranked as (
    select *, row_number() over (partition by order_id order by updated_at desc) as rn
    from source_table
)
select * from ranked where rn = 1
```
