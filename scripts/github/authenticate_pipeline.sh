#!/bin/bash
#
# Authenticate GitHub Actions pipeline.

gcloud config set project $GCP_PROJECT

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format=value\(projectNumber\))
POOL_ID="github-actions-pool-1787166615"
MEMBER="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/attribute.repository/bellanov/google"
SERVICE_ACCOUNT="github-actions-1787170169@${GCP_PROJECT}.iam.gserviceaccount.com"


if gcloud storage buckets add-iam-policy-binding "gs://${GCP_PROJECT}" \
    --role=roles/iam.serviceAccountTokenCreator \
    --member="$MEMBER"; then
    echo "Bucket IAM policy binding applied."
else
    echo "Bucket IAM policy binding already exists."
fi

# Grant the WIF principal permission to impersonate the service account
if gcloud iam service-accounts add-iam-policy-binding \
    "$SERVICE_ACCOUNT" \
    --project="$GCP_PROJECT" \
    --role="roles/iam.serviceAccountTokenCreator" \
    --member="$MEMBER"; then
    echo "Workload Identity User binding applied."
else
    echo "Workload Identity User binding already exists."
fi
