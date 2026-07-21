"""List Organizational Folders."""

import os

from gcp.domain.services.project import get_project, get_folders

organization_id = os.getenv("GCP_ORGANIZATION_ID")
get_folders(organization_id=organization_id)
