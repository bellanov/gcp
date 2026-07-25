"""Project Model."""

from pydantic import Field

from gcp.domain.models.pydantic import CamelCaseModel

GCP_PROJECT = r"^[a-z0-9-]+$"


class Project(CamelCaseModel):
    """Represents a project.

    Attributes:
        id: The ID of the project.
        organization_id: The ID of the organization the project belongs to.
    """

    id: str = Field(..., pattern=GCP_PROJECT)
    name: str
    organization_id: str = Field(..., pattern=GCP_PROJECT)
