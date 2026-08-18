#!/bin/bash
#
# Authenticate GitHub Actions pipeline.



gcloud config set project $GCP_PROJECT

PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format=value\(projectNumber\))


gcloud storage buckets add-iam-policy-binding "gs://${GCP_PROJECT}" \
    --role=roles/storage.objectViewer \
    --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github-actions-pool-1787030079/subject/assertion.sub"