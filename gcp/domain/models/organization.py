"""Organization Model."""

from pydantic import Field

from gcp.domain.models.pydantic import CamelCaseModel

GCP_ORGANIZATION = r"^[a-z0-9-]+$"


class Organization(CamelCaseModel):
    """Represents an organization.

    Attributes:
        id: The ID of the organization.
        name: The name of the organization.
    """

    id: str = Field(..., pattern=GCP_ORGANIZATION)
    name: str
