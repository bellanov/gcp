#!/bin/bash
#
# Assign roles to a Deployment Service Account for GitHub Actions.

gcloud config set project $GCP_PROJECT

TIMESTAMP=$(date +%s)

ROLES="roles/iam.serviceAccountAdmin
roles/serviceusage.serviceUsageAdmin"

SERVICE_ACCOUNT="github-actions"

# Check if the service account has the required roles, if not grant them
for role in $ROLES; do
    if ! gcloud projects get-iam-policy $GCP_PROJECT \
        --flatten="bindings[].members" \
        --format="table(bindings.role)" \
        --filter="bindings.members:${SERVICE_ACCOUNT}@${GCP_PROJECT}.iam.gserviceaccount.com" | grep -q "$role"; then
        gcloud projects add-iam-policy-binding $GCP_PROJECT \
            --member="serviceAccount:${SERVICE_ACCOUNT}@${GCP_PROJECT}.iam.gserviceaccount.com" \
            --role="$role"
        echo "Service account granted the role $role"
    else
        echo "Service account already has the role $role"
    fi
done
