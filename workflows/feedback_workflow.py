"""Feedback capture workflow."""

from __future__ import annotations

from memory.feedback_store import FeedbackEvent, FeedbackStore


class FeedbackWorkflow:
    """Captures post-review and post-execution signals."""

    def __init__(self) -> None:
        self.store = FeedbackStore()

    def record(
        self,
        request_id: str,
        artifact_type: str,
        outcome: str,
        comments: str,
        score: int,
    ) -> FeedbackEvent:
        event = FeedbackEvent(
            request_id=request_id,
            artifact_type=artifact_type,
            outcome=outcome,
            comments=comments,
            score=score,
        )
        self.store.append(event)
        return event
