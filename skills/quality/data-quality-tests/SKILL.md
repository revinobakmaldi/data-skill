---
name: data-quality-tests
description: Generate useful quality checks for analytics datasets.
---

# Data Quality Tests

## Purpose
Generate useful quality checks for analytics datasets.

## Expected inputs
- table or model name
- critical fields
- thresholds if known

## Expected outputs
- test list
- SQL assertions
- failure interpretation

## Guidance
- Prioritize checks that would break decision quality.
- Include null, duplicate, referential, and threshold checks when relevant.
- State why each test matters.
- Keep the set focused, not bloated.

## Starter prompt
Use this skill to handle **data quality tests**. Keep the output practical, concise, and ready for the analytics team to review.
