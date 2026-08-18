#!/bin/bash
#
# Create or update Deployment Service Account permissions.

gcloud config set project $GCP_PROJECT

ROLES="roles/iam.serviceAccountAdmin
roles/storage.admin"

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

# Check if the service account has the required roles, if not grant them
if ! gcloud projects add-iam-policy-binding $GCP_PROJECT \
    --member="serviceAccount:github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
    --role="roles/storage.admin" >/dev/null 2>&1; then
    gcloud projects add-iam-policy-binding $GCP_PROJECT \
        --member="serviceAccount:github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
        --role="roles/storage.admin"
    echo "Service account granted the role roles/storage.admin"
else
    echo "Service account already has the role roles/storage.admin"
fi
