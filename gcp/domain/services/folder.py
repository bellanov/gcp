"""Folder Service."""

from google.cloud import resourcemanager_v3

from gcp.domain.models.folder import Folder


def get_folder(id: str, folder_name: str) -> Folder:
    """Get a folder by name.

    Args:
        id: The ID of the folder.
        folder_name: The name of the folder.

    Returns:
        A Folder object.
    """
    return Folder(id=id, name=folder_name)


def get_folders_for_organization(organization_id: str):
    """Get all folders for an organization."""
    client = resourcemanager_v3.FoldersClient()
    request = resourcemanager_v3.ListFoldersRequest(
        parent=f"organizations/{organization_id}",
    )
    page_result = client.list_folders(request=request)

    for response in page_result:
        print(response)
