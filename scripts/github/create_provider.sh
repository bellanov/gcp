#!/bin/bash
#
# Create GitHub Providers.

IDENTITY_POOL="${1}"

gcloud config set project $GCP_PROJECT

# Add or update the GitHub OIDC Provider in the Pool
if gcloud iam workload-identity-pools providers describe github-provider \
    --location="global" \
    --workload-identity-pool="$IDENTITY_POOL" \
    --project="$GCP_PROJECT" >/dev/null 2>&1; then
    echo "Provider already exists."
else
    gcloud iam workload-identity-pools providers create-oidc github-provider \
        --location="global" \
        --workload-identity-pool="$IDENTITY_POOL" \
        --project="$GCP_PROJECT" \
        --display-name="GitHub Provider" \
        --issuer-uri="https://token.actions.githubusercontent.com/" \
        --attribute-mapping="google.subject=assertion.sub" \
        --attribute-condition="assertion.repository=='bellanov/google'"
    echo "WIF provider created."
fi
