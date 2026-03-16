# Workflows

## Operating model

The repository implements four core workflows:
- intake
- approval
- execution
- feedback

These workflows form the human-in-the-loop control system for the platform.

## Intake workflow

Purpose:
- normalize requests
- assess domain and risk
- route to the best specialist agents
- gather initial context

Inputs:
- freeform request text
- requester role
- target environment
- optional attachments

Outputs:
- structured task record
- selected agents
- initial draft artifacts

## Approval workflow

Purpose:
- package outputs for review
- enforce reviewer and policy gates
- record human approval or rejection

Key controls:
- explicit reviewer identity
- decision reason capture
- policy denial support
- artifact version tracking

## Execution workflow

Purpose:
- ensure only approved outputs become executable actions
- capture execution metadata and outcomes

Controls:
- approved artifact required
- environment and risk checks
- explicit execution event logging
- simulated mode supported in this repo

## Feedback workflow

Purpose:
- capture structured reviewer feedback
- store acceptance and rejection reasons
- support prompt, routing, and quality improvements

## Workflow state model

Recommended states:
- `submitted`
- `classified`
- `drafted`
- `awaiting_approval`
- `approved`
- `rejected`
- `executed`
- `failed`
- `closed`

## Review philosophy

The workflows are designed for enterprise data teams where the value of AI is acceleration with accountability. That means the system should bias toward transparent drafts, strong review packages, and durable decision records rather than silent automation.
