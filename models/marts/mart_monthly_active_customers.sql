with customer_activity as (
    select
        customer_id,
        activity_date
    from analytics.customer_activity
    where activity_flag = true
)
select
    date_trunc('month', activity_date) as activity_month,
    count(distinct customer_id) as monthly_active_customers
from customer_activity
group by 1;
