#!/bin/bash
#
# Create GitHub Identity Pool.

gcloud config set project $GCP_PROJECT

# Create a Workload Identity Pool
gcloud iam workload-identity-pools delete "github-actions-pool" \
    --project="$GCP_PROJECT" \
    --location="global" \
    --quiet
