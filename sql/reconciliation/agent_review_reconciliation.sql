with recommendations as (
    select task_id, count(*) as recommendation_count
    from platform.agent_recommendations
    group by 1
),
reviews as (
    select task_id, count(*) as review_count
    from platform.human_reviews
    group by 1
)
select
    r.task_id,
    r.recommendation_count,
    coalesce(rv.review_count, 0) as review_count
from recommendations r
left join reviews rv
    on r.task_id = rv.task_id
where coalesce(rv.review_count, 0) > r.recommendation_count;
