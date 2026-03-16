"""Simple runtime entrypoint for src-based orchestration."""

from __future__ import annotations

from uuid import uuid4

from src.agents.cloud_agent import CloudDataPlatformAgent
from src.agents.data_analyst_agent import DataAnalystAgent
from src.agents.data_architect_agent import DataArchitectAgent
from src.agents.data_engineer_agent import DataEngineerAgent
from src.agents.data_scientist_agent import DataScientistAgent
from src.agents.database_engineer_agent import DatabaseEngineerAgent
from src.agents.dba_agent import DbaAgent
from src.agents.documentation_agent import DocumentationAgent
from src.agents.ml_agent import MlEngineerAgent
from src.agents.observability_agent import ObservabilityAgent
from src.common.contracts import TaskEnvelope
from src.common.review import build_review_packet
from src.orchestration.agent_router import AgentRouter
from src.tools.dbt_generator_shim import DbtGeneratorShim
from src.tools.metadata_reader import MetadataReader
from src.tools.pipeline_diagnostics import PipelineDiagnostics
from src.tools.query_optimizer import QueryOptimizer
from src.tools.schema_inspector import SchemaInspector
from src.tools.sql_runner import SqlRunner


def run_request(prompt: str, request_type: str = "pipeline_generation", environment: str = "dev") -> dict:
    tools = {
        "sql_runner": SqlRunner(),
        "metadata_reader": MetadataReader(),
        "query_optimizer": QueryOptimizer(),
        "schema_inspector": SchemaInspector(),
        "dbt_generator": DbtGeneratorShim(),
        "pipeline_diagnostics": PipelineDiagnostics(),
    }
    agents = {
        "data_engineer_agent": DataEngineerAgent(tools),
        "data_architect_agent": DataArchitectAgent(tools),
        "cloud_data_platform_agent": CloudDataPlatformAgent(tools),
        "dba_agent": DbaAgent(tools),
        "data_analyst_agent": DataAnalystAgent(tools),
        "data_scientist_agent": DataScientistAgent(tools),
        "ai_ml_engineer_agent": MlEngineerAgent(tools),
        "database_engineer_agent": DatabaseEngineerAgent(tools),
        "observability_agent": ObservabilityAgent(tools),
        "documentation_agent": DocumentationAgent(tools),
    }
    task = TaskEnvelope(
        task_id=f"task_{uuid4()}",
        requester_role="data_engineer",
        request_type=request_type,
        prompt=prompt,
        environment=environment,
        payload={"dag_id": "platform_metadata_ingestion"},
    )
    router = AgentRouter()
    route = router.route(task)
    primary = agents.get(route.primary_agent)
    artifacts = [primary.run(task)] if primary else []
    return build_review_packet(task, artifacts, route.reason)
