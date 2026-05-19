# Automation Index

## Available now

| Script / Tool | What it does | File |
|---------------|-------------|------|
| HTML to PDF | Convert any HTML report to PDF via Playwright | `scripts/html_to_pdf.py` |
| Airflow DAG generation | Generate DAGs from a pipeline description | `skills/dag-builder.md` |
| dbt run + test | Automated via dbt CLI in Airflow DAGs | See `prompts/dag-scaffold.md` |

## Patterns to still implement

- Scheduled Airflow DAG for recurring HTML → PDF report delivery
- dbt freshness checks as a pre-run gate in CI
- Slack alert on dbt test failure (hook into Airflow on_failure_callback)
- Azure DevOps pipeline trigger on dbt model change (PR automation)
