# Skills Index

Quick reference for all skills in this repo. Copy any file to `~/.claude/skills/` to use it in Claude Code.

---

## Custom (built for this team)

| File | Trigger | Use for |
|------|---------|---------|
| `skills/dbt-model.md` | "create a dbt model for..." | Generate staging/intermediate/mart SQL + schema.yml + tests |
| `skills/sql-analyst.md` | "write SQL for..." | Business question → production BigQuery SQL |
| `skills/insight-writer.md` | "write a narrative for..." | KPI table → executive summary |
| `skills/dag-builder.md` | "create an Airflow DAG for..." | Pipeline description → Airflow DAG |
| `skills/data-analyst.md` | "analyze this data: ..." | Paste data → trend/anomaly analysis |
| `skills/azure-devops.md` | "create a work item for..." | Azure DevOps — boards, repos, PRs, wiki |

---

## From dbt-labs/dbt-agent-skills (Apache-2.0)

Source: https://github.com/dbt-labs/dbt-agent-skills · ⭐ 509

| File | Use for |
|------|---------|
| `skills/dbt-labs/using-dbt-for-analytics-engineering.md` | Full dbt workflow — building, testing, documenting |
| `skills/dbt-labs/adding-dbt-unit-test.md` | Add unit tests (dict/csv/sql format) |
| `skills/dbt-labs/troubleshooting-dbt-job-errors.md` | Diagnose and fix dbt job failures |
| `skills/dbt-labs/running-dbt-commands.md` | CLI: selectors, variables, deferral |
| `skills/dbt-labs/answering-natural-language-questions-with-dbt.md` | Query semantic layer in plain English |
| `skills/dbt-labs/building-dbt-semantic-layer.md` | Build semantic models, entities, metrics |

---

## From AltimateAI/data-engineering-skills (MIT)

Source: https://github.com/AltimateAI/data-engineering-skills · ⭐ 93

| File | Use for |
|------|---------|
| `skills/altimate-ai/creating-dbt-models.md` | Full dbt model creation workflow |
| `skills/altimate-ai/debugging-dbt-errors.md` | Debug errors with 3-failure methodology |
| `skills/altimate-ai/testing-dbt-models.md` | Add generic and custom tests |
| `skills/altimate-ai/migrating-sql-to-dbt.md` | Convert legacy SQL to dbt layer-by-layer |
| `skills/altimate-ai/developing-incremental-models.md` | Incremental strategies and late-arriving data |

---

## From alirezarezvani/claude-skills (MIT)

Source: https://github.com/alirezarezvani/claude-skills · ⭐ 15,411

| File | Use for |
|------|---------|
| `skills/community/senior-data-engineer.md` | DE persona — architecture, pipelines, best practices |
| `skills/community/senior-data-scientist.md` | DS persona — modeling, experimentation, ML |
| `skills/community/senior-ml-engineer.md` | MLE persona — model deployment, MLOps |
| `skills/community/sql-database-assistant.md` | SQL expert — query writing, optimization, schema design |
| `skills/community/data-quality-auditor.md` | Data quality audit — profiling, validation, issue detection |

---

---

## From data-goblin/power-bi-agentic-development (MIT)

Source: https://github.com/data-goblin/power-bi-agentic-development

Install via Claude Code plugin marketplace (not copied to `~/.claude/skills/`):
```bash
claude plugin marketplace add data-goblin/power-bi-agentic-development
```

| Plugin | Use for |
|--------|---------|
| `plugins/power-bi-agentic-development/plugins/pbip` | PBIR metadata editing: visual.json, report.json, themes, filters (requires PBIP format) |
| `plugins/power-bi-agentic-development/plugins/reports` | Deneb/Vega-Lite visuals, SVG via DAX, theme JSON, pbir-cli |
| `plugins/power-bi-agentic-development/plugins/pbi-desktop` | Live model exploration and real-time DAX query capture |
| `plugins/power-bi-agentic-development/plugins/semantic-models` | DAX, Power Query, naming conventions, lineage, refresh |
| `plugins/power-bi-agentic-development/plugins/tabular-editor` | BPA rules, C# macros, Tabular Editor 2 CLI |
| `plugins/power-bi-agentic-development/plugins/fabric-cli` | Remote Fabric ops, tenant audits, governance |

---

## Prompt Templates (prompts/)

Not skills — copy-paste prompts for one-off tasks.

| File | Use for |
|------|---------|
| `prompts/sql-from-question.md` | Business question → SQL |
| `prompts/dbt-model-generator.md` | Source schema → dbt model package |
| `prompts/insight-to-narrative.md` | KPI table → executive narrative |
| `prompts/data-quality-checks.md` | Table profile → dbt-expectations checks |
| `prompts/dashboard-wireframe.md` | Brief → HTML dashboard prototype |
| `prompts/dag-scaffold.md` | Pipeline description → Airflow DAG |
