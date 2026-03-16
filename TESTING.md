# Testing

## Test strategy

The platform should be validated at three levels:
- unit tests for agent, tool, and memory behavior
- workflow tests for routing, approval, and execution state transitions
- artifact validation tests for SQL, DAG, dbt, and documentation outputs

## Current repository focus

The current repository emphasizes reviewable control-flow code plus SQL assets that can be validated independently. The testable seams are deliberately clear:
- tool classes are deterministic
- workflows accept typed inputs and return typed outputs
- memory stores are file-backed and easy to inspect
- Snowflake SQL assets are organized so they can be executed or linted independently from Python workflows

## Recommended initial test suite

- router classification by request type
- agent result content and warning behavior
- quality checker scoring for key artifact types
- approval workflow state transition rules
- decision log persistence and reload behavior
- query optimizer recommendation coverage for common anti-patterns

## SQL validation scope

Warehouse validation should include:
- staging uniqueness and not-null checks
- mart-level non-negative and lifecycle consistency checks
- reconciliation between source and published marts
- metric-level assertions for KPI tables
- contract validation for upstream schema versions
- backfill rerun validation for affected partitions

## Production extension

For a fuller implementation, add:
- contract tests for metadata and lineage integrations
- fixture-driven SQL optimization tests
- notebook-driven evaluation reports
- policy engine regression tests
