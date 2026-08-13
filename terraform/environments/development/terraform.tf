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