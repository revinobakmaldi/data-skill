# data-skill

Repo for real AI resources the data team can use across:
- data engineering
- analytics engineering / modeling
- BI / Power BI
- analysis
- data science
- reporting and delivery

This repo is not a fake local skill pack.
It is a curated directory of **real external skills, MCPs, tools, frameworks, and workflow references** mapped to the team workflow.

## Start here

- `TEAM_WORKFLOW_MAP.html` , visual workflow and AI leverage map
- `REAL_RESOURCES.md` , main stage-by-stage resource list
- `catalog/real-workflow-resources.yaml` , machine-readable workflow mapping
- `SKILLS_INDEX.md` , fast index of the most relevant external resources

## What this repo currently contains

### 1. Workflow map
A visual map of the analytics product workflow, including where AI can help through:
- MCPs
- tools
- automation
- human review

### 2. Real external resources
Curated internet resources aligned to the workflow, including:
- MCP servers
- orchestration tools
- transformation tools
- data quality frameworks
- reporting tools
- LLM evaluation / observability tools
- ML experimentation tools

### 3. Lightweight reference docs
Small internal docs for:
- MCP references
- tool references
- automation references

## Current high-priority resources

### Core MCPs
- `googleapis/mcp-toolbox`  
  https://github.com/googleapis/mcp-toolbox
- `microsoft/powerbi-modeling-mcp`  
  https://github.com/microsoft/powerbi-modeling-mcp
- `dbt-labs/dbt-mcp`  
  https://github.com/dbt-labs/dbt-mcp

### Pipeline and ingestion
- `apache/airflow`  
  https://github.com/apache/airflow
- `astronomer/astro-sdk`  
  https://github.com/astronomer/astro-sdk
- `airbytehq/airbyte`  
  https://github.com/airbytehq/airbyte
- `dlt-hub/dlt`  
  https://github.com/dlt-hub/dlt

### Modeling and transformation
- `dbt-labs/dbt-core`  
  https://github.com/dbt-labs/dbt-core
- `dbt-labs/dbt-utils`  
  https://github.com/dbt-labs/dbt-utils
- `dbt-labs/dbt-project-evaluator`  
  https://github.com/dbt-labs/dbt-project-evaluator

### Data quality and observability
- `great-expectations/great_expectations`  
  https://github.com/great-expectations/great_expectations
- `calogica/dbt-expectations`  
  https://github.com/calogica/dbt-expectations
- `elementary-data/elementary`  
  https://github.com/elementary-data/elementary

### Analytics product build
- `data-goblin/power-bi-agentic-development`  
  https://github.com/data-goblin/power-bi-agentic-development
- `RuiRomano/powerbi-agentic-mcp-cloud-agent`  
  https://github.com/RuiRomano/powerbi-agentic-mcp-cloud-agent
- `quarto-dev/quarto-cli`  
  https://github.com/quarto-dev/quarto-cli
- `evidence-dev/evidence`  
  https://github.com/evidence-dev/evidence
- `microsoft/playwright`  
  https://github.com/microsoft/playwright

### Insight generation / LLM ops
- `promptfoo/promptfoo`  
  https://github.com/promptfoo/promptfoo
- `langfuse/langfuse`  
  https://github.com/langfuse/langfuse
- `evidentlyai/evidently`  
  https://github.com/evidentlyai/evidently

### Data science
- `mlflow/mlflow`  
  https://github.com/mlflow/mlflow
- `scikit-learn/scikit-learn`  
  https://github.com/scikit-learn/scikit-learn
- `alteryx/featuretools`  
  https://github.com/alteryx/featuretools

## Recommended use of this repo

Use this repo to answer 3 questions:

1. **What is the workflow stage?**  
   Check `TEAM_WORKFLOW_MAP.html`

2. **What real tools/MCPs fit that stage?**  
   Check `REAL_RESOURCES.md`

3. **Which resources should we evaluate, clone, or adopt?**  
   Use `SKILLS_INDEX.md` and the YAML catalog as the shortlist.

## Current gaps

This repo still needs a better decision layer for:
- clone now vs reference only
- team priority ranking
- owner by function
- implementation status

## Next improvement

The next useful upgrade is to add a matrix like:
- resource
- workflow stage
- team function
- use case
- maturity
- adopt now / later / reference only
