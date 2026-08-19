#!/bin/bash
#
# Authenticate GitHub Actions pipeline.



gcloud config set project $GCP_PROJECT

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format=value\(projectNumber\))


gcloud storage buckets add-iam-policy-binding "gs://${GCP_PROJECT}" \
    --role=roles/storage.admin \
    --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github-actions-pool-1787030079/subject/assertion.sub"

# Grant the WIF principal permission to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding \
    "github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
    --project="$GCP_PROJECT" \
    --role="roles/iam.serviceAccountTokenCreator" \
    --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github-actions-pool-1787030079/*"
echo "Workload Identity User binding applied."

    