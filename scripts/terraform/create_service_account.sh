#!/bin/bash
#
# Create or update Deployment Service Account permissions.

gcloud config set project $GCP_PROJECT

ROLES="roles/iam.serviceAccountAdmin
roles/storage.admin"

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format='value(projectNumber)')

# Check if the service account exists, if not create it
if ! gcloud iam service-accounts describe "github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" --project $GCP_PROJECT >/dev/null 2>&1; then
    gcloud iam service-accounts create github-actions-deploy-sa \
        --description="Deployment service account for GitHub Actions" \
        --display-name="GitHub Actions Deployment Service Account"

    echo "Service account github-actions-deploy-sa created."
else
    echo "Service account github-actions-deploy-sa already exists."
fi

# Check if the service account has the required roles, if not grant them
for role in $ROLES; do
    if ! gcloud projects get-iam-policy $GCP_PROJECT \
        --flatten="bindings[].members" \
        --format="table(bindings.role)" \
        --filter="bindings.members:github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" | grep -q "$role"; then
        gcloud projects add-iam-policy-binding $GCP_PROJECT \
            --member="serviceAccount:github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
            --role="$role"
        echo "Service account granted the role $role"
    else
        echo "Service account already has the role $role"
    fi
done

# Allow the WIF principal set to impersonate this service account
gcloud iam service-accounts add-iam-policy-binding \
    "github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
    --project="$GCP_PROJECT" \
    --role="roles/iam.workloadIdentityUser" \
    --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github-actions-pool/attribute.repository/bellanov/google"
echo "Workload Identity User binding applied to service account."
