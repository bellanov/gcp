
output "services" {
  description = "List of enabled services"
  value       = resource.google_project_service.service[*].service
}