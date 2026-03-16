variable "snowflake_database" {
  type        = string
  description = "Snowflake database name for platform-managed schemas."
  default     = "ANALYTICS"
}

variable "airflow_environment" {
  type        = string
  description = "Airflow deployment identifier."
  default     = "data-platform-airflow"
}
