# Skill: dag-builder

Generate production-ready Apache Airflow DAGs from a pipeline description.

## Trigger phrases
- "create an Airflow DAG for..."
- "write a DAG that..."
- "build a pipeline that..."
- "schedule this pipeline..."

## Instructions

When invoked, gather (or ask for):
1. Pipeline steps in order
2. Schedule (ask for WIB time — convert to UTC cron internally)
3. Data source and destination connections
4. SLA requirement (if any)
5. Error handling / notification requirements

Then generate a complete, runnable Python DAG file.

### WIB → UTC cron conversion
WIB is UTC+7. To run at 06:00 WIB: `0 23 * * *` (subtract 7 hours)
Always add a comment showing the WIB equivalent next to the cron string.

### Required DAG settings (always include)
```python
default_args = {
    'owner': 'data-engineering',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
}

DAG(
    catchup=False,
    max_active_runs=1,
    tags=['domain', 'frequency'],
)
```

### Standard task structure
1. **Sensor** (optional) — wait for upstream data or file
2. **Extract** — pull from source
3. **Load** — push to staging/warehouse
4. **Transform** — run dbt models
5. **Validate** — run dbt tests or GE checkpoint
6. **Notify** — Slack success/failure message

### Slack notification pattern
```python
from airflow.providers.slack.operators.slack import SlackAPIPostOperator

notify_success = SlackAPIPostOperator(
    task_id='notify_success',
    slack_conn_id='slack_default',
    channel='#data-alerts',
    text=f':white_check_mark: `{dag_id}` completed successfully for {{{{ ds }}}}',
    trigger_rule='all_success',
)

notify_failure = SlackAPIPostOperator(
    task_id='notify_failure',
    slack_conn_id='slack_default',
    channel='#data-on-call',
    text=f':red_circle: `{dag_id}` FAILED for {{{{ ds }}}}. Check logs.',
    trigger_rule='one_failed',
)
```

### dbt task pattern
```python
from airflow.operators.bash import BashOperator

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='dbt run --select stg_orders+ --target prod',
    env={'DBT_PROFILES_DIR': '/opt/airflow/dbt'},
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='dbt test --select stg_orders+ --target prod',
    env={'DBT_PROFILES_DIR': '/opt/airflow/dbt'},
)
```

## Output format

Single Python file, named `{frequency}_{domain}_{description}_dag.py`.
Include all imports at top. Add docstring to the DAG explaining what it does.
Show task dependency chain clearly at the bottom: `t1 >> t2 >> [t3, t4] >> t5`
