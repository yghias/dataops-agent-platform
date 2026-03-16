create schema if not exists platform;
create schema if not exists raw;
create schema if not exists staging;
create schema if not exists transformations;
create schema if not exists marts;

create or replace table platform.data_assets (
    asset_id varchar primary key,
    asset_name varchar not null,
    asset_type varchar not null,
    domain_name varchar not null,
    owner_role varchar not null,
    sensitivity_class varchar not null,
    sla_minutes number(10,0),
    created_at timestamp_ntz not null,
    updated_at timestamp_ntz not null
);

create or replace table platform.pipeline_runs (
    run_id varchar primary key,
    pipeline_id varchar not null,
    dag_id varchar not null,
    status varchar not null,
    started_at timestamp_ntz not null,
    ended_at timestamp_ntz,
    retry_count number(10,0) default 0,
    error_class varchar,
    error_message varchar,
    environment varchar not null
);

create or replace table platform.table_lineage (
    lineage_id varchar primary key,
    upstream_asset_id varchar not null references platform.data_assets(asset_id),
    downstream_asset_id varchar not null references platform.data_assets(asset_id),
    transform_layer varchar not null,
    transform_name varchar not null,
    created_at timestamp_ntz not null
);

create or replace table platform.data_quality_results (
    quality_result_id varchar primary key,
    run_id varchar references platform.pipeline_runs(run_id),
    asset_id varchar references platform.data_assets(asset_id),
    check_name varchar not null,
    check_type varchar not null,
    measured_value number(18,4),
    threshold_value number(18,4),
    status varchar not null,
    measured_at timestamp_ntz not null
);

create or replace table platform.query_history (
    query_id varchar primary key,
    warehouse_name varchar not null,
    user_name varchar not null,
    schema_name varchar not null,
    query_text varchar not null,
    query_hash varchar not null,
    bytes_scanned number(38,0),
    rows_produced number(38,0),
    execution_ms number(18,0),
    started_at timestamp_ntz not null,
    completed_at timestamp_ntz
);

create or replace table platform.model_registry (
    model_version_id varchar primary key,
    model_name varchar not null,
    version_label varchar not null,
    training_dataset varchar not null,
    evaluation_score number(18,6),
    status varchar not null,
    created_at timestamp_ntz not null
);

create or replace table platform.agent_tasks (
    task_id varchar primary key,
    requester_role varchar not null,
    request_type varchar not null,
    environment varchar not null,
    task_status varchar not null,
    assigned_agent varchar not null,
    approval_required boolean not null,
    submitted_at timestamp_ntz not null,
    updated_at timestamp_ntz,
    completed_at timestamp_ntz
);

create or replace table platform.agent_recommendations (
    recommendation_id varchar primary key,
    task_id varchar not null references platform.agent_tasks(task_id),
    agent_name varchar not null,
    artifact_type varchar not null,
    confidence_score number(5,4) not null,
    artifact_path varchar not null,
    review_status varchar not null,
    review_version number(10,0) default 1,
    created_at timestamp_ntz not null
);

create or replace table platform.human_reviews (
    review_id varchar primary key,
    task_id varchar not null references platform.agent_tasks(task_id),
    recommendation_id varchar not null references platform.agent_recommendations(recommendation_id),
    reviewer_role varchar not null,
    review_decision varchar not null,
    review_notes varchar,
    reviewed_at timestamp_ntz not null
);

create or replace table platform.execution_events (
    execution_event_id varchar primary key,
    task_id varchar not null references platform.agent_tasks(task_id),
    recommendation_id varchar not null references platform.agent_recommendations(recommendation_id),
    execution_status varchar not null,
    executed_by varchar not null,
    execution_notes varchar,
    executed_at timestamp_ntz not null
);

create or replace table platform.schema_versions (
    schema_version_id varchar primary key,
    source_system varchar not null,
    entity_name varchar not null,
    version_number number(10,0) not null,
    schema_payload variant not null,
    drift_type varchar,
    effective_at timestamp_ntz not null
);
