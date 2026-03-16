select *
from analytics.mart_sales_pipeline
where lifecycle_status = 'OPEN'
  and stage_name in ('CLOSED_WON', 'CLOSED_LOST');
