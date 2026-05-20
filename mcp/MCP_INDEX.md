# MCP Index

MCP servers give Claude direct tool-call access to external services. Claude Code Plugins are skills/agents installed via the plugin marketplace — a different layer.

---

## MCP Servers (`mcp/configs/`)

Ready to paste into `claude_desktop_config.json` or register with `claude mcp add`.

| Config file | MCP | Use for |
|-------------|-----|---------|
| `configs/bigquery-toolbox.json` + `configs/toolbox-config.yaml` | Google MCP Toolbox | BigQuery schema discovery, SQL execution, data profiling |
| `configs/dbt-mcp.json` | dbt MCP (dbt-labs) | dbt model exploration, semantic layer queries, dbt commands |
| `configs/powerbi-mcp.json` | Power BI Modeling MCP (Microsoft) | Semantic model only: DAX, measures, tables, columns, relationships |
| `configs/azure-devops-mcp.json` | Azure DevOps MCP (Microsoft) | Work items, repos, PRs, pipelines, wiki |

### Quickstart (Claude Code CLI)

```bash
# BigQuery (after configuring toolbox-config.yaml)
claude mcp add bigquery -- python -m toolbox.server

# dbt
claude mcp add dbt -- python -m dbt_mcp.server

# Power BI Modeling (semantic model only — NOT report/visual editing)
claude mcp add powerbi-modeling-mcp -- npx -y @microsoft/powerbi-modeling-mcp@latest --start

# Azure DevOps
claude mcp add azure-devops -- npx -y @azure-devops/mcp YOUR_ORG_NAME
```

---

## Claude Code Plugin Marketplace (`plugins/`)

Installed once via `claude plugin marketplace add`. Provides skills, agents, and hooks — not MCP tool calls.

| Plugin | Source | Use for |
|--------|--------|---------|
| `power-bi-agentic-development` | data-goblin (MIT) | Report/visual editing (PBIP), Deneb visuals, Tabular Editor, Fabric CLI, semantic model auditing |

### Install

```bash
claude plugin marketplace add data-goblin/power-bi-agentic-development
```

Individual plugins within the marketplace:

| Plugin name | Use for |
|-------------|---------|
| `pbip` | PBIR metadata: visual.json, report.json, themes, filters — requires PBIP format |
| `reports` | Deneb/Vega-Lite visuals, SVG via DAX, theme JSON, pbir-cli manipulation |
| `pbi-desktop` | Live model exploration and DAX query capture from running PBI Desktop |
| `semantic-models` | DAX, Power Query, naming conventions, refresh, lineage auditing |
| `tabular-editor` | BPA rules, C# macros, Tabular Editor 2 CLI automation |
| `fabric-cli` | Remote Fabric operations, tenant audits, governance |

---

## Rule of thumb

- **Power BI semantic model** (measures, tables, DAX) → use `powerbi-modeling-mcp` (MCP server, live tool calls)
- **Power BI report/visual editing** (pages, visuals, themes) → use `data-goblin pbip + reports` plugins (requires saving file as PBIP first)
- **BigQuery**: source discovery, SQL execution → Google MCP Toolbox
- **dbt**: model exploration, semantic layer → dbt MCP
- **Azure DevOps**: boards, PRs, pipelines → Azure DevOps MCP
