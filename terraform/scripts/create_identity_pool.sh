#!/bin/bash
#
# Create GitHub Identity Pool.

TIMESTAMP=$(date +%s)

gcloud config set project $GCP_PROJECT

# Create a Workload Identity Pool
gcloud iam workload-identity-pools create "github-actions-pool-$TIMESTAMP" \
    --project="$GCP_PROJECT" \
    --location="global" \
    --display-name="GitHub Actions Pool"
