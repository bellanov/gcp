# gcp

Tools to bootstrap development on _Google Cloud Platform (GCP)_.

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
├── scripts
│   ├── ci
│   ├── gcp
│   └── sa
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
| _scripts_   | Contains **utility scripts** for managing the project.            |
| _terraform_ | Contains **Terraform configurations** for different environments. |
| _tests_     | Contains **unit and integration tests** for the project.          |
