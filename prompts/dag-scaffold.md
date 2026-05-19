# Prompt: Pipeline Description → Airflow DAG

Generate a production-ready Airflow DAG from a plain-language pipeline description.

---

## Prompt Template

```
You are a senior data engineer. Generate a production-ready Apache Airflow DAG from the pipeline description below.

**DAG name:** [e.g. daily_sales_pipeline]
**Schedule:** [e.g. daily at 06:00 WIB (UTC+7) → "0 23 * * *" in UTC cron]
**Owner:** [e.g. data-engineering]
**SLA:** [e.g. must complete by 07:30 WIB]

**Pipeline steps (in order):**
[e.g.]
1. Extract: Pull yesterday's sales data from PostgreSQL source DB (table: raw_sales)
2. Load: Insert into BigQuery staging table (dataset: staging, table: raw_sales_daily)
3. Transform: Run dbt models: stg_sales → int_sales_by_outlet → fct_daily_sales
4. Validate: Run dbt tests on fct_daily_sales — fail DAG if critical tests fail
5. Notify: Send Slack message to #data-alerts on success or failure

**Error handling requirements:**
- Retry each task up to 2 times with 5-minute delay
- On final failure, send alert to Slack #data-on-call
- DAG should not run if previous run is still active (no catchup)

**Connections to use (already set up in Airflow):**
- PostgreSQL: `source_postgres`
- BigQuery: `bigquery_default`
- Slack: `slack_default`

**Output:** Complete Python DAG file, ready to drop into dags/ directory.
Include all imports, proper default_args, and inline comments.
```

---

## Example Output Structure

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.slack.operators.slack import SlackAPIPostOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data-engineering',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
    'sla': timedelta(hours=1, minutes=30),
}

with DAG(
    dag_id='daily_sales_pipeline',
    default_args=default_args,
    schedule_interval='0 23 * * *',  # 06:00 WIB
    start_date=datetime(2026, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=['sales', 'daily', 'critical'],
) as dag:

    extract = PostgresToGCSOperator(
        task_id='extract_sales',
        postgres_conn_id='source_postgres',
        sql="SELECT * FROM raw_sales WHERE date = '{{ ds }}'",
        bucket='your-gcs-bucket',
        filename='sales/{{ ds }}/raw_sales.csv',
    )

    # ... more tasks

    extract >> load >> transform >> validate >> notify
```

---

## Common Additions

### Add a sensor (wait for upstream data)
```
Before step 1, add an ExternalTaskSensor that waits for DAG `source_extract`
to complete for the same execution date. Timeout after 2 hours.
```

### Add branching (conditional steps)
```
After validation, add a BranchPythonOperator:
- If row count > 1000: proceed to full refresh of mart table
- If row count <= 1000: send a warning Slack message and skip mart refresh
```

### Add Great Expectations checkpoint
```
After loading to BigQuery, add a task that runs a Great Expectations checkpoint
named `daily_sales_checkpoint`. Fail the DAG if the checkpoint fails.
```
