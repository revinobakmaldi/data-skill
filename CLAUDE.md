# Data Team — AI Assistant Instructions

Read by Claude Code, AWS Kiro, Codex, GitHub Copilot Workspace, and other AI coding assistants.

---

## Stack

| Layer | Tool | Location |
|-------|------|----------|
| Orchestration | Apache Airflow | `dags/`, connections in Airflow UI |
| Transformation | dbt Core | `models/`, profiles in `~/.dbt/profiles.yml` |
| Data warehouse | BigQuery | project: `your-gcp-project`, dataset prefix: `analytics_` |
| Data quality | dbt-expectations + Great Expectations | |
| BI / reporting | Power BI + HTML reports (Playwright) | |
| LLM / AI coding | Claude Code (CLI) | |
| Scripting | Python 3.11+ | `scripts/` |

---

## Data Layer Boundaries

```
Source DB / APIs
      ↓
  [Airbyte / dlt]         ← ingestion (raw, untransformed)
      ↓
  BigQuery: raw_*          ← never modified by dbt
      ↓
  dbt staging (stg_*)      ← clean, typed, renamed — no logic
      ↓
  dbt intermediate (int_*) ← joins, dedup, business rules
      ↓
  dbt mart (fct_/dim_*)    ← final, queryable by BI
      ↓
  Power BI / HTML reports  ← consumption layer
```

Do not skip layers. Build intermediate models before mart models if something is missing.

---

## Conventions

### dbt
- Staging: `stg_{source}__{entity}.sql` — rename + cast only, no business logic
- Intermediate: `int_{domain}_{description}.sql` — joins, dedup, business rules
- Mart: `fct_{entity}.sql` / `dim_{entity}.sql` — final grain, no logic
- Every model needs `schema.yml` with column descriptions and tests
- Use `{{ source() }}` in staging, `{{ ref() }}` everywhere else
- Required tests on every primary key: `unique` + `not_null`
- Use `dbt-expectations` for range checks, `relationships` for FK integrity

### Airflow DAGs
- File naming: `{frequency}_{domain}_{description}_dag.py`
- Always set `catchup=False` and `max_active_runs=1`
- Schedule in UTC cron (server timezone: WIB/UTC+7, subtract 7h)
- Retry: `retries=2, retry_delay=timedelta(minutes=5)`
- On failure: Slack alert to `#data-alerts`
- Use Airflow UI connections — never hardcode credentials

### Python
- Python 3.11+, type hints required
- Use `argparse` for CLI scripts
- Check required env vars at startup, exit with clear error if missing
- No hardcoded credentials — use env vars or secret manager

### SQL
- BigQuery dialect unless stated otherwise
- Use CTEs, never nested subqueries
- Explicit column lists — no `SELECT *` in production
- Filter out deleted/test records unless analysis specifically needs them

---

## MCP Servers (live tool calls)

Register with `claude mcp add`. These give Claude direct programmatic access.

| MCP | Config | Use for |
|-----|--------|---------|
| Google MCP Toolbox | `mcp/configs/bigquery-toolbox.json` | BigQuery: list datasets/tables, describe columns, run SQL, profile data |
| dbt MCP | `mcp/configs/dbt-mcp.json` | dbt model exploration, semantic layer queries, dbt CLI commands |
| Power BI Modeling MCP | `mcp/configs/powerbi-mcp.json` | **Semantic model only**: DAX, measures, tables, columns, relationships |
| Azure DevOps MCP | `mcp/configs/azure-devops-mcp.json` | Work items, repos, PRs, pipelines, wiki |

```bash
claude mcp add powerbi-modeling-mcp -- npx -y @microsoft/powerbi-modeling-mcp@latest --start
claude mcp add bigquery -- python -m toolbox.server
claude mcp add dbt -- python -m dbt_mcp.server
claude mcp add azure-devops -- npx -y @azure-devops/mcp YOUR_ORG_NAME
```

---

## Claude Code Plugins (skills, agents, hooks)

Installed via plugin marketplace — not MCP servers. Provide skill docs and agents Claude reads and acts on.

| Plugin suite | Location | Use for |
|--------------|----------|---------|
| data-goblin/power-bi-agentic-development | `plugins/power-bi-agentic-development/` | Power BI report/visual editing, Deneb, Tabular Editor, Fabric CLI |

```bash
claude plugin marketplace add data-goblin/power-bi-agentic-development
```

Plugins within the suite:

| Plugin | Use for |
|--------|---------|
| `pbip` | PBIR metadata: visual.json, report.json, themes, filters — **requires PBIP format** |
| `reports` | Deneb/Vega-Lite visuals, SVG via DAX, theme JSON, pbir-cli |
| `pbi-desktop` | Live model exploration and DAX query capture from running PBI Desktop |
| `semantic-models` | DAX, Power Query, naming conventions, lineage, refresh |
| `tabular-editor` | BPA rules, C# macros, Tabular Editor 2 CLI |
| `fabric-cli` | Remote Fabric operations, tenant audits, governance |

**Power BI decision guide:**
- Semantic model work (DAX, measures, tables) → use **Power BI Modeling MCP**
- Report/visual editing (pages, visuals, themes) → use **data-goblin pbip + reports plugins** (save as PBIP first: File → Save as → Power BI Project)

---

## Common Tasks

### Generate a dbt model
See `prompts/dbt-model-generator.md`. Provide source table DDL + business context → get stg model + schema.yml.

### Write SQL from a business question
See `prompts/sql-from-question.md`. Always provide schema context and BigQuery dialect.

### Generate an Airflow DAG
See `prompts/dag-scaffold.md`. Provide: pipeline steps, schedule, connections, error handling requirements.

### Analyze data
```bash
python scripts/data_to_claude.py --file sales.csv --question "What are the top trends?"
```

### Convert HTML report to PDF
```bash
python scripts/html_to_pdf.py report.html -o report_output.pdf
```

### Testing (dbt)
After writing any dbt model: `dbt compile` → `dbt test --select <model_name>` → `dbt source freshness` (if new source added).

### Testing (Python)
After writing any script: `python <script>.py --help` → test with a small sample before large datasets.

---

## What NOT to do

- Never write to `raw_*` tables — they are owned by the ingestion layer
- Never use `SELECT *` in dbt models
- Never hardcode credentials, tokens, or connection strings
- Never skip `schema.yml` for a new model
- Never run `dbt run` without `dbt test` in a pipeline context
- Never push directly to `main` — use feature branches and PRs
