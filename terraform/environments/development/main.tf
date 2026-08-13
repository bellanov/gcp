
resource "google_service_account" "service_account" {
  account_id   = "github-actions-deploy-sa"
  display_name = "Service Account to deploy via GitHub Actions"
}