"""List Organizational Folders."""

import os

from gcp.domain.services.folder import get_folders

print("Retrieving folders...")
get_folders(organization_id=os.getenv("GCP_ORGANIZATION_ID"))
