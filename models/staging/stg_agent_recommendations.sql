select
    recommendation_id,
    task_id,
    agent_name,
    artifact_type,
    confidence_score::number(5,4) as confidence_score,
    artifact_path,
    review_status,
    review_version::number(10,0) as review_version,
    created_at::timestamp_ntz as created_at
from platform.agent_recommendations;
