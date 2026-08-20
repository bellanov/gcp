"""List Organizational Folders."""

import os

from cli.domain.services.folder import get_folders_for_organization

# TODO: Integrate rich for more user-friendly output

print("Retrieving folders...")

folders = get_folders_for_organization(organization_id=os.getenv("GCP_ORGANIZATION_ID"))
for folder in folders:
    print(f"Folder Name: {folder.name}")
    print(f"Folder Display Name: {folder.display_name}")
    print(f"Folder Parent: {folder.parent}")
