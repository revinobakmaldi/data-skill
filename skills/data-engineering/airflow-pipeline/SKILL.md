---
name: airflow-pipeline
description: Scaffold or review Airflow-based ingestion pipelines.
---

# Airflow Pipeline

## Purpose
Scaffold or review Airflow-based ingestion pipelines.

## Expected inputs
- source type
- load frequency
- destination
- incremental logic

## Expected outputs
- DAG outline
- task list
- failure handling notes

## Guidance
- Design the DAG at the right granularity.
- Include retries, logging, and alert hooks.
- Prefer idempotent tasks.
- Document assumptions about source freshness and backfill behavior.

## Starter prompt
Use this skill to handle **airflow pipeline**. Keep the output practical, concise, and ready for the analytics team to review.
