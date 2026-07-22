"""Project Service."""

from google.cloud import resourcemanager_v3

from gcp.domain.models.project import Project


def get_project(project_id: str) -> Project:
    """Get a project by ID.

    Args:
        project_id: The ID of the project.

    Returns:
        A Project object.
    """
    return Project(id=project_id)
