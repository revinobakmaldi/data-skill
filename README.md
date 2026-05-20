# data-skill

AI skills, tools, and MCP configs that supercharge the analytics team.
Designed for use with **Claude Code**, **AWS Kiro**, **Codex**, and other AI coding assistants.

---

## What's in here

| Directory | What it is |
|-----------|-----------|
| `CLAUDE.md` | Main instructions for Claude Code and AI assistants |
| `AGENTS.md` | Instructions for Codex, Copilot Workspace, and agent-based tools |
| `skills/` | Claude Code skill files — invoke with `/skill-name` |
| `prompts/` | Copy-paste prompt templates for daily analytics tasks |
| `scripts/` | Working Python scripts for data ops |
| `mcp/configs/` | Ready-to-use MCP server JSON configs (live tool-call integrations) |
| `plugins/` | Claude Code plugin marketplaces (skills, agents, hooks installed via `claude plugin marketplace add`) |

---

## Skills (Claude Code)

Drop the files in `skills/` into your Claude Code skills directory (`~/.claude/skills/`).

### Custom skills (built for this team)

| Skill | What it does |
|-------|-------------|
| `dbt-model` | Generate dbt SQL + schema.yml + tests from a source table |
| `sql-analyst` | Answer business questions with production BigQuery SQL |
| `insight-writer` | Turn KPI data into executive narratives |
| `dag-builder` | Generate Airflow DAGs from a pipeline description |
| `data-analyst` | Analyze pasted data tables and answer business questions |

### From dbt-labs/dbt-agent-skills (Apache-2.0)

Source: https://github.com/dbt-labs/dbt-agent-skills

| Skill | What it does |
|-------|-------------|
| `dbt-labs/using-dbt-for-analytics-engineering` | Core dbt workflow — model building, testing, documentation |
| `dbt-labs/adding-dbt-unit-test` | Add unit tests to dbt models (dict/csv/sql formats) |
| `dbt-labs/troubleshooting-dbt-job-errors` | Diagnose and fix dbt job failures |
| `dbt-labs/running-dbt-commands` | CLI execution, selectors, variables, deferral |
| `dbt-labs/answering-natural-language-questions-with-dbt` | Query semantic layer with natural language |
| `dbt-labs/building-dbt-semantic-layer` | Build semantic models, entities, and metrics |

### From AltimateAI/data-engineering-skills (MIT)

Source: https://github.com/AltimateAI/data-engineering-skills

| Skill | What it does |
|-------|-------------|
| `altimate-ai/creating-dbt-models` | Full dbt model creation workflow with conventions |
| `altimate-ai/debugging-dbt-errors` | Debug errors with 3-failure rule methodology |
| `altimate-ai/testing-dbt-models` | Add generic and custom tests to models |
| `altimate-ai/migrating-sql-to-dbt` | Convert existing SQL to dbt layer-by-layer |
| `altimate-ai/developing-incremental-models` | Incremental strategies, unique keys, late-arriving data |

### From alirezarezvani/claude-skills (MIT)

Source: https://github.com/alirezarezvani/claude-skills

| Skill | What it does |
|-------|-------------|
| `community/senior-data-engineer` | Senior DE persona — architecture, pipelines, best practices |
| `community/senior-data-scientist` | Senior DS persona — modeling, experimentation, ML workflows |
| `community/senior-ml-engineer` | Senior MLE persona — model deployment, MLOps |
| `community/sql-database-assistant` | SQL expert — query writing, optimization, schema design |
| `community/data-quality-auditor` | Data quality audit — profiling, validation, issue detection |

---

## Prompt Templates

Copy-paste prompts for tasks you do regularly.

| Prompt | Use it for |
|--------|-----------|
| `sql-from-question.md` | Business question → SQL |
| `dbt-model-generator.md` | Source schema → full dbt model package |
| `insight-to-narrative.md` | KPI table → executive summary |
| `data-quality-checks.md` | Table profile → dbt-expectations / GE tests |
| `dashboard-wireframe.md` | Dashboard brief → HTML prototype |
| `dag-scaffold.md` | Pipeline description → Airflow DAG |

---

## MCP Server Configs

JSON snippets ready to paste into `claude_desktop_config.json`.

| Config | What it gives you |
|--------|------------------|
| `bigquery-toolbox.json` | BigQuery schema discovery + SQL execution via Google MCP Toolbox |
| `toolbox-config.yaml` | Tool definitions: list tables, describe columns, profile data, run SQL |
| `dbt-mcp.json` | dbt model exploration, semantic queries, dbt commands |
| `powerbi-mcp.json` | Semantic model only: DAX generation, measures, tables, columns, relationships |

### Quickstart (Claude Desktop)

1. Open `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Merge the `mcpServers` block from the config file you want
3. Update the env vars (project ID, workspace ID, etc.)
4. Restart Claude Desktop

---

## Scripts

| Script | Usage |
|--------|-------|
| `scripts/data_to_claude.py` | `python scripts/data_to_claude.py --file data.csv --question "What are the trends?"` |
| `scripts/html_to_pdf.py` | `python scripts/html_to_pdf.py report.html -o report.pdf` |

### data_to_claude.py requirements
```bash
pip install anthropic pandas tabulate
export ANTHROPIC_API_KEY=sk-ant-...
```

### html_to_pdf.py requirements
```bash
pip install playwright
playwright install chromium
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

---

## Contributing

- Add a skill: create `skills/your-skill-name.md` following the format of existing skills
- Add a prompt: create `prompts/your-prompt-name.md` with template + example
- Add a script: add to `scripts/`, include usage in docstring, update this README
