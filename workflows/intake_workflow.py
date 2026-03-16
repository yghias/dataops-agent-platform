"""Entry point for request intake, routing, and draft generation."""

from __future__ import annotations

from pprint import pprint
from uuid import uuid4

from agents.ai_ml_engineer_agent import AiMlEngineerAgent
from agents.base_agent import AgentResult, TaskRequest
from agents.cloud_platform_agent import CloudPlatformAgent
from agents.data_analyst_agent import DataAnalystAgent
from agents.data_architect_agent import DataArchitectAgent
from agents.data_engineer_agent import DataEngineerAgent
from agents.data_scientist_agent import DataScientistAgent
from agents.database_engineer_agent import DatabaseEngineerAgent
from agents.dba_agent import DbaAgent
from agents.documentation_agent import DocumentationAgent
from agents.observability_agent import ObservabilityAgent
from agents.router_agent import RouterAgent
from tools.dag_generator import DagGenerator
from tools.dbt_generator import DbtGenerator
from tools.doc_generator import DocGenerator
from tools.lineage_tool import LineageTool
from tools.metadata_reader import MetadataReader
from tools.quality_checker import QualityChecker
from tools.query_optimizer import QueryOptimizer
from tools.schema_inspector import SchemaInspector
from tools.sql_runner import SqlRunner
from workflows.approval_workflow import ApprovalWorkflow


class IntakeWorkflow:
    """Coordinates request normalization, routing, and agent execution."""

    def __init__(self) -> None:
        self.tools = {
            "schema": SchemaInspector(),
            "metadata": MetadataReader(),
            "lineage": LineageTool(),
            "dag_generator": DagGenerator(),
            "dbt_generator": DbtGenerator(),
            "doc_generator": DocGenerator(),
            "query_optimizer": QueryOptimizer(),
            "sql_runner": SqlRunner(),
            "quality": QualityChecker(),
        }
        self.agents = [
            DataEngineerAgent(self.tools),
            DataArchitectAgent(self.tools),
            CloudPlatformAgent(self.tools),
            DatabaseEngineerAgent(self.tools),
            DbaAgent(self.tools),
            DataAnalystAgent(self.tools),
            DataScientistAgent(self.tools),
            AiMlEngineerAgent(self.tools),
            ObservabilityAgent(self.tools),
            DocumentationAgent(self.tools),
        ]
        self.router = RouterAgent(self.agents)
        self.approval_workflow = ApprovalWorkflow()

    def classify_domain(self, prompt: str) -> str:
        lowered = prompt.lower()
        if any(word in lowered for word in ("dag", "airflow", "etl", "elt", "pipeline")):
            return "data_engineering"
        if any(word in lowered for word in ("schema", "architecture", "model")):
            return "architecture"
        if any(word in lowered for word in ("query", "sql", "optimize")):
            return "sql"
        if any(word in lowered for word in ("metric", "kpi", "dashboard")):
            return "metrics"
        if any(word in lowered for word in ("feature", "training", "ml", "scoring")):
            return "ml"
        return "general"

    def run(self, prompt: str, requester_role: str = "data_engineer", environment: str = "dev") -> dict:
        inferred_title = "Request review package"
        if "pipeline" in prompt.lower():
            inferred_title = "Pipeline implementation package"
        if "query" in prompt.lower() or "sql" in prompt.lower():
            inferred_title = "SQL optimization package"
        task = TaskRequest(
            request_id=f"req-{uuid4()}",
            requester_role=requester_role,
            prompt=prompt,
            environment=environment,
            domain=self.classify_domain(prompt),
            context={"title": inferred_title, "owner": requester_role},
        )
        route = self.router.route(task)
        selected = [agent for agent in self.agents if agent.name in {route.primary_agent, *route.supporting_agents}]
        results: list[AgentResult] = [agent.run(task) for agent in selected]
        approval_packet = self.approval_workflow.package_for_review(task, route, results)
        return {
            "task": task,
            "route": route,
            "results": results,
            "approval_packet": approval_packet,
        }


def main() -> None:
    workflow = IntakeWorkflow()
    review_packet = workflow.run(
        "Generate an Airflow DAG, Snowflake staging model, and observability package for daily CRM to warehouse ingestion."
    )
    pprint(review_packet["approval_packet"])


if __name__ == "__main__":
    main()
