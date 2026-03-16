from workflows.intake_workflow import IntakeWorkflow


def test_intake_workflow_produces_review_packet() -> None:
    workflow = IntakeWorkflow()
    result = workflow.run("Optimize a Snowflake SQL query for the sales pipeline mart.")
    assert result["approval_packet"]["review_required"] is True
    assert result["approval_packet"]["artifacts"]
