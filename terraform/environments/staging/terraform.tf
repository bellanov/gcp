terraform {
  backend "gcs" {
    bucket = "terraform-state-503118"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.44.0"
    }
  }
}