---
description: Build a Power BI report specification with clear page structure, visual intent, PBIP/PBIR workflow choice, and release readiness. Use for new dashboard build work or substantial report redesign.
when_to_use: Prefer after intake and semantic-model clarity already exist.
---

# Power BI build playbook

Use this skill to make report-build work concrete and reviewable.

## Preferred plugin routing

- `reports@power-bi-agentic-development` for report-page, visual, theme, and `pbir` CLI workflows
- `pbip@power-bi-agentic-development` for PBIP/PBIR structure and validation
- `pbi-desktop@power-bi-agentic-development` for live Desktop checks when needed

## Workflow

1. Use `templates/report-spec-template.md`.
2. Check `checklists/release-checklist.md`.
3. Decide the execution surface:
   - PBIP/TMDL/PBIR project edits
   - live Desktop model / report session
4. Design pages around decisions, not around chart variety.
5. Keep a short rationale for every page and major visual.

## Rules

- Do not redefine business logic in the report layer if it belongs in the model.
- Avoid decorative visuals that do not improve decision speed.
- Name the plugin workflow or CLI path you expect to use.
- Add explicit QA handoff items.

## Supporting files

- `templates/report-spec-template.md`
- `checklists/release-checklist.md`
- `references/plugin-routing.md`
