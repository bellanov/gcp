
terraform {
  backend "gcs" {
    bucket = "terraform-state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.44.0"
    }
  }
}

resource "google_service_account" "service_account" {
  account_id   = "developer-sa"
  display_name = "Service Account for local development"
}