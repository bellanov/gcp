"""Test Project Service."""

import os

import pytest

from cli.domain.services.project import get_project


@pytest.mark.integration
def test_get_project():
    """Test project retrieval."""
    result = get_project(
        project_id=os.getenv("GCP_PROJECT_ID"),
        name=os.getenv("GCP_PROJECT_NAME"),
        organization_id=os.getenv("GCP_ORGANIZATION_ID"),
    )
    assert result.id == os.getenv("GCP_PROJECT_ID")
    assert result.organization_id == os.getenv("GCP_ORGANIZATION_ID")
