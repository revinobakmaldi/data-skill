# data-skill

Repo contains AI skills of data team, including data engineering, modeling, analyst, and scientist.

Shortlist of MCPs, templates, and agentic skill repositories for practical data-team AI workflows.

This file is a living shortlist. More links can be appended as they come in.

## Repo structure

- `TEAM_WORKFLOW_MAP.html` , visual workflow map
- `REAL_RESOURCES.md` , real internet resources mapped to the workflow
- `catalog/real-workflow-resources.yaml` , machine-readable stage-to-resource mapping
- `mcp/` , MCP references used in the workflow
- `tools/` , tool and automation references
- `automation/` , automation pattern index
- `SKILLS_INDEX.md` , quick directory of real external resources

## Important

The previous internal starter skill files were placeholders. Use `REAL_RESOURCES.md` and `catalog/real-workflow-resources.yaml` as the source of truth for real external skills, MCPs, and tools.

## Current shortlist

| Name | Type | Link | Why it matters | Priority | Action |
|---|---|---|---|---|---|
| Google MCP Toolbox for Databases | General data / database MCP | https://github.com/googleapis/mcp-toolbox | Strong cross-stack MCP for database access, schema discovery, SQL workflows, and warehouse connectivity across many data platforms | High | Track closely |
| Microsoft Power BI Modeling MCP | Core Power BI MCP | https://github.com/microsoft/powerbi-modeling-mcp | Best official MCP for Power BI semantic modeling, DAX validation, and PBIP/TMDL workflows | High | Keep |
| data-goblin Power BI Agentic Development | Skill marketplace / plugin library | https://github.com/data-goblin/power-bi-agentic-development | Broad reusable library of Power BI agent resources, plugins, skills, hooks, and workflows | High | Reference and selectively reuse |
| RuiRomano Power BI Agentic MCP Cloud Agent | Workflow template | https://github.com/RuiRomano/powerbi-agentic-mcp-cloud-agent | Clean example of how to wire PBIP, Copilot agent, MCP, issues, and PR-based workflows together | Medium | Reference and adapt |

## Recommended classification

### 1. Core MCPs
These are the actual engines/tools that give AI capabilities.

- Google MCP Toolbox for Databases
- Microsoft Power BI Modeling MCP

### 2. Workflow templates
These show how to organize AI work around MCPs.

- RuiRomano Power BI Agentic MCP Cloud Agent

### 3. Skill libraries / marketplaces
These provide reusable skills, plugins, hooks, and patterns.

- data-goblin Power BI Agentic Development

## Current recommendation

If the team wants a tight, high-signal starting point:

1. Use **Google MCP Toolbox for Databases** for broader data and database workflows.
2. Use **Microsoft Power BI Modeling MCP** for Power BI-specific modeling work.
3. Mine **data-goblin/power-bi-agentic-development** for reusable Power BI skills.
4. Use **RuiRomano/powerbi-agentic-mcp-cloud-agent** only as a workflow example when needed.

## Next skill categories to add

- SQL generation and safe query workflows
- Schema exploration and metadata discovery
- BigQuery / warehouse AI workflows
- DAX generation
- DAX debugging
- Semantic model documentation
- Naming convention audit and cleanup
- Performance tuning

## Notes

- This shortlist is intentionally trimmed.
- Keep only tools that are either broadly useful for the data team or clearly best-in-class for Power BI.
