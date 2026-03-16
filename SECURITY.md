# Security

## Security posture

This repository models a secure-by-default approach for AI-assisted data operations.

## Key controls

- do not store credentials in prompts, source, or logs
- treat schema metadata as potentially sensitive
- separate read-only inspection from write execution
- mask secrets and restricted fields in all persisted output
- require human approval before any material execution step

## Threat considerations

### Prompt leakage
Sensitive connection details or schema content should never be embedded directly in reusable prompts.

### Over-permissioned tools
Tooling should be scoped by role and environment. A read-only analyst workflow should not receive production write capability.

### Audit gaps
Missing audit records weaken governance and incident response. Logging should capture requests, tool calls, decisions, and execution attempts.

### Unsafe automation
Generated code must not bypass peer review or change-control processes.

## Hardening roadmap

- integrate secret manager references
- add policy-as-code enforcement
- support stronger identity and session binding
- add artifact signing and retention rules
