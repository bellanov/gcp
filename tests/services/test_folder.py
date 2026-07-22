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
    folder_name = os.getenv("GCP_FOLDER_NAME")
    result = get_folder(folder_name=folder_name)
    assert result.id == folder_name
    assert result.name == folder_name
