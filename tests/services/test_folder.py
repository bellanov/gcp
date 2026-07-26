"""Test Folder Service."""

import os

import pytest

from gcp.domain.services.folder import get_folder, get_folders_for_organization

GCP_FOLDER_ID = os.getenv("GCP_FOLDER_ID")
GCP_FOLDER_NAME = os.getenv("GCP_FOLDER_NAME")
GCP_FOLDER_DISPLAY_NAME = os.getenv("GCP_FOLDER_DISPLAY_NAME")
GCP_ORGANIZATION_ID = os.getenv("GCP_ORGANIZATION_ID")


@pytest.mark.integration
def test_get_folders():
    """Test folder retrieval."""
    assert get_folders_for_organization(organization_id=GCP_ORGANIZATION_ID) is not None


@pytest.mark.unit
def test_get_folder():
    """Test folder retrieval by name."""
    result = get_folder(
        id=GCP_FOLDER_ID,
        folder_name=GCP_FOLDER_NAME
    )
