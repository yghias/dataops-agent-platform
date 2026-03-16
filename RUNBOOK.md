# Runbook

## Purpose

This runbook covers basic operation of the local portfolio implementation and mirrors the structure expected in a real internal platform runbook.

## Starting the platform locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m workflows.intake_workflow
```

## Common operator tasks

### Review a generated artifact
- inspect the output from the intake workflow
- confirm quality warnings and assumptions
- record approval or rejection via the approval workflow

### Inspect decision logs
- open `memory/store/decision_log.jsonl`
- correlate with request IDs and artifact IDs

### Troubleshoot low-quality output
- check which tools were invoked
- inspect quality checker warnings
- review prompt version in the prompt registry
- compare against accepted examples

## Failure patterns

### Misrouted request
Symptoms:
- agent output does not match the expected domain

Actions:
- review route decision
- update routing keywords or confidence thresholds
- capture feedback for future tuning

### Artifact rejected for missing context
Symptoms:
- reviewer notes cite assumptions or ambiguity

Actions:
- enrich request intake fields
- add metadata retrieval before generation
- store rejection reason in feedback memory

### Unsafe execution attempt
Symptoms:
- execution denied due to approval or risk policy

Actions:
- confirm artifact approval status
- verify requester role and environment
- inspect governance policy notes
