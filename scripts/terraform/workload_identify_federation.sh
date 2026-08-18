#!/bin/bash
#
# Establish Workload Identity Federation for GitHub Actions to access Google Cloud resources.

gcloud config set project $GCP_PROJECT

# Create a Workload Identity Pool
gcloud iam workload-identity-pools create "github-actions-pool" \
    --project="$GCP_PROJECT" \
    --location="global" \
    --display-name="GitHub Actions Pool"

# Add the GitHub OIDC Provider to the Pool
gcloud iam workload-identity-pools providers create-oidc github-provider \
    --location="global" \
    --workload-identity-pool="github-actions-pool" \
    --display-name="GitHub Provider" \
    --issuer-uri="https://token.actions.githubusercontent.com/" \
    --attribute-mapping="google.subject=assertion.sub" \
    --attribute-condition="assertion.repository_owner=='bellanov' && assertion.repository=='bellanov/google'"