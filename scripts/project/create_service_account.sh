#!/bin/bash
#
# Create or update Deployment Service Account permissions.

gcloud config set project $GCP_PROJECT

TIMESTAMP=$(date +%s)

ROLES="roles/iam.serviceAccountAdmin
roles/storage.admin"

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format='value(projectNumber)')

# Check if the service account exists, if not create it
if ! gcloud iam service-accounts describe "github-actions-${TIMESTAMP}@${GCP_PROJECT}.iam.gserviceaccount.com" --project $GCP_PROJECT >/dev/null 2>&1; then
    gcloud iam service-accounts create "github-actions-${TIMESTAMP}" \
        --description="Deployment service account for GitHub Actions" \
        --display-name="GitHub Actions Deployment Service Account"

    echo "Service account github-actions-${TIMESTAMP} created."
else
    echo "Service account github-actions-${TIMESTAMP} already exists."
fi

# Check if the service account has the required roles, if not grant them
for role in $ROLES; do
    if ! gcloud projects get-iam-policy $GCP_PROJECT \
        --flatten="bindings[].members" \
        --format="table(bindings.role)" \
        --filter="bindings.members:github-actions-${TIMESTAMP}@${GCP_PROJECT}.iam.gserviceaccount.com" | grep -q "$role"; then
        gcloud projects add-iam-policy-binding $GCP_PROJECT \
            --member="serviceAccount:github-actions-${TIMESTAMP}@${GCP_PROJECT}.iam.gserviceaccount.com" \
            --role="$role"
        echo "Service account granted the role $role"
    else
        echo "Service account already has the role $role"
    fi
done
