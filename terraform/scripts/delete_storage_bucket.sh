#!/bin/bash
#
# Delete the Google Cloud Storage bucket for Terraform state.

gcloud storage buckets delete gs://terraform-state-503118
