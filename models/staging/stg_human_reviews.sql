select
    review_id,
    task_id,
    recommendation_id,
    reviewer_role,
    review_decision,
    review_notes,
    reviewed_at::timestamp_ntz as reviewed_at
from platform.human_reviews;
