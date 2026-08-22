
output "services" {
  description = "List of enabled services"
  value       = { for service in resource.google_project_service.service : service.id => service }
}