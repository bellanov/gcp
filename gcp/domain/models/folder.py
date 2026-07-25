"""Folder Model."""

from pydantic import Field

from gcp.domain.models.pydantic import CamelCaseModel

GCP_FOLDER_NAME = r"^[a-zA-Z0-9][a-zA-Z0-9 _-]{1,28}[a-zA-Z0-9]$"
GCP_FOLDER_ID = r"^[a-z0-9-]+$"


class Folder(CamelCaseModel):
    """Represents a folder.

    Attributes:
        id: The ID of the folder.
    """

    id: str = Field(..., pattern=GCP_FOLDER_ID)
    name: str = Field(..., pattern=GCP_FOLDER_NAME)
