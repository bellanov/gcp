#!/bin/bash
#
# Grant permissions to the Workload Identity User.

gcloud config set project $GCP_PROJECT

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format=value\(projectNumber\))
SERVICE_ACCOUNT="github-actions@${GCP_PROJECT}.iam.gserviceaccount.com"

# Grant project-level permissions for API management
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/serviceusage.serviceUsageAdmin"

# Grant permissions to create and manage service accounts
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/iam.serviceAccountAdmin"

# Grant permissions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding "$SERVICE_ACCOUNT" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WORKLOAD_IDENTITY_POOL}/attribute.repository/${REPO}"

# Grant permissions to access Terraform state
gcloud storage buckets add-iam-policy-binding "gs://$GCP_PROJECT" \
    --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WORKLOAD_IDENTITY_POOL}/*" \
    --role="roles/storage.objectUser"
