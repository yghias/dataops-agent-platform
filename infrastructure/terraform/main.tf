terraform {
  required_version = ">= 1.6.0"
}

variable "environment" {
  type = string
}

locals {
  platform_name = "dataops-agent-platform"
  tags = {
    service     = local.platform_name
    environment = var.environment
    owner       = "data-platform"
  }
}

output "platform_context" {
  value = {
    platform_name = local.platform_name
    environment   = var.environment
    tags          = local.tags
  }
}
