"""Test Project Service."""

import os

import pytest

from gcp.domain.services.project import get_project


@pytest.mark.unit
def test_get_project():
    """Test project retrieval."""
    project_id = os.getenv("GCP_PROJECT_ID")
    result = get_project(project_id=project_id)
    assert result.id == project_id
