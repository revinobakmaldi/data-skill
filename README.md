# data-skill

Shortlist of MCPs, templates, and agentic skill repositories for data work, starting with Power BI and related AI-assisted development workflows.

This file is a living shortlist. More links can be appended as they come in.

## Current shortlist

| Name | Type | Link | Why it matters | Priority | Action |
|---|---|---|---|---|---|
| Microsoft Power BI Modeling MCP | Core MCP | https://github.com/microsoft/powerbi-modeling-mcp | Official Microsoft MCP for Power BI semantic modeling, DAX validation, bulk refactoring, PBIP/TMDL workflows | High | Track closely |
| Microsoft Remote Power BI MCP | Hosted MCP | https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started | Official hosted MCP for querying published semantic models with AI | High | Reference |
| RuiRomano Power BI Agentic MCP Cloud Agent | Workflow template | https://github.com/RuiRomano/powerbi-agentic-mcp-cloud-agent | Good example of combining PBIP, GitHub Copilot coding agent, Power BI Modeling MCP, issues, and PR-based workflows | High | Reference and adapt |
| data-goblin Power BI Agentic Development | Skill marketplace / plugin library | https://github.com/data-goblin/power-bi-agentic-development | Broad collection of Power BI agent resources, plugins, skills, hooks, and workflows | High | Reference and selectively reuse |
| sulaiman013 Power BI MCP | Community MCP | https://github.com/sulaiman013/powerbi-mcp | Interesting community implementation with PBIP-safe refactoring ideas, Desktop + Service connectivity, and RLS testing | Medium | Reference |
| SemanticOps MCP | Commercial MCP tool | https://github.com/maxanatsko/mcp-engine-public | Practical local AI workflow for Power BI Desktop with strong safety positioning | Medium | Evaluate |
| Google MCP Toolbox for Databases | General data / database MCP | https://github.com/googleapis/mcp-toolbox | Official Google open source MCP toolbox for connecting AI agents to databases like BigQuery, PostgreSQL, MySQL, SQL Server, Snowflake, Neo4j, and more | High | Reference and evaluate for broader data stack |

## Recommended classification

### 1. Core MCPs
These are the actual engines/tools that give AI capabilities.

- Microsoft Power BI Modeling MCP
- Microsoft Remote Power BI MCP
- sulaiman013 Power BI MCP
- SemanticOps MCP

### 1b. General data platform MCPs
These are not Power BI-specific, but they are highly relevant for AI-assisted data engineering, analytics, and database workflows.

- Google MCP Toolbox for Databases

### 2. Workflow templates
These show how to organize AI work around MCPs.

- RuiRomano Power BI Agentic MCP Cloud Agent

### 3. Skill libraries / marketplaces
These provide reusable skills, plugins, hooks, and patterns.

- data-goblin Power BI Agentic Development

## Current recommendation

If the team wants the highest-value starting point for Power BI:

1. Start with **Microsoft Power BI Modeling MCP** as the core foundation.
2. Use **RuiRomano/powerbi-agentic-mcp-cloud-agent** as a workflow example.
3. Mine **data-goblin/power-bi-agentic-development** for reusable team skills and plugin ideas.

If the repo is expanding into broader data and database work too:

4. Add **Google MCP Toolbox for Databases** as a cross-stack MCP option for BigQuery, PostgreSQL, MySQL, SQL Server, Snowflake, and related database workflows.

## Next skill categories to add

- DAX generation
- DAX debugging
- Semantic model documentation
- Naming convention audit and cleanup
- Measure refactoring
- RLS review and testing
- Performance tuning
- PBIP-safe bulk rename workflows
- Report review and QA
- Fabric workspace / deployment workflow support
- SQL generation and safe query workflows
- Schema exploration and metadata discovery
- BigQuery / warehouse AI workflows

## Notes

- Some repos above are under active development and may change structure quickly.
- Prefer official Microsoft MCPs for core capability.
- Prefer community/template repos for workflow inspiration, not blind standardization.
