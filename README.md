# gcp

**Command Line Interface (CLI)** to bootstrap development on _Google Cloud Platform (GCP)_.

# Environments

The project is deployed across multiple *environments*, each of which has its own Terraform configuration.

| Environment | Description |
| ----------- | ----------------------------------------------------------------- |
| _development_ | Development environment for testing and experimentation.          |
| _staging_   | Staging environment for pre-production testing.                   |
| _production_| Production environment for live deployment.                       |

*Terraform* configurations are located in the `terraform/environments` directory.

# Architecture

The project _architecture_ is summarized below.

![Project Architecture](./diagrams/Project.svg)

# Project Structure

The project _structure_ is summarized below.

```sh
gcp
├── .github
│   └── workflows
├── diagrams
├── docs
├── cli
│   └── domain
│       ├── models
│       └── services
├── terraform
│   └── environments
│       ├── development
│       ├── production
│       └── staging
└── tests
    ├── models
    └── services
```

| Environment | Description                                                       |
| ----------- | ----------------------------------------------------------------- |
| _.github_   | Contains GitHub **workflows** for CI/CD.                          |
| _diagrams_  | Contains project architecture **diagrams**.                       |
| _docs_      | Contains project **documentation**.                               |
| _cli_       | Contains project **source code** for GCP tooling.                 |
| _terraform_ | Contains **Terraform configurations** for different environments. |
| _tests_     | Contains **unit and integration tests** for the project.          |


# Workload Identity Federation

The project uses *[Direct Workload Identity Federation](https://github.com/google-github-actions/auth?tab=readme-ov-file#preferred-direct-workload-identity-federation)* to manage identities and access across different environments.

In this setup, the Workload Identity Pool has direct IAM permissions on Google Cloud resources; there are no intermediate service accounts or keys. This is preferred since it directly authenticates GitHub Actions to Google Cloud without a proxy resource. However, not all Google Cloud resources support principalSet identities, and the resulting token has a maximum lifetime of 10 minutes. Please see the documentation for your Google Cloud service for more information.

![Direct Workload Identity Federation](https://raw.githubusercontent.com/google-github-actions/auth/refs/heads/main/docs/google-github-actions-auth-direct-workload-identity-federation.svg)

| Workflow | Description |
| -------- | ----------------------------------------------------------------- |
| _cli-ci-\<environment\>_     | Continuous Integration workflow for testing and validating the `cli`.  |
| _cd-\<environment\>_     | Continuous Deployment workflow for *Terraform* deployments.  |
