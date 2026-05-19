# Prompt: dbt Model Generator

Generate a complete dbt model (SQL + schema.yml + tests) from a source table description.

---

## Prompt Template

```
You are a senior analytics engineer. Generate a complete dbt model package for the staging/intermediate/mart layer described below.

**Layer:** [staging / intermediate / mart]
**Source table name:** [e.g. raw.shopify_orders]
**Target model name:** [e.g. stg_shopify__orders]

**Source schema (paste DDL or column list):**
[e.g.]
order_id STRING
customer_id STRING
created_at TIMESTAMP
status STRING (values: pending, processing, complete, cancelled, refunded)
subtotal_price NUMERIC
total_price NUMERIC
discount_codes ARRAY<STRING>
shipping_address JSON

**Business context:**
[e.g. "This is the Shopify orders table. We use it to track e-commerce revenue.
Cancelled and refunded orders should be flagged but not excluded.
order_id is always unique. created_at is in UTC."]

**Output I need:**
1. `models/staging/stg_shopify__orders.sql` — clean, renamed, typed columns; no business logic
2. `models/staging/schema.yml` — with description, column descriptions, and tests
3. Suggested dbt tests: not_null, unique, accepted_values, relationships

Rules:
- Use {{ source() }} macro for staging models
- Use snake_case column names
- Cast all timestamps to TIMESTAMP
- Add a boolean flag `is_cancelled` for cancelled/refunded status
- Add `_loaded_at` audit column using current_timestamp
- Do not add business metrics to staging layer
```

---

## Example Output Structure

### stg_shopify__orders.sql
```sql
with source as (
    select * from {{ source('shopify', 'orders') }}
),

renamed as (
    select
        order_id,
        customer_id,
        cast(created_at as timestamp) as created_at,
        status,
        status in ('cancelled', 'refunded') as is_cancelled,
        cast(subtotal_price as numeric) as subtotal_price,
        cast(total_price as numeric) as total_price,
        current_timestamp as _loaded_at
    from source
)

select * from renamed
```

### schema.yml
```yaml
version: 2

models:
  - name: stg_shopify__orders
    description: "Cleaned and renamed Shopify orders from raw source."
    columns:
      - name: order_id
        description: "Primary key. Unique identifier for each order."
        tests:
          - unique
          - not_null
      - name: status
        description: "Order status from Shopify."
        tests:
          - accepted_values:
              values: ['pending', 'processing', 'complete', 'cancelled', 'refunded']
      - name: is_cancelled
        description: "True if order was cancelled or refunded."
        tests:
          - not_null
```

---

## Layer-Specific Rules

| Layer | Purpose | Should contain |
|-------|---------|---------------|
| `staging` | Clean raw → typed, renamed | Renaming, casting, simple flags |
| `intermediate` | Join/combine sources | Business joins, deduplication |
| `mart` | Business-ready | Aggregations, metrics, final grain |

---

## Tips
- Always generate staging before intermediate/mart
- Add `accepted_values` tests for all status/type columns
- Use `relationships` test for all foreign keys to other models
