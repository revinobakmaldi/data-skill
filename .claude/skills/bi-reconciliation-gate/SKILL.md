---
description: Run a KPI reconciliation gate before release or incident closure. Use when numbers changed, trust is in question, or a dashboard needs independent validation.
when_to_use: Prefer after model or report changes and before calling work done.
---

# BI reconciliation gate

Use this skill to produce an explicit pass/fail validation result.

## Workflow

1. Use `templates/reconciliation-template.md`.
2. Apply `references/variance-rules.md`.
3. State the source of truth and the exact comparison grain.
4. Separate critical KPI validation from secondary checks.
5. If source truth is unclear, stop and name the missing authority.

## Rules

- No unexplained variance on critical metrics.
- Validation method must be reproducible.
- Recommendations must end with `release`, `fix-before-release`, or `needs-business-decision`.

## Supporting files

- `templates/reconciliation-template.md`
- `references/variance-rules.md`
