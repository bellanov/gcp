#!/bin/bash
#
# Update GitHub Providers.

IDENTITY_POOL="${1}"

gcloud config set project $GCP_PROJECT

gcloud iam workload-identity-pools providers update-oidc github-provider \
        --location="global" \
        --workload-identity-pool="$IDENTITY_POOL" \
        --project="$GCP_PROJECT" \
        --attribute-mapping="google.subject=assertion.sub" \
        --attribute-condition="assertion.repository=='bellanov/google'"
    echo "WIF provider updated."