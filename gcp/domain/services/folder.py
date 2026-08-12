"""Folder Service."""

from typing import Generator

from gcp.domain.models.folder import Folder
from google.cloud import resourcemanager_v3


def get_folder(id: str, folder_name: str) -> Folder:
    """Get a folder by name.

    Args:
        id: The ID of the folder.
        folder_name: The name of the folder.

    Returns:
        A Folder object.
    """
    pass


def get_folders_for_organization(organization_id: str) -> Generator[Folder, None, None]:
    """Get all folders for an organization.
    Args:
        organization_id: The ID of the organization.

    Returns:
        A generator of Folder objects.
    """
    client = resourcemanager_v3.FoldersClient()
    request = resourcemanager_v3.ListFoldersRequest(
        parent=f"organizations/{organization_id}",
    )
    page_result = client.list_folders(request=request)

    for response in page_result:
        print(response)
        folder = Folder(
            name=response.name,
            display_name=response.display_name,
            parent=response.parent,
        )
        yield folder
