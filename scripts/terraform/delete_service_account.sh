#!/bin/bash
#
# Delete Deployment Service Account.

gcloud config set project $GCP_PROJECT
gcloud iam service-accounts delete github-actions-deploy-sa@${GCP_PROJECT}.iam.gserviceaccount.com
