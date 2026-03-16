# Approval Policy

## Purpose

This policy defines the minimum approval expectations for AI-generated artifacts created by `dataops-agent-platform`.

## Decision classes

### Advisory
Examples:
- architecture notes
- KPI drafts
- documentation suggestions

Requirement:
- one reviewer before adoption into shared documentation or backlog

### Technical draft
Examples:
- SQL rewrite proposals
- DAG scaffolds
- dbt models
- schema recommendations

Requirement:
- one qualified domain reviewer
- logged rationale if rejected

### Production-impacting
Examples:
- executable SQL changes
- DDL recommendations intended for promotion
- deployment or runtime changes

Requirement:
- explicit approver with appropriate role
- execution logged separately from approval
- no automated production action without approval

## Denial conditions

Block approval when:
- the request lacks required context
- policy restrictions are violated
- the artifact includes unsafe assumptions
- evidence is insufficient for the requested action

## Reviewer expectations

Reviewers should evaluate:
- technical correctness
- operational safety
- standards compliance
- clarity of assumptions
- appropriateness for the target environment
