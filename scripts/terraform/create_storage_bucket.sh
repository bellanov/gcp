#!/bin/bash
#
# Create a Google Cloud Storage bucket for Terraform state.

gcloud storage buckets create gs://terraform-state-503118 \
    --default-storage-class=STANDARD \
    --location=US \
    --uniform-bucket-level-access \
    --public-access-prevention