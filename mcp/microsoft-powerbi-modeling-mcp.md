# Microsoft Power BI Modeling MCP

- Source: https://github.com/microsoft/powerbi-modeling-mcp
- Config: `mcp/configs/powerbi-mcp.json`

## What it provides

Direct access to Power BI semantic models from Claude Code:
- DAX measure generation and explanation
- Semantic model table, column, and relationship inspection
- Auto-documentation of measures and columns
- Naming convention enforcement
- DAX syntax validation before applying changes

## Workflow stage

Best used in Stage 05 (Analytics product build) when building or maintaining Power BI reports.

## Setup

See `mcp/configs/powerbi-mcp.json` for the full config and auth requirements.
