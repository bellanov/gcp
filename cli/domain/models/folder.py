"""Folder Model."""

from pydantic import Field

from cli.domain.models.pydantic import CamelCaseModel

GCP_FOLDER_NAME = r"^(folders|organizations)/[0-9]+$"
GCP_FOLDER_DISPLAY_NAME = r"^[a-zA-Z0-9][a-zA-Z0-9 _-]{1,28}[a-zA-Z0-9]$"


class Folder(CamelCaseModel):
    """Represents a folder.

    Attributes:
        id: The ID of the folder.
        name: The name of the folder.
    """

    name: str = Field(..., pattern=GCP_FOLDER_NAME)
    parent: str = Field(..., pattern=GCP_FOLDER_NAME)
    display_name: str = Field(..., pattern=GCP_FOLDER_DISPLAY_NAME)
