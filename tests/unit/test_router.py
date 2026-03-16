from agents.base_agent import TaskRequest
from agents.data_analyst_agent import DataAnalystAgent
from agents.data_architect_agent import DataArchitectAgent
from agents.data_engineer_agent import DataEngineerAgent
from agents.documentation_agent import DocumentationAgent
from agents.observability_agent import ObservabilityAgent
from agents.router_agent import RouterAgent


def build_router() -> RouterAgent:
    agents = [
        DataEngineerAgent({}),
        DataArchitectAgent({}),
        DataAnalystAgent({}),
        ObservabilityAgent({}),
        DocumentationAgent({}),
    ]
    return RouterAgent(agents)


def test_router_prefers_data_engineer_for_pipeline_requests() -> None:
    router = build_router()
    task = TaskRequest(request_id="req-1", requester_role="data_engineer", prompt="Generate an Airflow DAG for a daily pipeline.")
    decision = router.route(task)
    assert decision.primary_agent == "data_engineer_agent"


def test_router_prefers_architect_for_schema_requests() -> None:
    router = build_router()
    task = TaskRequest(request_id="req-2", requester_role="data_architect", prompt="Review this schema for grain and dimensional modeling.")
    decision = router.route(task)
    assert decision.primary_agent == "data_architect_agent"
