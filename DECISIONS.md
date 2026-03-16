# Decisions

## Architectural decisions

### 0001: Use specialist agents instead of a single general agent
Reason:
- improves domain alignment and explainability
- makes tool scoping and review easier

### 0002: Separate generation from execution
Reason:
- preserves human control
- makes policy enforcement tractable
- aligns with enterprise change management

### 0003: Model memory as decision-centric rather than chat-centric
Reason:
- approvals, rejections, and rationale are the most valuable long-term learning signal

### 0004: Keep tool interfaces simple and replaceable
Reason:
- keeps runtime responsibilities clear and makes Snowflake, catalog, and lineage integrations easier to swap

### 0005: Use file-backed stores in the initial repository version
Reason:
- easy to inspect and operate locally
- keeps approval and feedback records durable without introducing a full state service on day one

### 0006: Prefer SQL over Python for transformation logic
Reason:
- warehouse transformations, marts, KPI logic, and quality checks are easier to review and validate in SQL
- orchestration and control flow should stay in Python, but data logic should live in Snowflake assets whenever practical
