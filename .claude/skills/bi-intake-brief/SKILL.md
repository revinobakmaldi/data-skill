---
description: Build a scoped BI intake brief from a vague request. Use when a user asks for a new dashboard, KPI change, semantic-model change, or BI enhancement and the request is still ambiguous.
when_to_use: Prefer before semantic-model design or report build work. Good for converting chat requests into a structured execution brief.
---

# BI intake brief

Use this skill to turn a vague BI request into a buildable brief.

## Workflow

1. Classify the request using `references/request-types.md`.
2. Draft the brief using `templates/intake-brief-template.md`.
3. Force explicit KPI, grain, audience, decision, refresh, and source assumptions.
4. If anything is missing, put it under `Open questions`, not hidden inside prose.
5. Route the next step:
   - semantic-model uncertainty -> `semantic-model-rubric`
   - report build specification -> `powerbi-build-playbook`
   - existing dashboard support -> `bi-ops-triage`

## Rules

- Do not invent metric definitions.
- Do not jump into visuals before grain and business logic are explicit.
- Separate `must know now` from `can refine later`.
- Keep the brief concise but decision-ready.

## Supporting files

- `templates/intake-brief-template.md`
- `references/request-types.md`
