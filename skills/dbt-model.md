# Skill: dbt-model

Generate a complete dbt model package (SQL + schema.yml + tests) from a source table or a business requirement.

## Trigger phrases
- "create a dbt model for..."
- "generate a staging model for..."
- "write dbt for [table name]"
- "build a mart for..."

## Instructions

When invoked, ask the user for (if not already provided):
1. Target layer: staging / intermediate / mart
2. Source table name and schema (DDL or column list)
3. Business context / rules
4. Target model name (suggest one if not given)

Then generate:
1. **The SQL model file** — clean, well-commented, using proper macros
2. **schema.yml entry** — with descriptions and tests
3. **Suggested dbt tests** — not_null, unique, accepted_values, relationships, dbt_expectations

### Layer rules

**Staging (`stg_`):**
- Use `{{ source('source_name', 'table_name') }}`
- Rename columns to snake_case
- Cast types (especially timestamps and numerics)
- Add simple boolean flags (is_deleted, is_active, is_cancelled)
- No aggregations or joins
- Add `_loaded_at AS current_timestamp`

**Intermediate (`int_`):**
- Use `{{ ref('stg_...') }}`
- Joins between staging models
- Deduplication logic
- Business rule application
- No final aggregations

**Mart (`fct_` / `dim_`):**
- Use `{{ ref('int_...') }}` or `{{ ref('stg_...') }}`
- Final aggregations and metrics
- Optimized for BI consumption
- Include grain comment at top of file

### Output format

```sql
-- models/{layer}/{model_name}.sql
-- Grain: [one row per ...]
-- Owner: [team/person]

with source as (
    select * from {{ source('...', '...') }}
    -- OR: select * from {{ ref('...') }}
),

renamed as (
    select
        -- primary key
        order_id,

        -- dimensions
        customer_id,
        outlet_id,
        status,
        status in ('cancelled', 'refunded') as is_cancelled,

        -- measures
        cast(total_amount as numeric) as total_amount,

        -- metadata
        cast(created_at as timestamp) as created_at,
        current_timestamp as _loaded_at

    from source
)

select * from renamed
```

Then show the schema.yml block separately.

## Example invocation
User: "Create a staging model for our BigQuery table `raw.shopify_orders` with columns order_id STRING, customer_id STRING, status STRING, total_price FLOAT64, created_at TIMESTAMP"
