from src.common.contracts import TaskEnvelope
from src.orchestration.agent_router import AgentRouter


def test_query_requests_route_to_database_engineer_before_pipeline_agent() -> None:
    router = AgentRouter()
    task = TaskEnvelope(
        task_id="task_1",
        requester_role="data_engineer",
        request_type="optimize_query",
        prompt="Optimize a slow query for pipeline health reporting.",
        environment="dev",
    )
    route = router.route(task)
    assert route.primary_agent == "database_engineer_agent"
