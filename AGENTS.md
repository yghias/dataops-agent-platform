# Agent Catalog

## Overview

The platform is built around domain specialists rather than a monolithic assistant. Each agent has:
- a defined purpose
- explicit input and output contracts
- constrained tool access
- a quality and governance role in the larger workflow
- a bias toward SQL-first outputs for warehouse-facing work

This structure makes the system easier to review, safer to operate, and more credible in enterprise settings.

## Shared contract

Every agent accepts a `TaskRequest` and returns an `AgentResult`.

### Standard input
- request ID
- request text
- requester role
- target environment
- task domain and intent
- any supplied attachments or prior context

### Standard output
- agent name
- artifact type
- rendered draft content
- rationale and assumptions
- referenced tool evidence
- quality notes and warnings
- recommended next step

## Specialist agents

### RouterAgent
Chooses the primary specialist and any collaborators based on domain, keywords, risk, and output type.

### DataEngineerAgent
Focus:
- ingestion and transformation workflows
- ETL/ELT design
- orchestration-aware implementation patterns
- Snowflake staging and curated model generation

Typical outputs:
- pipeline specifications
- incremental load logic
- implementation notes for Airflow and dbt-style SQL assets

### DataArchitectAgent
Focus:
- schema and domain design
- canonical models
- architectural tradeoff analysis

Typical outputs:
- conceptual and logical models
- schema review notes
- target-state architecture recommendations

### CloudPlatformAgent
Focus:
- CI/CD pipelines
- environment promotion
- infrastructure operating model
- deployment risk reduction

### DatabaseEngineerAgent
Focus:
- query structure and performance
- storage strategy
- physical design guidance

### DbaAgent
Focus:
- production-safety review
- access and operational controls
- DDL/change management constraints

### DataAnalystAgent
Focus:
- KPI logic
- semantic metric definitions
- BI-ready query patterns
- stable SQL publication for business-facing marts

### DataScientistAgent
Focus:
- feature engineering workflows
- experiment reproducibility
- offline/online data preparation alignment

### AiMlEngineerAgent
Focus:
- ML workflow operationalization
- training and scoring pipelines
- model promotion and monitoring controls

### ObservabilityAgent
Focus:
- data quality checks
- SLA and freshness monitoring
- alerting and triage design

### DocumentationAgent
Focus:
- design docs
- runbooks
- change summaries
- support documentation

## Routing guidance

Use the router to select one primary owner and optional supporting agents. Common combinations:
- pipeline build: `DataEngineerAgent` + `ObservabilityAgent` + `DocumentationAgent`
- schema review: `DataArchitectAgent` + `DatabaseEngineerAgent` + `DbaAgent`
- query optimization: `DatabaseEngineerAgent` + `DbaAgent`
- KPI request: `DataAnalystAgent` + `DocumentationAgent`
- ML pipeline request: `DataScientistAgent` + `AiMlEngineerAgent` + `ObservabilityAgent`

## Human review expectation

No agent has authority to finalize production changes. Every agent produces a draft plus reasoning. Final acceptance belongs to a human reviewer whose decision is persisted in memory and linked to the task history.
