#!/bin/bash
#
# Grant permissions to the Workload Identity User.

gcloud config set project $GCP_PROJECT

SERVICE_ACCOUNT="github-actions-1787174527@${GCP_PROJECT}.iam.gserviceaccount.com"

# Grant workload identity user role to allow GitHub Actions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding "$SERVICE_ACCOUNT" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"

gcloud storage buckets add-iam-policy-binding "gs://$GCP_PROJECT" \
    --member="principalSet://iam.googleapis.com/projects/<PROJECT_NUMBER>/locations/global/workloadIdentityPools/<POOL_ID>/*" \
    --role="roles/storage.objectUser"

