"""Test Project Service."""

import os

import pytest

from gcp.domain.services.project import get_folders, get_project


@pytest.mark.unit
def test_get_project():
    """Test project retrieval."""
    project_name = os.getenv("GCP_PROJECT_ID")
    result = get_project(project_name)
    assert result.name == project_name  # Replace with the expected project name


@pytest.mark.integration
def test_get_folders():
    """Test folder retrieval."""
    organization_id = os.getenv("GCP_ORGANIZATION_ID")
    get_folders(organization_id=organization_id)
