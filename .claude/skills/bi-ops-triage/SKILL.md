---
description: Triage and structure Power BI operations incidents such as refresh failures, wrong numbers, access issues, or performance regressions. Use for existing report support work.
when_to_use: Prefer when a report already exists and the main task is diagnose, contain, fix, or communicate.
---

# BI ops triage

Use this skill to make support work systematic instead of reactive.

## Preferred plugin routing

- `pbi-desktop@power-bi-agentic-development` for live Desktop inspection and query capture
- `pbip@power-bi-agentic-development` for PBIP validation and structure issues
- `semantic-models@power-bi-agentic-development` for model audits and DAX/model quality checks

## Workflow

1. Classify the incident using `references/incident-types.md`.
2. Draft the incident response using `templates/incident-template.md`.
3. Separate:
   - evidence
   - hypothesis
   - containment
   - durable fix
4. If numbers changed, hand off to `bi-reconciliation-gate`.
5. If stakeholder messaging is needed, produce a separate short update.

## Rules

- Do not confuse symptoms with root cause.
- Prefer deterministic validation and plugin workflows before speculation.
- Name the likely failure layer: source, model, report, access, or refresh/orchestration.

## Supporting files

- `templates/incident-template.md`
- `references/incident-types.md`
