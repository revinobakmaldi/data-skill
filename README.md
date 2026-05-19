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
| `mcp/configs/` | Ready-to-use MCP server JSON configs |

---

## Skills (Claude Code)

Drop the files in `skills/` into your Claude Code skills directory (`~/.claude/skills/`).

| Skill | What it does |
|-------|-------------|
| `dbt-model` | Generate dbt SQL + schema.yml + tests from a source table |
| `sql-analyst` | Answer business questions with production BigQuery SQL |
| `insight-writer` | Turn KPI data into executive narratives |
| `dag-builder` | Generate Airflow DAGs from a pipeline description |

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
| `powerbi-mcp.json` | DAX generation, semantic model edits, Power BI report support |

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
| LLM | Anthropic Claude API (`claude-opus-4-6`) |

---

## Contributing

- Add a skill: create `skills/your-skill-name.md` following the format of existing skills
- Add a prompt: create `prompts/your-prompt-name.md` with template + example
- Add a script: add to `scripts/`, include usage in docstring, update this README
