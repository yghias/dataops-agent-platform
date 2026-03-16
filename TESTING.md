# Testing

## Test strategy

The platform should be validated at three levels:
- unit tests for agent, tool, and memory behavior
- workflow tests for routing, approval, and execution state transitions
- artifact validation tests for SQL, DAG, dbt, and documentation outputs

## Current repository focus

This repository emphasizes reviewable code structure and representative logic rather than exhaustive runtime integration. The testable seams are deliberately clear:
- tool classes are deterministic
- workflows accept typed inputs and return typed outputs
- memory stores are file-backed and easy to inspect

## Recommended initial test suite

- router classification by request type
- agent result content and warning behavior
- quality checker scoring for key artifact types
- approval workflow state transition rules
- decision log persistence and reload behavior
- query optimizer recommendation coverage for common anti-patterns

## Production extension

For a fuller implementation, add:
- contract tests for metadata and lineage integrations
- fixture-driven SQL optimization tests
- notebook-driven evaluation reports
- policy engine regression tests
