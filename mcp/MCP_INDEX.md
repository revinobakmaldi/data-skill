# MCP Index

All MCP server configs are in `mcp/configs/`. Each file is ready to paste into `claude_desktop_config.json` or use with the Claude Code CLI.

## Configured MCPs

| Config file | MCP | Use for |
|-------------|-----|---------|
| `configs/bigquery-toolbox.json` + `configs/toolbox-config.yaml` | Google MCP Toolbox | BigQuery schema discovery, SQL execution, data profiling |
| `configs/dbt-mcp.json` | dbt MCP (dbt-labs) | dbt model exploration, semantic layer queries, dbt commands |
| `configs/powerbi-mcp.json` | Power BI Modeling MCP (Microsoft) | DAX generation, semantic model edits, Power BI support |
| `configs/azure-devops-mcp.json` | Azure DevOps MCP (Microsoft, ⭐ 1,693) | Work items, repos, PRs, pipelines, wiki |

## Quickstart (Claude Code CLI)

```bash
# BigQuery (after configuring toolbox-config.yaml)
claude mcp add bigquery -- python -m toolbox.server

# dbt
claude mcp add dbt -- python -m dbt_mcp.server

# Azure DevOps
claude mcp add azure-devops -- npx -y @azure-devops/mcp YOUR_ORG_NAME
```

## Rule of thumb

- **BigQuery Toolbox**: source discovery, schema exploration, running SQL, data profiling
- **dbt MCP**: semantic layer queries, model exploration, dbt command execution
- **Power BI MCP**: DAX generation, semantic model edits, report support
- **Azure DevOps MCP**: task management, repo and PR workflows, pipeline status, wiki docs
