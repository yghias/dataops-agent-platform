"""Controlled execution workflow for approved artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class ExecutionResult:
    request_id: str
    approved: bool
    executed: bool
    environment: str
    summary: str
    timestamp: str


class ExecutionWorkflow:
    """Executes only approved artifacts.

    This repository uses a simulated execution path to demonstrate
    governance boundaries without requiring live infrastructure.
    """

    def run(self, request_id: str, approved: bool, environment: str) -> ExecutionResult:
        if not approved:
            return ExecutionResult(
                request_id=request_id,
                approved=False,
                executed=False,
                environment=environment,
                summary="Execution blocked because no approved artifact was supplied.",
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        return ExecutionResult(
            request_id=request_id,
            approved=True,
            executed=True,
            environment=environment,
            summary="Simulated execution completed after approval and environment checks.",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
