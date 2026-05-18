# Analytics Team Workflows

Practical workflow map for a modern analytics team using AI support across data engineering, analytics engineering, BI, analysis, and data science.

## 1. Core team workflow map

```text
Business question
  -> Request intake
  -> Scope and prioritization
  -> Data discovery
  -> Data pipeline / ingestion
  -> Data modeling / transformation
  -> Data quality validation
  -> Analysis / insight generation
  -> Dashboard / semantic model / reporting
  -> Review with stakeholders
  -> Deploy / publish
  -> Monitor / iterate
```

## 2. Workflow by function

## A. Request intake and scoping
**Goal:** turn messy business asks into executable work.

### Typical tasks
- clarify objective
- define KPI or success metric
- identify owner and stakeholder
- estimate effort
- classify request type
- prioritize backlog

### Inputs
- stakeholder request
- business context
- timeline
- expected output

### Outputs
- clear problem statement
- scoped task ticket
- success criteria
- owner assignment

### AI support ideas
- rewrite vague request into structured brief
- generate assumptions and clarifying questions
- draft acceptance criteria
- suggest task breakdown

---

## B. Data discovery and source mapping
**Goal:** identify what data exists and where it lives.

### Typical tasks
- find source tables/files/APIs
- inspect schema
- map joins and business keys
- identify grain
- document freshness and ownership

### Inputs
- scoped business question
- database access
- source system knowledge

### Outputs
- source inventory
- join logic
- field mapping
- risks and gaps

### AI support ideas
- schema exploration
- metadata summarization
- join path suggestions
- column description generation

---

## C. Data pipeline / ingestion workflow
**Goal:** move raw data reliably from source to usable storage.

### Typical tasks
- build extraction job
- connect API/database/file source
- define schedule
- handle incremental loads
- log failures and retries
- monitor freshness

### Inputs
- source credentials
- source schema
- frequency requirement
- destination target

### Outputs
- working ingestion pipeline
- load logs
- retry/error handling
- freshness monitoring

### AI support ideas
- generate ETL/ELT boilerplate
- create SQL or Python ingestion scripts
- write validation checks
- draft observability rules

### Typical owners
- data engineer
- analytics engineer

---

## D. Data modeling / transformation workflow
**Goal:** transform raw data into trusted business-ready models.

### Typical tasks
- clean and standardize fields
- define business logic
- create fact and dimension models
- build marts
- enforce naming conventions
- manage dependencies

### Inputs
- raw/staging data
- business rules
- grain definition
- KPI logic

### Outputs
- transformed tables
- semantic layer
- reusable business definitions
- documented logic

### AI support ideas
- generate dbt or SQL models
- review naming conventions
- explain model lineage
- propose star schema improvements
- convert business logic into transformation logic

### Typical owners
- analytics engineer
- BI developer
- data modeler

---

## E. Data quality and testing workflow
**Goal:** ensure trusted outputs before stakeholder use.

### Typical tasks
- null checks
- duplicate checks
- referential integrity checks
- reconciliation vs source
- anomaly detection
- test business rule validity

### Inputs
- transformed models
- expected thresholds
- source comparisons

### Outputs
- test results
- issue log
- pass/fail decision
- remediation actions

### AI support ideas
- generate test cases
- write SQL assertions
- summarize failed checks
- propose root causes

### Typical owners
- data engineer
- analytics engineer
- BI developer

---

## F. BI / semantic model / dashboard workflow
**Goal:** expose trusted metrics for consumption.

### Typical tasks
- build semantic model
- create measures
- create dimensions/hierarchies
- define RLS
- build dashboard/report
- optimize usability and performance

### Inputs
- clean modeled data
- KPI definitions
- stakeholder reporting needs

### Outputs
- semantic model
- dashboard/report
- measure catalog
- access model

### AI support ideas
- DAX generation
- DAX debugging
- semantic model documentation
- naming audit
- report QA checklist
- performance tuning suggestions

### Typical owners
- BI developer
- analytics engineer
- analyst

---

## G. Analysis and insight generation workflow
**Goal:** answer business questions with clear reasoning and recommendations.

### Typical tasks
- perform exploratory analysis
- compare segments and trends
- identify drivers
- validate hypotheses
- quantify impact
- write recommendation

### Inputs
- trusted datasets
- business question
- baseline and benchmark

### Outputs
- analysis narrative
- charts/tables
- insight summary
- recommendation and next action

### AI support ideas
- generate analysis plan
- summarize findings
- write executive narrative
- suggest follow-up cuts or hypotheses

### Typical owners
- data analyst
- BI analyst
- analytics manager

---

## H. Data science / advanced modeling workflow
**Goal:** build predictive or optimization models when descriptive analytics is not enough.

### Typical tasks
- define prediction target
- create feature set
- train and validate model
- compare algorithms
- explain drivers
- package scoring logic

### Inputs
- labeled data
- business objective
- constraints
- evaluation metric

### Outputs
- trained model
- validation report
- scoring pipeline
- deployment recommendation

### AI support ideas
- feature ideation
- notebook scaffolding
- experiment logging templates
- model explanation draft
- code review support

### Typical owners
- data scientist
- machine learning engineer

---

## I. Deployment and stakeholder delivery workflow
**Goal:** publish outputs safely and make them usable.

### Typical tasks
- publish dashboard/model
- deploy pipeline or transformation job
- handoff documentation
- stakeholder walkthrough
- collect feedback
- train users

### Inputs
- approved output
- deployment environment
- access settings

### Outputs
- production release
- release notes
- user guidance
- feedback log

### AI support ideas
- release note generation
- documentation draft
- meeting summary
- FAQ generation

---

## J. Monitoring and iteration workflow
**Goal:** keep analytics products healthy after release.

### Typical tasks
- monitor pipeline failures
- monitor data freshness
- review report usage
- review model drift
- fix broken logic
- prioritize enhancements

### Inputs
- logs
- incidents
- usage metrics
- stakeholder feedback

### Outputs
- incident resolution
- enhancement backlog
- revised logic
- updated documentation

### AI support ideas
- incident summary
- root cause draft
- anomaly summaries
- enhancement clustering

---

## 3. Recommended operating lanes

### Lane 1. Data engineering
Focus:
- ingestion
- orchestration
- storage
- monitoring
- reliability

### Lane 2. Analytics engineering / modeling
Focus:
- transformation
- semantic logic
- reusable models
- testing
- documentation

### Lane 3. BI and reporting
Focus:
- semantic models
- DAX
- dashboards
- stakeholder-facing reporting

### Lane 4. Analysis
Focus:
- decision support
- insight generation
- narrative
- business recommendations

### Lane 5. Data science
Focus:
- prediction
- experimentation
- optimization
- automation of decision logic

## 4. Standard request routing

| Request type | Primary owner | Secondary owner | Typical output |
|---|---|---|---|
| Broken pipeline | Data Engineer | Analytics Engineer | Fixed job |
| New KPI definition | Analytics Engineer | BI Developer | Metric logic |
| New dashboard | BI Developer | Analyst | Report |
| Deep-dive business question | Analyst | Analytics Manager | Insight deck / summary |
| Predictive use case | Data Scientist | Data Engineer | Model / scoring workflow |
| Data quality issue | Analytics Engineer | Data Engineer | Fixed model and tests |
| Slow Power BI report | BI Developer | Analytics Engineer | Tuned semantic model/report |

## 5. Where AI should help most

Highest ROI areas:
- SQL generation
- DAX generation and debugging
- schema summarization
- documentation writing
- test creation
- issue triage
- analysis summarization
- stakeholder-ready narrative writing
- refactoring repetitive model logic

## 6. Suggested repo structure for skills

```text
skills/
  data-engineering/
    pipeline-design/
    ingestion-debugging/
    sql-validation/
    data-quality-checks/
  analytics-engineering/
    model-design/
    dbt-sql-generation/
    naming-standardization/
    lineage-documentation/
  bi/
    dax-generation/
    dax-debugging/
    semantic-model-documentation/
    report-qa/
  analysis/
    exploratory-analysis/
    insight-writing/
    hypothesis-generation/
  data-science/
    feature-ideation/
    experiment-design/
    model-review/
```

## 7. Simple execution model

For each team task, use this pattern:

1. Define the business goal
2. Gather source and context
3. Let AI draft the first pass
4. Human reviews logic and risk
5. Publish or deploy
6. Monitor results
7. Improve the skill/playbook

That keeps AI useful without letting it run blind.
