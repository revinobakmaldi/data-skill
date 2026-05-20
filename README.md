# data-skill

AI skills, tools, MCP configs, and plugins for the analytics team.
Works with **Claude Code**, **AWS Kiro**, **Codex**, and other AI coding assistants.

---

## Repo Structure

| Path | What it is |
|------|-----------|
| `CLAUDE.md` | AI assistant instructions — conventions, tools, what to use for what |
| `skills/` | Claude Code skill files (copy to `~/.claude/skills/`) |
| `prompts/` | Copy-paste prompt templates for daily tasks |
| `scripts/` | Working Python scripts for data ops |
| `mcp/configs/` | MCP server JSON configs — live tool-call integrations |
| `plugins/` | Claude Code plugin marketplaces — skills/agents/hooks installed via CLI |

---

## Skills

### Custom (built for this team)

Copy files from `skills/` to `~/.claude/skills/` to activate.

| Skill | Trigger | What it does |
|-------|---------|-------------|
| `skills/dbt-model.md` | "create a dbt model for..." | Generate staging/intermediate/mart SQL + schema.yml + tests |
| `skills/sql-analyst.md` | "write SQL for..." | Business question → production BigQuery SQL |
| `skills/insight-writer.md` | "write a narrative for..." | KPI table → executive summary |
| `skills/dag-builder.md` | "create an Airflow DAG for..." | Pipeline description → Airflow DAG |
| `skills/data-analyst.md` | "analyze this data: ..." | Paste data → trend/anomaly analysis |
| `skills/azure-devops.md` | "create a work item for..." | Azure DevOps — boards, repos, PRs, wiki |

### From dbt-labs/dbt-agent-skills (Apache-2.0)

Source: https://github.com/dbt-labs/dbt-agent-skills

| Skill | What it does |
|-------|-------------|
| `skills/dbt-labs/using-dbt-for-analytics-engineering.md` | Core dbt workflow — building, testing, documentation |
| `skills/dbt-labs/adding-dbt-unit-test.md` | Add unit tests (dict/csv/sql formats) |
| `skills/dbt-labs/troubleshooting-dbt-job-errors.md` | Diagnose and fix dbt job failures |
| `skills/dbt-labs/running-dbt-commands.md` | CLI: selectors, variables, deferral |
| `skills/dbt-labs/answering-natural-language-questions-with-dbt.md` | Query semantic layer in plain English |
| `skills/dbt-labs/building-dbt-semantic-layer.md` | Build semantic models, entities, metrics |

### From AltimateAI/data-engineering-skills (MIT)

Source: https://github.com/AltimateAI/data-engineering-skills

| Skill | What it does |
|-------|-------------|
| `skills/altimate-ai/creating-dbt-models.md` | Full dbt model creation workflow |
| `skills/altimate-ai/debugging-dbt-errors.md` | Debug errors with 3-failure methodology |
| `skills/altimate-ai/testing-dbt-models.md` | Add generic and custom tests |
| `skills/altimate-ai/migrating-sql-to-dbt.md` | Convert legacy SQL to dbt layer-by-layer |
| `skills/altimate-ai/developing-incremental-models.md` | Incremental strategies and late-arriving data |

### From alirezarezvani/claude-skills (MIT)

Source: https://github.com/alirezarezvani/claude-skills

| Skill | What it does |
|-------|-------------|
| `skills/community/senior-data-engineer.md` | Senior DE persona — architecture, pipelines, best practices |
| `skills/community/senior-data-scientist.md` | Senior DS persona — modeling, experimentation, ML |
| `skills/community/senior-ml-engineer.md` | Senior MLE persona — model deployment, MLOps |
| `skills/community/sql-database-assistant.md` | SQL expert — query writing, optimization, schema design |
| `skills/community/data-quality-auditor.md` | Data quality audit — profiling, validation, issue detection |

---

## Claude Code Plugins

Installed via `claude plugin marketplace add` — provides skills, agents, and hooks. Not MCP servers.

### data-goblin/power-bi-agentic-development (MIT)

Source: https://github.com/data-goblin/power-bi-agentic-development  
Location: `plugins/power-bi-agentic-development/`

```bash
claude plugin marketplace add data-goblin/power-bi-agentic-development
```

| Plugin | What it does |
|--------|-------------|
| `pbip` | PBIR metadata editing: visual.json, report.json, themes, filters — requires PBIP format |
| `reports` | Deneb/Vega-Lite visuals, SVG via DAX, theme JSON, pbir-cli manipulation |
| `pbi-desktop` | Live model exploration and real-time DAX query capture from running PBI Desktop |
| `semantic-models` | DAX, Power Query, naming conventions, lineage, refresh troubleshooting |
| `tabular-editor` | BPA rules, C# macros, Tabular Editor 2 CLI automation |
| `fabric-cli` | Remote Fabric operations, tenant audits, governance |

> **Note:** `pbip` and `reports` plugins require saving the `.pbix` file as a Power BI Project (PBIP) first: File → Save as → Power BI Project.

---

## MCP Servers

MCP servers give Claude direct tool-call access. Register once with `claude mcp add`.

| Config | MCP | Use for |
|--------|-----|---------|
| `mcp/configs/bigquery-toolbox.json` + `toolbox-config.yaml` | Google MCP Toolbox | BigQuery schema discovery, SQL execution, data profiling |
| `mcp/configs/dbt-mcp.json` | dbt MCP (dbt-labs) | dbt model exploration, semantic layer queries, dbt commands |
| `mcp/configs/powerbi-mcp.json` | Power BI Modeling MCP (Microsoft) | Semantic model only: DAX, measures, tables, columns, relationships |
| `mcp/configs/azure-devops-mcp.json` | Azure DevOps MCP (Microsoft) | Work items, repos, PRs, pipelines, wiki |

**Google MCP Toolbox tools:** `list-datasets`, `list-tables`, `describe-table`, `run-sql`, `sample-table`, `profile-column`

### Quickstart

```bash
# Power BI Modeling (semantic model — NOT report/visual editing)
claude mcp add powerbi-modeling-mcp -- npx -y @microsoft/powerbi-modeling-mcp@latest --start

# BigQuery (after configuring toolbox-config.yaml)
claude mcp add bigquery -- python -m toolbox.server

# dbt
claude mcp add dbt -- python -m dbt_mcp.server

# Azure DevOps
claude mcp add azure-devops -- npx -y @azure-devops/mcp YOUR_ORG_NAME
```

---

## Prompt Templates

Copy-paste prompts for one-off tasks (not skills).

| Prompt | Use it for |
|--------|-----------|
| `prompts/sql-from-question.md` | Business question → SQL |
| `prompts/dbt-model-generator.md` | Source schema → full dbt model package |
| `prompts/insight-to-narrative.md` | KPI table → executive summary |
| `prompts/data-quality-checks.md` | Table profile → dbt-expectations checks |
| `prompts/dashboard-wireframe.md` | Dashboard brief → HTML prototype |
| `prompts/dag-scaffold.md` | Pipeline description → Airflow DAG |

---

## Scripts

| Script | Usage |
|--------|-------|
| `scripts/data_to_claude.py` | `python scripts/data_to_claude.py --file data.csv --question "What are the trends?"` |
| `scripts/html_to_pdf.py` | `python scripts/html_to_pdf.py report.html -o report.pdf` |

```bash
# data_to_claude.py deps
pip install anthropic pandas tabulate

# html_to_pdf.py deps
pip install playwright && playwright install chromium
```

---

## Team Stack

| Layer | Tool |
|-------|------|
| Orchestration | Apache Airflow |
| Transformation | dbt Core |
| Data warehouse | BigQuery |
| Data quality | dbt-expectations + Great Expectations |
| BI | Power BI + HTML reports |
| LLM / AI coding | Claude Code (CLI) |
| Scripting | Python 3.11+ |

---

## External Resources

Key open-source tools mapped to each workflow stage.

**Ingestion:** [Airbyte](https://github.com/airbytehq/airbyte), [dlt](https://github.com/dlt-hub/dlt), [Airflow](https://github.com/apache/airflow)  
**Transformation:** [dbt-core](https://github.com/dbt-labs/dbt-core), [dbt-utils](https://github.com/dbt-labs/dbt-utils), [dbt-project-evaluator](https://github.com/dbt-labs/dbt-project-evaluator)  
**Data quality:** [Great Expectations](https://github.com/great-expectations/great_expectations), [dbt-expectations](https://github.com/calogica/dbt-expectations), [Elementary](https://github.com/elementary-data/elementary)  
**BI / reporting:** [Quarto](https://github.com/quarto-dev/quarto-cli), [Evidence](https://github.com/evidence-dev/evidence), [Playwright](https://github.com/microsoft/playwright)  
**ML / experimentation:** [MLflow](https://github.com/mlflow/mlflow), [scikit-learn](https://github.com/scikit-learn/scikit-learn), [Featuretools](https://github.com/alteryx/featuretools)  
**LLM observability:** [Langfuse](https://github.com/langfuse/langfuse), [Evidently](https://github.com/evidentlyai/evidently), [promptfoo](https://github.com/promptfoo/promptfoo)

### Configured in this repo

| Status | Resource | Location |
|--------|----------|----------|
| ✅ | googleapis/mcp-toolbox | `mcp/configs/bigquery-toolbox.json` |
| ✅ | dbt-labs/dbt-mcp | `mcp/configs/dbt-mcp.json` |
| ✅ | microsoft/powerbi-modeling-mcp | `mcp/configs/powerbi-mcp.json` (semantic model only) |
| ✅ | data-goblin/power-bi-agentic-development | `plugins/power-bi-agentic-development/` |
| ✅ | microsoft/azure-devops-mcp | `mcp/configs/azure-devops-mcp.json` |
| ✅ | microsoft/playwright | `scripts/html_to_pdf.py` |
| ⬜ | apache/airflow | install separately |
| ⬜ | dbt-labs/dbt-core | install separately |
| ⬜ | elementary-data/elementary | install as dbt package |
| ⬜ | airbytehq/airbyte | deploy separately |

---

## Contributing

- Add a skill: create `skills/your-skill-name.md` following existing format
- Add a prompt: create `prompts/your-prompt-name.md` with template + example
- Add a script: add to `scripts/`, include usage in docstring
