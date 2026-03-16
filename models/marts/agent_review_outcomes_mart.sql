select
    assigned_agent,
    request_type,
    environment,
    count(*) as total_recommendations,
    count_if(review_decision = 'approved') as approved_recommendations,
    count_if(review_decision = 'rejected') as rejected_recommendations,
    round(count_if(review_decision = 'approved') / nullif(count(*), 0), 4) as approval_rate,
    avg(minutes_to_review) as avg_minutes_to_review
from {{ ref('int_task_review_cycle') }}
group by 1, 2, 3;
