"""Project Service."""

import googleapiclient.discovery
from google.cloud import resourcemanager_v3

from gcp.domain.models.project import Project


def get_project(project_name: str) -> Project:
    """Get a project by name.

    Args:
        project_name: The name of the project.

    Returns:
        A Project object.
    """
    return Project(name=project_name)


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
