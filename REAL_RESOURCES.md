# Real External Resources

Source of truth for real internet resources that map to the analytics workflow.

## 1. Project assessment

### HTML prototyping and UI generation
- **quarto-dev/quarto-cli**  
  https://github.com/quarto-dev/quarto-cli  
  Good for fast document-style prototyping that can become HTML and PDF outputs.

- **evidence-dev/evidence**  
  https://github.com/evidence-dev/evidence  
  Strong fit for analytics products that mix SQL, charts, narrative, and web delivery.

### Data discovery / retrieval
- **googleapis/mcp-toolbox**  
  https://github.com/googleapis/mcp-toolbox  
  Real MCP toolbox for structured database access across multiple data systems.

## 2. Pipeline and ingestion

### Orchestration
- **apache/airflow**  
  https://github.com/apache/airflow  
  Core orchestration platform for ingestion and scheduling.

- **astronomer/astro-sdk**  
  https://github.com/astronomer/astro-sdk  
  Helpful Airflow SDK for data pipeline development patterns.

### Data loading / movement
- **airbytehq/airbyte**  
  https://github.com/airbytehq/airbyte  
  Real connector ecosystem for extraction and ingestion.

- **dlt-hub/dlt**  
  https://github.com/dlt-hub/dlt  
  Good for programmable loading pipelines with Python.

## 3. Modeling and transformation

### Analytics engineering
- **dbt-labs/dbt-core**  
  https://github.com/dbt-labs/dbt-core  
  Core transformation framework.

- **dbt-labs/dbt-utils**  
  https://github.com/dbt-labs/dbt-utils  
  Widely used reusable macros and testing helpers.

- **dbt-labs/dbt-project-evaluator**  
  https://github.com/dbt-labs/dbt-project-evaluator  
  Good for evaluating dbt project quality and conventions.

- **dbt-labs/dbt-mcp**  
  https://github.com/dbt-labs/dbt-mcp  
  Real MCP server from dbt Labs for dbt-aware AI workflows.

## 4. Data quality and testing

- **great-expectations/great_expectations**  
  https://github.com/great-expectations/great_expectations  
  Real data quality framework.

- **calogica/dbt-expectations**  
  https://github.com/calogica/dbt-expectations  
  dbt-native testing patterns inspired by Great Expectations.

- **elementary-data/elementary**  
  https://github.com/elementary-data/elementary  
  dbt observability and data quality monitoring.

## 5. Analytics product build

### Power BI exploratory products
- **microsoft/powerbi-modeling-mcp**  
  https://github.com/microsoft/powerbi-modeling-mcp  
  Real Power BI semantic-model MCP.

- **data-goblin/power-bi-agentic-development**  
  https://github.com/data-goblin/power-bi-agentic-development  
  Real collection of Power BI agent resources and workflows.

- **RuiRomano/powerbi-agentic-mcp-cloud-agent**  
  https://github.com/RuiRomano/powerbi-agentic-mcp-cloud-agent  
  Real workflow template for agentic Power BI development.

### HTML narrative products and PDF outputs
- **quarto-dev/quarto-cli**  
  https://github.com/quarto-dev/quarto-cli  
  Best fit for HTML to PDF analytics reporting.

- **evidence-dev/evidence**  
  https://github.com/evidence-dev/evidence  
  Best fit for self-explanatory analytical web reports.

- **microsoft/playwright**  
  https://github.com/microsoft/playwright  
  Useful for browser-based HTML-to-PDF rendering and testing.

## 6. Exploration and insight generation

### Prompting, evaluation, and insight workflows
- **promptfoo/promptfoo**  
  https://github.com/promptfoo/promptfoo  
  Real prompt testing and eval framework.

- **langfuse/langfuse**  
  https://github.com/langfuse/langfuse  
  Real tracing, prompt management, and LLM observability platform.

- **evidentlyai/evidently**  
  https://github.com/evidentlyai/evidently  
  Useful for evaluation and quality tracking of data/ML/LLM outputs.

### Retrieval / data access
- **googleapis/mcp-toolbox**  
  https://github.com/googleapis/mcp-toolbox  
  Strong candidate when the insight script needs structured retrieval.

## 7. Predictive modeling and experimentation

- **mlflow/mlflow**  
  https://github.com/mlflow/mlflow  
  Real experiment tracking and model lifecycle tooling.

- **scikit-learn/scikit-learn**  
  https://github.com/scikit-learn/scikit-learn  
  Core ML toolkit for many practical predictive workflows.

- **featuretools/featuretools**  
  https://github.com/alteryx/featuretools  
  Good for feature engineering acceleration.

## 8. Deployment and stakeholder delivery

- **quarto-dev/quarto-cli**  
  https://github.com/quarto-dev/quarto-cli  
  Strong delivery path for publishable HTML and PDF outputs.

- **microsoft/playwright**  
  https://github.com/microsoft/playwright  
  Good for rendering validation and export automation.

- **apache/airflow**  
  https://github.com/apache/airflow  
  Can orchestrate recurring delivery jobs.

## 9. Monitoring and iteration

- **elementary-data/elementary**  
  https://github.com/elementary-data/elementary  
  Data quality and observability for dbt-heavy stacks.

- **langfuse/langfuse**  
  https://github.com/langfuse/langfuse  
  Monitoring for LLM prompts and outputs.

- **evidentlyai/evidently**  
  https://github.com/evidentlyai/evidently  
  Useful for monitoring model and output drift.

## Status

Resources now configured in this repo (see `mcp/configs/` and `skills/`):

- ✅ `googleapis/mcp-toolbox` — config at `mcp/configs/bigquery-toolbox.json`
- ✅ `dbt-labs/dbt-mcp` — config at `mcp/configs/dbt-mcp.json`; skills from `dbt-labs/dbt-agent-skills`
- ✅ `microsoft/powerbi-modeling-mcp` — config at `mcp/configs/powerbi-mcp.json` (semantic model MCP only — NOT report/visual editing)
- ✅ `data-goblin/power-bi-agentic-development` — cloned at `plugins/power-bi-agentic-development/` (report/visual editing via PBIP + full PBI plugin suite)
- ✅ `microsoft/azure-devops-mcp` — config at `mcp/configs/azure-devops-mcp.json`
- ✅ `microsoft/playwright` — wrapped in `scripts/html_to_pdf.py`

Still external references (not yet configured locally):

- ⬜ `RuiRomano/powerbi-agentic-mcp-cloud-agent` — superseded by data-goblin plugin suite, skip
- ⬜ `apache/airflow` — orchestration platform, install separately
- ⬜ `dbt-labs/dbt-core` — transformation framework, install separately
- ⬜ `great-expectations/great_expectations` — quality framework, install separately
- ⬜ `elementary-data/elementary` — dbt observability, install as dbt package
- ⬜ `airbytehq/airbyte` — ingestion platform, deploy separately
- ⬜ `promptfoo/promptfoo` — prompt eval, install separately
- ⬜ `langfuse/langfuse` — LLM observability, deploy separately
