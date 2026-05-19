# Agent Instructions — Data Team Analytics Repo

This file is read by OpenAI Codex, GitHub Copilot Workspace, and other agent-based coding tools.

---

## Repository Purpose

This is an analytics engineering repo for a data team. It contains:
- dbt transformation models (`models/`)
- Airflow DAGs (`dags/`)
- Python scripts for data ops (`scripts/`)
- Prompt templates for AI-assisted analytics (`prompts/`)
- MCP server configs (`mcp/configs/`)

---

## Key Conventions (READ BEFORE WRITING CODE)

### dbt models
1. Staging: rename + cast only. Never add business logic.
2. Intermediate: joins and business rules. Reference staging models only.
3. Mart: final aggregations. Reference intermediate or other mart models.
4. Every new model MUST have a corresponding entry in `schema.yml`.
5. Primary keys need `unique` + `not_null` tests always.

### Airflow DAGs
1. Always use `catchup=False` and `max_active_runs=1`.
2. Schedules in UTC cron. Server timezone is WIB (UTC+7).
3. Retry config: `retries=2, retry_delay=timedelta(minutes=5)`.
4. Pull connections from Airflow connection store — no hardcoded credentials.

### Python
1. Python 3.11+, type hints required.
2. Use `argparse` for all CLI scripts.
3. Required env vars must be checked at startup with a clear error message.

### SQL
1. BigQuery dialect unless otherwise specified.
2. Use CTEs, never nested subqueries.
3. No `SELECT *` in production code.

---

## File Structure

```
models/
  staging/      stg_{source}__{entity}.sql + schema.yml
  intermediate/ int_{domain}_{description}.sql + schema.yml
  mart/         fct_{entity}.sql / dim_{entity}.sql + schema.yml
dags/           {frequency}_{domain}_{description}_dag.py
scripts/        data_to_claude.py, html_to_pdf.py
prompts/        prompt templates for common analytics tasks
mcp/configs/    MCP server JSON configs
```

---

## Testing Requirements

After writing any dbt model:
1. Run `dbt compile` — check for syntax errors
2. Run `dbt test --select <model_name>` — all tests must pass
3. If adding a new source, run `dbt source freshness`

After writing any Python script:
1. Run `python <script>.py --help` — verify argparse works
2. Test with a small sample file before large datasets

---

## Do Not

- Modify files in `raw/` or `raw_*` datasets — they are ingestion-owned
- Add `SELECT *` to any dbt model
- Hardcode any credentials, tokens, or connection strings
- Merge to `main` without a PR review
