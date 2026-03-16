# Architecture

## System intent

`dataops-agent-platform` is designed as an orchestration layer for domain-specific AI agents operating in controlled data environments. The architecture treats AI-generated work as a governed draft artifact, not an automatically trusted production action.

## Design principles

- Human approval is mandatory for impactful outputs.
- Agents are specialized by domain and constrained by role.
- Tools are explicit, typed, and audited.
- Governance is embedded into workflows rather than bolted on later.
- Memory stores decisions and outcomes, not just prompts and outputs.
- Execution is a separate, policy-controlled phase.

## Core runtime components

### 1. Intake and routing
The intake workflow converts a raw request into a structured `TaskRequest`, applies lightweight classification, and chooses a primary specialist plus any supporting agents. Routing decisions consider domain, output type, environment, risk, and whether execution is even permitted.

### 2. Specialist agents
Each specialist agent owns a narrow problem space:
- `DataEngineerAgent` for pipeline generation and transformation strategy
- `DataArchitectAgent` for schema and system design
- `CloudPlatformAgent` for infrastructure and CI/CD guidance
- `DatabaseEngineerAgent` for query and data model performance
- `DbaAgent` for operational safety, access, and change controls
- `DataAnalystAgent` for KPI and semantic logic
- `DataScientistAgent` for feature workflow and experiment support
- `AiMlEngineerAgent` for model operationalization and ML platform patterns
- `ObservabilityAgent` for monitoring and quality controls
- `DocumentationAgent` for runbooks and technical documentation

### 3. Tooling layer
The tools are intentionally isolated behind simple interfaces. That makes them easy to test, mock, audit, and replace with real integrations later.

Current tool families:
- SQL execution and explain-plan inspection
- schema and metadata lookup
- lineage retrieval
- DAG and dbt scaffold generation
- query optimization heuristics
- document generation
- quality validation

### 4. Reviewer and approval flow
All generated artifacts flow through machine review before humans see them. The approval workflow packages:
- artifact summary
- risk and quality signals
- supporting tool evidence
- policy considerations
- recommended next action

The human reviewer is the control point that determines whether the artifact is approved, rejected, or revised.

### 5. Memory and audit services
The repository models three durable platform memory types:
- decision memory: who approved what, when, and why
- feedback memory: why an output was accepted or rejected
- prompt memory: which prompt or generation strategy version was used

These are the backbone of continuous improvement and auditability.

## End-to-end flow

1. User submits a request.
2. Intake workflow normalizes the request into a typed task.
3. Router selects the appropriate specialist agents.
4. Selected agents call scoped tools and generate draft artifacts.
5. Quality checks and reviewer logic evaluate the draft.
6. Approval workflow packages results for human review.
7. Human decision is logged.
8. Approved artifacts can move into controlled execution.
9. Execution outcome and feedback are recorded for future reuse.

## Runtime boundaries

### Generation boundary
The generation boundary separates inference from action. Within this boundary, agents can:
- inspect schemas and metadata
- run read-only diagnostics
- generate code or documents
- propose recommendations

They cannot:
- automatically promote code
- execute production changes without approval
- bypass policy checks

### Execution boundary
The execution workflow requires:
- an approved artifact
- a policy-compliant environment
- the right reviewer role
- explicit logging of the action

This boundary is the main safety mechanism for enterprise usage.

## Tradeoffs

### Why multiple agents
Multiple agents increase orchestration complexity, but they improve explainability, maintainability, and domain alignment. A single general agent tends to produce weaker outputs in cross-functional data environments.

### Why mock tools in this repo
The repo is designed for reviewability and portability. Mock and demo tool implementations make the workflow understandable without live infrastructure, while preserving realistic interfaces for future integration work.

### Why file-backed memory
File-backed JSONL storage is enough to demonstrate auditability and feedback loops. In a production implementation, these stores would be moved to transactional and analytical backends with stronger access controls and retention policies.

## Future production hardening

- replace mock tools with warehouse, catalog, and lineage service integrations
- add an API layer and RBAC-backed identity provider integration
- persist workflow state in a database
- integrate OpenTelemetry traces and centralized logs
- add policy-as-code enforcement and change approval escalations
