# Prompt: Data Quality Check Generator

Generate dbt-expectations or Great Expectations checks from a table profile.

---

## Prompt Template (dbt-expectations)

```
You are a data quality engineer. Generate dbt-expectations tests for the table described below.

**Table name:** [e.g. fct_daily_sales]
**Grain:** [e.g. one row per outlet per day]
**Source system:** [e.g. POS system export, synced via Airbyte]

**Column profile (paste output of SELECT * FROM ... LIMIT 5 or describe the columns):**
[e.g.]
- date DATE — no nulls, business days only
- outlet_id STRING — FK to dim_outlets
- total_revenue NUMERIC — always positive, typical range 500K–5M
- transaction_count INT — always positive, typical range 50–500
- avg_ticket NUMERIC — derived: total_revenue / transaction_count
- data_freshness_ts TIMESTAMP — when this row was last updated

**Known business rules:**
[e.g. "Revenue can never be negative. Outlets that are closed have 0 transactions, not NULL.
avg_ticket should be between 10K and 150K. No data should be older than 2 days."]

**Generate:**
1. schema.yml dbt-expectations tests for each column
2. A model-level test for row count (at least N rows per day)
3. A freshness check
4. Any anomaly detection suggestions (spike/drop thresholds)
```

---

## Example Output

```yaml
version: 2

models:
  - name: fct_daily_sales
    description: "Daily sales fact table at outlet-day grain."
    tests:
      - dbt_expectations.expect_table_row_count_to_be_between:
          min_value: 100  # at least 100 outlets reporting per day
          max_value: 2000

    columns:
      - name: date
        tests:
          - not_null
          - dbt_expectations.expect_column_values_to_be_of_type:
              column_type: date
          - dbt_expectations.expect_column_values_to_be_between:
              min_value: "'2024-01-01'"
              max_value: "current_date"

      - name: outlet_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_outlets')
              field: outlet_id

      - name: total_revenue
        tests:
          - not_null
          - dbt_expectations.expect_column_values_to_be_between:
              min_value: 0
              max_value: 50000000  # 50M hard cap — investigate if exceeded

      - name: transaction_count
        tests:
          - not_null
          - dbt_expectations.expect_column_values_to_be_between:
              min_value: 0
              max_value: 2000

      - name: avg_ticket
        tests:
          - dbt_expectations.expect_column_values_to_be_between:
              min_value: 10000
              max_value: 150000
          - dbt_expectations.expect_column_value_lengths_to_be_between:
              # Ensure avg_ticket is not NULL when transaction_count > 0
              # Use a custom test below instead

      - name: data_freshness_ts
        tests:
          - not_null
          - dbt_expectations.expect_column_values_to_be_between:
              min_value: "dateadd(day, -2, current_timestamp)"
              max_value: "current_timestamp"
```

---

## Prompt Template (Great Expectations)

```
Generate a Great Expectations suite for the following table.

**Table:** [name]
**Columns and types:** [list]
**Business rules:** [list]
**Environment:** [Pandas DataFrame / SQLAlchemy / Spark]

Output: Python code using great_expectations SDK to define the expectation suite.
Include:
- expect_column_values_to_not_be_null for required columns
- expect_column_values_to_be_between for numeric ranges
- expect_column_values_to_be_in_set for categorical columns
- expect_table_row_count_to_be_between
- expect_column_pair_values_A_to_be_greater_than_B where applicable
```

---

## Anomaly Detection Thresholds (add to any prompt)

```
Also add anomaly detection rules:
- Alert if daily revenue drops more than 20% from 7-day average
- Alert if transaction count drops more than 30% vs same day last week
- Alert if avg_ticket exceeds 2x the 30-day median
Format these as dbt macros or SQL assertions I can run as a scheduled check.
```
