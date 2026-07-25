# Troubleshooting

A summary of common problems and their solutions.

## Missing Environment Variables

If environment variables are causing errors in pipelines, confirm the following:

- Environment variable exists locally via `.env`

  ```sh
  export GCP_FOLDER_NAME=Development
  export GCP_FOLDER_ID=123456789012
  export GCP_PROJECT_ID=my-project-id-12345
  export GCP_PROJECT_NAME=my-project
  export GCP_ORGANIZATION_ID=12345687890
  ```

- Environment variable exists in the **Project Settings**

- Environment variable exists in GitHub Actions CICD

  ```yaml
  env:
  GCP_PROJECT_ID: ${{ vars.GCP_PROJECT_ID }}
  GCP_PROJECT_NAME: ${{ vars.GCP_PROJECT_NAME }}
  GCP_FOLDER_NAME: ${{ vars.GCP_FOLDER_NAME }}
  GCP_FOLDER_ID: ${{ vars.GCP_FOLDER_ID }}
  GCP_ORGANIZATION_ID: ${{ vars.GCP_ORGANIZATION_ID }}
  GCP_CREDENTIALS: ${{ secrets.GCP_CREDENTIALS }}
  ```
