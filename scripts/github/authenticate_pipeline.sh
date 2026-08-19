#!/bin/bash
#
# Authenticate GitHub Actions pipeline.



gcloud config set project $GCP_PROJECT

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format=value\(projectNumber\))
POOL_ID="github-actions-pool-1787166615"


if gcloud storage buckets add-iam-policy-binding "gs://${GCP_PROJECT}" \
    --role=roles/storage.admin \
    --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/subject/assertion.repository=='bellanov/google'"; then
    echo "Bucket IAM policy binding applied."
else
    echo "Bucket IAM policy binding already exists."
fi

# Grant the WIF principal permission to impersonate the service account
if gcloud iam service-accounts add-iam-policy-binding \
    "github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
    --project="$GCP_PROJECT" \
    --role="roles/iam.serviceAccountTokenCreator" \
    --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/attribute.repository/'bellanov/google'"; then
    echo "Workload Identity User binding applied."
else
    echo "Workload Identity User binding already exists."
fi