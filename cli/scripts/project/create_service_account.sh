#!/bin/bash
#
# Create a Deployment Service Account for GitHub Actions.

gcloud config set project $GCP_PROJECT

TIMESTAMP=$(date +%s)

if gcloud iam service-accounts create "github-actions-${TIMESTAMP}" \
        --description="Deployment service account for GitHub Actions" \
        --display-name="GitHub Actions Deployment Service Account"; then
    echo "Service account github-actions-${TIMESTAMP} created."
else
    echo "Failure creating Service Account { github-actions-${TIMESTAMP} } already exists."
fi
