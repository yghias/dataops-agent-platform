with tasks as (
    select * from {{ ref('stg_agent_tasks') }}
),
recommendations as (
    select * from {{ ref('stg_agent_recommendations') }}
),
reviews as (
    select * from {{ ref('stg_human_reviews') }}
),
executions as (
    select * from {{ ref('stg_execution_events') }}
)
select
    t.task_id,
    t.request_type,
    t.assigned_agent,
    t.environment,
    r.recommendation_id,
    r.artifact_type,
    r.confidence_score,
    rv.review_decision,
    rv.reviewed_at,
    e.execution_status,
    e.executed_at,
    datediff('minute', t.submitted_at, rv.reviewed_at) as minutes_to_review,
    datediff('minute', rv.reviewed_at, e.executed_at) as minutes_review_to_execution
from tasks t
left join recommendations r
    on t.task_id = r.task_id
left join reviews rv
    on r.recommendation_id = rv.recommendation_id
left join executions e
    on r.recommendation_id = e.recommendation_id;
