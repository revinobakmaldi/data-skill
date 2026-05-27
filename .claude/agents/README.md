# Claude Code agents

These are project-level Claude Code subagents for BI build and BI operations work.

They are designed to align first with the `data-goblin/power-bi-agentic-development` marketplace plugins.
Reference: `../plugins/power-bi-agentic-development.md`

## Agent set

- `bi-intake-manager`
- `semantic-model-architect`
- `powerbi-build-agent`
- `bi-ops-agent`
- `qa-reconciliation-agent`
- `bi-documentation-agent`

## Suggested usage

- New dashboard request:
  `Use the bi-intake-manager subagent, then semantic-model-architect, then powerbi-build-agent, then qa-reconciliation-agent.`
- Existing report incident:
  `Use the bi-ops-agent to triage this issue, then qa-reconciliation-agent before we close it.`
- Documentation follow-up:
  `Use the bi-documentation-agent to turn the accepted change into a metric note and changelog entry.`

## Design intent

- Narrow responsibilities beat one general BI bot.
- `semantic-model-architect` protects long-term model quality.
- `bi-ops-agent` protects your time from support churn.
- `qa-reconciliation-agent` protects trust in numbers.

## Plugin expectation

- Preferred Power BI integration: `data-goblin/power-bi-agentic-development`
- Preferred child plugins:
  - `pbip`
  - `pbi-desktop`
  - `semantic-models`
  - `reports`
- Use those plugin workflows first for semantic-model inspection, DAX validation, PBIP validation, report manipulation, and trace-based diagnosis.
- Treat standalone MCP use as secondary in this repo.
