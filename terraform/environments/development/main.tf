
provider "google" {
  project = "gcp-development-503118"
}

resource "google_service_account" "service_account" {
  account_id   = "developer-sa"
  display_name = "Service Account for local development"
}