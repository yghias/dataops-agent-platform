# dataops-agent-platform

`dataops-agent-platform` is a human-in-the-loop multi-agent AI platform for data engineering, architecture, database, cloud, analytics, and AI/ML workflows. It helps teams generate draft artifacts such as ETL designs, Airflow DAGs, dbt models, SQL optimizations, schema reviews, runbooks, and governance evidence, while ensuring that humans stay in control of approval and execution.

The repository is designed as a production-style portfolio project rather than a toy chatbot. It emphasizes:
- specialist agents instead of a single general assistant
- policy-aware routing and tool access
- explicit human review before execution
- auditability, feedback capture, and reusable memory
- strong documentation and operational structure

## What the platform does

The platform accepts a request, classifies it, routes it to the right specialist agents, invokes constrained tools, generates draft outputs, runs a reviewer pass, and packages results for human approval. Approved outputs can then move into a controlled execution workflow, while rejected outputs are logged for continuous improvement.

Supported request families include:
- ETL/ELT pipeline generation
- Airflow DAG creation
- dbt model and test generation
- SQL generation and optimization
- schema and data model review
- architecture review and platform guidance
- CI/CD and cloud platform recommendations
- data quality and observability design
- documentation and runbook generation
- feature pipeline and ML workflow support

## Why this repo matters

Most AI examples stop at prompt engineering. This repository focuses on the harder enterprise problem: how to apply AI safely to production data work. It demonstrates:
- orchestration across multiple domain specialists
- governance and approval controls
- recoverable workflows with traceability
- reusable tool contracts
- artifact memory and decision logging
- documentation that reflects real platform concerns

## Architecture summary

At a high level, the repository contains:
- `agents/`: specialist agents with clear input and output contracts
- `tools/`: tool adapters for SQL, metadata, lineage, query analysis, documentation, and quality checks
- `workflows/`: intake, approval, execution, and feedback flows
- `memory/`: prompt registry, decision logging, and feedback storage
- `governance/`: approval and audit operating model
- `examples/`: realistic request examples
- `sql/`: sample warehouse assets used by the tools and examples

See [`PLAN.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/PLAN.md) for the implementation blueprint and [`ARCHITECTURE.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/ARCHITECTURE.md) for the runtime model.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m workflows.intake_workflow
```

This repository ships with mock implementations and sample assets so the orchestration model can be reviewed without requiring live warehouse credentials.

## Review path

If you want the fastest tour of the repository, review these first:
1. [`ARCHITECTURE.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/ARCHITECTURE.md)
2. [`AGENTS.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/AGENTS.md)
3. [`workflows/intake_workflow.py`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/workflows/intake_workflow.py)
4. [`tools/query_optimizer.py`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/tools/query_optimizer.py)
5. [`memory/decision_log.py`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/memory/decision_log.py)

## Human-in-the-loop design

The platform deliberately separates generation from execution.

- Agents can draft recommendations and code.
- Reviewer logic scores and critiques the draft.
- Humans approve, reject, or request changes.
- Decisions are logged with rationale.
- Only approved outputs can enter the execution workflow.

This pattern makes the platform realistic for regulated, production-sensitive data environments.
