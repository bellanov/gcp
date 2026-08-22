
provider "google" {
  project = var.project_id
}

resource "google_project_service" "service" {
  for_each = toset(local.services)
  project  = var.project_id
  service  = each.value

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_service_account" "service_account" {
  account_id   = "developer"
  display_name = "Service Account for local development"

  depends_on = [
    google_project_service.service
  ]
}

locals {
  services = []

  # TODO: Dynamically generate service accounts and roles based on a map of service accounts and their roles
  service_accounts = {
    developer = {
      roles = [
        "roles/iam.serviceAccountUser",
        "roles/iam.serviceAccountTokenCreator",
        "roles/iam.workloadIdentityUser",
      ]
    }
  }
}