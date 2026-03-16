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
- supports demo portability today and real integration later

### 0005: Use file-backed stores in the portfolio implementation
Reason:
- easy to inspect during review
- demonstrates auditability without introducing unnecessary infrastructure complexity
