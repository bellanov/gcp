"""Test Folder Service."""

import os

import pytest

from gcp.domain.services.folder import get_folder, get_folders


@pytest.mark.integration
def test_get_folders():
    """Test folder retrieval."""
    organization_id = os.getenv("GCP_ORGANIZATION_ID")
    get_folders(organization_id=organization_id)


@pytest.mark.unit
def test_get_folder():
    """Test folder retrieval by name."""
    result = get_folder(
        id=os.getenv("GCP_FOLDER_ID"),
        folder_name=os.getenv("GCP_FOLDER_NAME"),
    )
    assert result.id == os.getenv("GCP_FOLDER_ID")
    assert result.name == os.getenv("GCP_FOLDER_NAME")
