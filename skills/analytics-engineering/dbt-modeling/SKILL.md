---
name: dbt-modeling
description: Draft or improve dbt models for trusted business-ready datasets.
---

# dbt Modeling

## Purpose
Draft or improve dbt models for trusted business-ready datasets.

## Expected inputs
- source tables
- business rules
- grain definition

## Expected outputs
- model plan
- dbt SQL pattern
- test suggestions

## Guidance
- Prefer clear staging -> intermediate -> mart flow.
- Keep naming consistent and business-readable.
- State grain explicitly.
- Recommend tests for important fields and relationships.

## Starter prompt
Use this skill to handle **dbt modeling**. Keep the output practical, concise, and ready for the analytics team to review.
