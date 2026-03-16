# Audit Model

## Objective

The audit model provides traceability across request intake, routing, tool usage, human review, and execution.

## Required audit events

- request submitted
- request classified
- route selected
- tool invoked
- artifact generated
- artifact reviewed
- human decision recorded
- execution requested
- execution completed or denied
- feedback recorded

## Mandatory fields

- request ID
- timestamp
- actor or system component
- event type
- environment
- affected artifact or asset
- summary payload

## Retention guidance

In a production implementation:
- store event history in an immutable or append-only system
- separate sensitive payloads from general audit metadata
- apply retention rules aligned to compliance and incident-response needs
