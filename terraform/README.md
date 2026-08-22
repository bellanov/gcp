# Terraform Deployment

*Terraform* is used to deploy infrastructure into the `development`, `staging`, and `production` environments.
 
| Environment | Description |
|---|---|
| *development* | Manages infrastructure undergoing **development**. |
| *staging* | Manages infrastructure undergoing **validation**. |
| *production* | Manages infrastructure that is **customer-facing**. |

Various *Scripts* are available to support the deployment of infrastructure.

| Script | Description |
|---|---|
| *ci* | Scripts to **lint** and **format** the codebase. |
| *project* | Scripts to establish the **Workload Identity Federation (WIF)**. |
