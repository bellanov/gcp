
provider "google" {
  project = var.project_id
}

resource "google_service_account" "service_account" {
  account_id   = "developer"
  display_name = "Service Account for local development"
}

locals {
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