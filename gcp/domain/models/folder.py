"""Folder Model."""

from pydantic import Field

from gcp.domain.models.pydantic import CamelCaseModel

GCP_FOLDER_NAME = r"^[a-z0-9\s\-_]+$"
GCP_FOLDER_ID = r"^[a-z0-9-]+$"


class Folder(CamelCaseModel):
    """Represents a folder.

    Attributes:
        id: The ID of the folder.
    """

    id: str = Field(..., pattern=GCP_FOLDER_ID)
    name: str = Field(..., pattern=GCP_FOLDER_NAME)
