"""Folder Service."""

from google.cloud import resourcemanager_v3

from gcp.domain.models.folder import Folder


def get_folder(folder_name: str) -> Folder:
    """Get a folder by name.

    Args:
        folder_name: The name of the folder.

    Returns:
        A Folder object.
    """
    return Folder(id=folder_name, name=folder_name)


def get_folders(organization_id: str):
    # Create a client
    client = resourcemanager_v3.FoldersClient()

    # Initialize request argument(s)
    request = resourcemanager_v3.ListFoldersRequest(
        parent=f"organizations/{organization_id}",
    )

    # Make the request
    page_result = client.list_folders(request=request)

    # Handle the response
    for response in page_result:
        print(response)
