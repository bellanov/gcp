#!/bin/bash
#
# Create a Deployment Service Account for GitHub Actions.

gcloud config set project $GCP_PROJECT

SERVICE_ACCOUNT="github-actions"

if gcloud iam service-accounts create "$SERVICE_ACCOUNT" \
        --description="Deployment service account for GitHub Actions" \
        --display-name="GitHub Actions Deployment Service Account"; then
    echo "Service account $SERVICE_ACCOUNT created."
else
    echo "Failure creating Service Account { $SERVICE_ACCOUNT } already exists."
fi
