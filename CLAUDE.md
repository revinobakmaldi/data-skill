# Data Team — AI Assistant Instructions

This file is read by Claude Code, AWS Kiro, and other AI coding assistants.
It defines how AI should behave when working in this analytics codebase.

---

## Stack & Tools

| Layer | Tool |
|-------|------|
| Orchestration | Apache Airflow (DAGs in `dags/`, connections in Airflow UI) |
| Transformation | dbt Core (models in `models/`, profiles in `~/.dbt/profiles.yml`) |
| Data warehouse | BigQuery (project: `your-gcp-project`, dataset prefix: `analytics_`) |
| Data quality | dbt-expectations + Great Expectations |
| BI / reporting | Power BI + HTML reports (rendered via Playwright) |
| LLM / AI coding | Claude Code (CLI) |
| Scripting | Python 3.11+ |

---

## Project Conventions

### dbt
- Staging models: `stg_{source}__{entity}.sql` — clean, rename, cast only
- Intermediate models: `int_{domain}_{description}.sql` — joins, dedup, business logic
- Mart models: `fct_{entity}.sql` / `dim_{entity}.sql` — final grain, no logic
- All models must have `schema.yml` with column descriptions and tests
- Use `{{ source() }}` in staging, `{{ ref() }}` everywhere else
- Required tests on every model: `unique` + `not_null` on primary key
- Use `dbt-expectations` for range checks, `relationships` for FK integrity

### Airflow DAGs
- File naming: `{frequency}_{domain}_{description}_dag.py` (e.g. `daily_sales_pipeline_dag.py`)
- Always set `catchup=False` and `max_active_runs=1`
- Schedule in UTC cron (server timezone: WIB/UTC+7, so subtract 7h)
- Retry: 2 retries, 5-minute delay
- On failure: Slack alert to `#data-alerts`
- Use connections from Airflow UI — never hardcode credentials

### Python scripts
- Use type hints
- Use argparse for CLI scripts
- Always check for required env vars at startup and exit with a clear error if missing
- No hardcoded credentials — use environment variables or secret manager

### SQL style
- Use CTEs, not subqueries
- snake_case column names
- Explicit column lists — no `SELECT *` in production models
- Always filter out deleted/test records unless the analysis specifically needs them

---

## Data Layer Boundaries

```
Source DB / APIs
      ↓
  [Airbyte / dlt]         ← ingestion layer (raw, untransformed)
      ↓
  BigQuery: raw_*          ← raw tables, never modified by dbt
      ↓
  dbt staging (stg_*)      ← clean, typed, renamed — no logic
      ↓
  dbt intermediate (int_*) ← joins, dedup, business rules
      ↓
  dbt mart (fct_/dim_*)    ← final, queryable by BI and analysts
      ↓
  Power BI / HTML reports  ← consumption layer
```

**Do not skip layers.** If a mart model needs something that doesn't exist in intermediate, build the intermediate model first.

---

## Common Tasks

### Generate a dbt model
See `prompts/dbt-model-generator.md` for the full prompt template.
Quick version: provide source table DDL + business context → get stg model + schema.yml.

### Write SQL from a business question
See `prompts/sql-from-question.md`.
Always provide schema context and dialect (BigQuery).

### Generate an Airflow DAG
See `prompts/dag-scaffold.md`.
Provide: pipeline steps, schedule, connections, error handling requirements.

### Analyze data with Claude
Use `scripts/data_to_claude.py`:
```bash
python scripts/data_to_claude.py --file sales.csv --question "What are the top trends?"
```

### Convert HTML report to PDF
Use `scripts/html_to_pdf.py`:
```bash
python scripts/html_to_pdf.py report.html -o report_output.pdf
```

---

## MCP Servers

See `mcp/configs/` for ready-to-use MCP config snippets.

| MCP | Use for |
|-----|---------|
| Google MCP Toolbox | BigQuery schema discovery, SQL execution, multi-source access |
| dbt MCP | dbt model generation, test creation, semantic queries |
| Power BI Modeling MCP | Semantic model only: DAX, measures, tables, columns, relationships |

## Claude Code Plugins

See `plugins/` for installed Claude Code plugin marketplaces.

| Plugin | Use for |
|--------|---------|
| data-goblin/power-bi-agentic-development | Report/visual editing (PBIP), Deneb visuals, Tabular Editor, Fabric CLI, semantic model auditing |

> Power BI semantic model → use Power BI Modeling MCP (live tool calls)
> Power BI report/visual editing → use data-goblin plugins (requires PBIP format)

---

## What NOT to do

- Never write to raw tables directly — they are owned by the ingestion layer
- Never use `SELECT *` in dbt models
- Never hardcode connection strings, passwords, or API keys
- Never skip writing `schema.yml` for a new model
- Never run `dbt run` without `dbt test` afterwards in a pipeline context
- Never push directly to `main` — use feature branches and PR
