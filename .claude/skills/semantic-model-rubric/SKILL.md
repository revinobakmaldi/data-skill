---
description: Design or review a Power BI semantic model with explicit grain, relationship, measure, and performance checks. Use for semantic-model planning, audit, or major model changes.
when_to_use: Prefer before report build or when numbers, relationships, or model performance are in doubt.
---

# Semantic model rubric

Use this skill for model-first thinking.

## Preferred plugin routing

- `semantic-models@power-bi-agentic-development` for audits and DAX/model review
- `pbip@power-bi-agentic-development` for TMDL/PBIR project workflows
- `pbi-desktop@power-bi-agentic-development` for live Desktop model inspection

## Workflow

1. Use `checklists/model-review-checklist.md`.
2. Draft the design or review using `templates/semantic-model-template.md`.
3. Name where business logic should live:
   - source / SQL / dbt
   - semantic model
   - report-only layer
4. Flag star-schema violations, ambiguous relationships, many-to-many risk, and time-intelligence risk.
5. If the model cannot be reconciled back to source truth, fail the recommendation.

## Rules

- Prefer simple dimensional modeling over clever structures.
- Do not hide metric uncertainty inside DAX recommendations.
- Distinguish live-model tactics from PBIP/TMDL file tactics.
- Route report-page work away from this skill to `powerbi-build-playbook`.

## Supporting files

- `templates/semantic-model-template.md`
- `checklists/model-review-checklist.md`
- `references/plugin-routing.md`
