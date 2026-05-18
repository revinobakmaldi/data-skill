---
name: reconciliation-checks
description: Design reconciliation logic between source and downstream outputs.
---

# Reconciliation Checks

## Purpose
Design reconciliation logic between source and downstream outputs.

## Expected inputs
- source metrics
- target metrics
- time grain

## Expected outputs
- reconciliation plan
- variance thresholds
- investigation path

## Guidance
- Compare at the right grain.
- Separate expected differences from real issues.
- Make mismatch investigation easy to follow.
- Recommend escalation rules.

## Starter prompt
Use this skill to handle **reconciliation checks**. Keep the output practical, concise, and ready for the analytics team to review.
