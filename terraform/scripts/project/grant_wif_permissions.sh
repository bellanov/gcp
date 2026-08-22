#!/bin/bash
#
# Grant permissions to the Workload Identity User.
# 
# Prerequisites: The user running this script must have the following roles:
# - Service Account Admin (to create/manage service accounts)
# - Service Usage Admin (to enable APIs)
# - Storage Admin (to manage buckets)
# - IAM Security Admin (to bind IAM policies)

gcloud config set project $GCP_PROJECT

# Grant permissions for API management
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="${WIF_PRINCIPAL}" \
  --role="roles/serviceusage.serviceUsageAdmin"

# Grant permissions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding "$SERVICE_ACCOUNT" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WORKLOAD_IDENTITY_POOL}/attribute.repository/${REPO}"

# Grant permissions to access Terraform state
gcloud storage buckets add-iam-policy-binding "gs://$GCP_PROJECT" \
    --member="${WIF_PRINCIPAL}" \
    --role="roles/storage.objectUser"

# Grant permissions for service account management
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="${WIF_PRINCIPAL}" \
  --role="roles/iam.serviceAccountAdmin"
