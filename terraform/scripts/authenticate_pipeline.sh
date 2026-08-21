#!/bin/bash
#
# Authenticate GitHub Actions pipeline.

gcloud config set project $GCP_PROJECT

SERVICE_ACCOUNT="github-actions-1787174527@${GCP_PROJECT}.iam.gserviceaccount.com"

# Grant workload identity user role to allow GitHub Actions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding "$SERVICE_ACCOUNT" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"

# Grant storage permissions to the service account itself (project-level)
gcloud projects add-iam-policy-binding "$GCP_PROJECT" \
  --role="roles/storage.folderAdmin" \
  --member="serviceAccount:$SERVICE_ACCOUNT"
