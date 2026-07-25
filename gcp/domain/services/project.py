"""Project Service."""

# from google.cloud import resourcemanager_v3

from gcp.domain.models.project import Project


def get_project(project_id: str, name: str, organization_id: str) -> Project:
    """Get a project by ID.

    Args:
        project_id: The ID of the project.
        name: The name of the project.
        organization_id: The ID of the organization the project belongs to.

    Returns:
        A Project object.
    """
    return Project(id=project_id, name=name, organization_id=organization_id)
