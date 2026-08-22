#!/bin/bash
#
# Create GitHub Providers.

IDENTITY_POOL="${1}"

gcloud config set project $GCP_PROJECT

gcloud iam workload-identity-pools providers create-oidc "google" \
  --location="global" \
  --workload-identity-pool="github" \
  --display-name="My GitHub repo Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
  --attribute-condition="assertion.repository_owner == '${GITHUB_ORG}'" \
  --issuer-uri="https://token.actions.githubusercontent.com"

gcloud iam workload-identity-pools providers describe "google" \
  --location="global" \
  --workload-identity-pool="github" \
  --format="value(name)"