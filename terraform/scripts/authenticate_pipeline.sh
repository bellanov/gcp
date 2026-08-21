#!/bin/bash
#
# Authenticate GitHub Actions pipeline.

gcloud config set project $GCP_PROJECT

gcloud iam service-accounts add-iam-policy-binding "github-actions-1787174527@${GCP_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"

gcloud storage buckets add-iam-policy-binding "gs://gcp-development-503118-1787174368" \
  --role="roles/storage.admin" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"
