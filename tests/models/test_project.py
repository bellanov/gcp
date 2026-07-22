"""Test Project Model."""

import pytest
from pydantic import ValidationError

from gcp.domain.models.project import Project


@pytest.mark.unit
class TestProject:
    """Test suite for Project model."""

    def test_project_valid_creation(self):
        """Test valid project creation."""
        project = Project(id="my-project-123")
        assert project.id == "my-project-123"

    def test_project_valid_id_lowercase(self):
        """Test project with lowercase alphanumeric ID."""
        project = Project(id="test-project")
        assert project.id == "test-project"

    def test_project_valid_id_with_numbers(self):
        """Test project with numbers in ID."""
        project = Project(id="project-123-abc")
        assert project.id == "project-123-abc"

    def test_project_valid_id_with_hyphens(self):
        """Test project with hyphens in ID."""
        project = Project(id="my-test-project-name")
        assert project.id == "my-test-project-name"

    def test_project_valid_single_word_id(self):
        """Test project with single word ID."""
        project = Project(id="myproject")
        assert project.id == "myproject"

    def test_project_invalid_id_uppercase(self):
        """Test project creation fails with uppercase in ID."""
        with pytest.raises(ValidationError) as exc_info:
            Project(id="MyProject")
        assert "string should match pattern" in str(exc_info.value).lower()

    def test_project_invalid_id_special_chars(self):
        """Test project creation fails with special characters in ID."""
        with pytest.raises(ValidationError):
            Project(id="my_project!")

    def test_project_invalid_id_spaces(self):
        """Test project creation fails with spaces in ID."""
        with pytest.raises(ValidationError):
            Project(id="my project")

    def test_project_invalid_id_uppercase_and_special(self):
        """Test project creation fails with uppercase and special chars."""
        with pytest.raises(ValidationError):
            Project(id="My-Project@123")

    def test_project_missing_id(self):
        """Test project creation fails without ID."""
        with pytest.raises(ValidationError):
            Project()

    def test_project_empty_id(self):
        """Test project creation fails with empty ID."""
        with pytest.raises(ValidationError):
            Project(id="")

    def test_project_id_edge_case_numbers_only(self):
        """Test project with numeric-only ID."""
        project = Project(id="123456")
        assert project.id == "123456"

    def test_project_id_starts_with_hyphen(self):
        """Test project ID starting with hyphen."""
        project = Project(id="-my-project")
        assert project.id == "-my-project"

    def test_project_id_ends_with_hyphen(self):
        """Test project ID ending with hyphen."""
        project = Project(id="my-project-")
        assert project.id == "my-project-"

    def test_project_long_id(self):
        """Test project with long ID."""
        long_id = "a" * 30 + "-123"
        project = Project(id=long_id)
        assert project.id == long_id

    def test_project_json_serialization(self):
        """Test project model JSON serialization."""
        project = Project(id="test-project")
        json_data = project.model_dump_json()
        assert "test-project" in json_data

    def test_project_model_dump(self):
        """Test project model dump."""
        project = Project(id="test-project")
        data = project.model_dump()
        assert data["id"] == "test-project"
        assert len(data) == 1
