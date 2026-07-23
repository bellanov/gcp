"""Project Model."""

from pydantic import Field

from gcp.domain.models.pydantic import CamelCaseModel

GCP_PROJECT = r"^[a-z0-9-]+$"


class Project(CamelCaseModel):
    """Represents a project.

    Attributes:
        name: The name of the project.
        id: The ID of the project.
    """

    # id: str = Field(..., pattern=GCP_PROJECT)
    name: str = Field(..., pattern=GCP_PROJECT)
    # number: int
    