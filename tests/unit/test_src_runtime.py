from src.orchestration.runtime import run_request


def test_src_runtime_returns_review_packet() -> None:
    packet = run_request("Generate a Snowflake pipeline and dbt transformation package.")
    assert packet["review_status"] == "pending_human_review"
    assert packet["artifacts"]
