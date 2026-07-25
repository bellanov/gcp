"""List Organizational Folders."""

import os

from gcp.domain.services.folder import get_folders_for_organization

# TODO: Integrate rich for more user-friendly output

print("Retrieving folders...")
get_folders_for_organization(organization_id=os.getenv("GCP_ORGANIZATION_ID"))
