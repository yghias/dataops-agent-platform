# CI/CD

## Objectives

The CI/CD model for this repository is designed to reinforce code quality and governance readiness.

## Continuous integration

The `ci.yml` workflow is intended to:
- set up Python
- install dependencies
- run static checks
- execute unit tests
- validate repository structure
- validate SQL and dbt-style assets are present

Recommended checks:
- `python -m compileall`
- `pytest`
- `ruff check`
- optional notebook and markdown validation
- SQL linting or warehouse parser checks where available

## Continuous delivery

The `deploy.yml` workflow is intentionally conservative. In a real implementation it would:
- build a container image
- run integration smoke checks
- publish tagged images or release artifacts
- require environment protection rules for staging and production

## Promotion philosophy

This repository models the same principle used inside the platform:
- generation is easy
- promotion is controlled

That means deployment steps should be tied to approvals, protected branches, and environment policies rather than automatic push-to-prod behavior.

## Deployment expectations

- `dev`: build and validation only
- `staging`: integration checks against Snowflake non-production datasets
- `prod`: protected environment with explicit approval and rollback evidence
