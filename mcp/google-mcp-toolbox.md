# Google MCP Toolbox

- Source: https://github.com/googleapis/mcp-toolbox
- Config: `mcp/configs/bigquery-toolbox.json` + `mcp/configs/toolbox-config.yaml`

## What it provides

Cross-stack data access for Claude Code. Configured for BigQuery with these tools:
- `list-datasets` — list all datasets in the project
- `list-tables` — list tables in a dataset with row count and size
- `describe-table` — get column names, types, and descriptions
- `run-sql` — execute a read-only SQL query (max 1000 rows)
- `sample-table` — preview first N rows of any table
- `profile-column` — null rate, distinct count, min/max for a column

## Setup

See `mcp/configs/bigquery-toolbox.json` for the full config and setup steps.
