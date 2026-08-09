#!/bin/bash
#
# Create Deployment Service Account.

gcloud config set project $GCP_PROJECT

gcloud iam service-accounts create github-actions-deploy-sa \
    --description="Deployment service account for GitHub Actions" \
    --display-name="GitHub Actions Deployment Service Account"

gcloud projects add-iam-policy-binding $GCP_PROJECT \
    --member="serviceAccount:github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountAdmin"
