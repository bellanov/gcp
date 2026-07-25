"""Test Project Model."""

import pytest
from pydantic import ValidationError

from gcp.domain.models.project import Project


@pytest.mark.unit
class TestProject:
    """Test suite for Project model."""

    def test_project_valid_creation(self):
        """Test valid project creation."""
        project = Project(
            id="my-project-123", name="my-project-123", organization_id="my-org-456"
        )
        assert project.id == "my-project-123"
        assert project.organization_id == "my-org-456"

    def test_project_valid_id_lowercase(self):
        """Test project with lowercase alphanumeric ID."""
        project = Project(
            id="test-project", name="test-project", organization_id="my-org-456"
        )
        assert project.id == "test-project"
        assert project.organization_id == "my-org-456"

    def test_project_valid_id_with_numbers(self):
        """Test project with numbers in ID."""
        project = Project(
            id="project-123-abc", name="project-123-abc", organization_id="my-org-456"
        )
        assert project.id == "project-123-abc"
        assert project.organization_id == "my-org-456"

    def test_project_valid_id_with_hyphens(self):
        """Test project with hyphens in ID."""
        project = Project(
            id="my-test-project-name",
            name="my-test-project-name",
            organization_id="my-org-456",
        )
        assert project.id == "my-test-project-name"
        assert project.organization_id == "my-org-456"

    def test_project_valid_single_word_id(self):
        """Test project with single word ID."""
        project = Project(
            id="myproject", name="myproject", organization_id="my-org-456"
        )
        assert project.id == "myproject"
        assert project.organization_id == "my-org-456"

    def test_project_invalid_id_special_chars(self):
        """Test project creation fails with special characters in ID."""
        with pytest.raises(ValidationError):
            Project(id="my_project!", name="my_project!", organization_id="my-org-456")

    def test_project_invalid_id_spaces(self):
        """Test project creation fails with spaces in ID."""
        with pytest.raises(ValidationError):
            Project(id="my project", name="my project", organization_id="my-org-456")

    def test_project_invalid_id_uppercase_and_special(self):
        """Test project creation fails with uppercase and special chars."""
        with pytest.raises(ValidationError):
            Project(
                id="My-Project@123", name="My-Project@123", organization_id="my-org-456"
            )

    def test_project_missing_id(self):
        """Test project creation fails without ID."""
        with pytest.raises(ValidationError):
            Project(organization_id="my-org-456")

    def test_project_empty_id(self):
        """Test project creation fails with empty ID."""
        with pytest.raises(ValidationError):
            Project(id="", organization_id="my-org-456")

    def test_project_id_edge_case_numbers_only(self):
        """Test project with numeric-only ID."""
        project = Project(id="123456", name="123456", organization_id="my-org-456")
        assert project.id == "123456"
        assert project.organization_id == "my-org-456"

    def test_project_id_starts_with_hyphen(self):
        """Test project ID starting with hyphen."""
        project = Project(
            id="-my-project", name="-my-project", organization_id="my-org-456"
        )
        assert project.id == "-my-project"
        assert project.organization_id == "my-org-456"

    def test_project_id_ends_with_hyphen(self):
        """Test project ID ending with hyphen."""
        project = Project(
            id="my-project-", name="my-project-", organization_id="my-org-456"
        )
        assert project.id == "my-project-"
        assert project.organization_id == "my-org-456"

    def test_project_long_id(self):
        """Test project with long ID."""
        long_id = "a" * 30 + "-123"
        project = Project(id=long_id, name=long_id, organization_id="my-org-456")
        assert project.id == long_id
        assert project.organization_id == "my-org-456"

    def test_project_json_serialization(self):
        """Test project model JSON serialization."""
        project = Project(
            id="test-project", name="test-project", organization_id="my-org-456"
        )
        json_data = project.model_dump_json()
        assert "test-project" in json_data
        assert "my-org-456" in json_data

    def test_project_model_dump(self):
        """Test project model dump."""
        project = Project(
            id="test-project", name="test-project", organization_id="my-org-456"
        )
        data = project.model_dump()
        assert data["id"] == "test-project"
        assert data["organization_id"] == "my-org-456"
        assert len(data) == 3
