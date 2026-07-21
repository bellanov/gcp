#!/bin/bash
#
# Generate default application credentials.

GCP_PROJECT=$(gcloud config get-value project)

echo "Generating default application credentials..."
gcloud auth application-default login

echo "Setting quota project..."
gcloud auth application-default set-quota-project ${GCP_PROJECT}
