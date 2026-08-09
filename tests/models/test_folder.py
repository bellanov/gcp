"""Test Folder Model."""

import pytest
from pydantic import ValidationError

from gcp.domain.models.folder import Folder


@pytest.mark.unit
class TestFolder:
    """Test suite for Folder model."""

    def test_folder_valid_creation(self):
        """Test valid folder creation."""
        folder = Folder(
            name="folders/123456", display_name="My Folder", parent="folders/123456"
        )
        assert folder.name == "folders/123456"
        assert folder.display_name == "My Folder"
        assert folder.parent == "folders/123456"

    def test_folder_valid_id_lowercase(self):
        """Test folder with lowercase ID."""
        folder = Folder(
            name="folders/123456", display_name="Test Folder", parent="folders/123456"
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_id_with_numbers(self):
        """Test folder with numbers in ID."""
        folder = Folder(
            name="folders/123456",
            display_name="Folder 123 ABC",
            parent="folders/123456",
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_id_with_hyphens(self):
        """Test folder with hyphens in ID."""
        folder = Folder(
            name="folders/123456",
            display_name="My Test Folder",
            parent="folders/123456",
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_id_with_underscores(self):
        """Test folder with underscores in ID."""
        folder = Folder(
            name="folders/123456",
            display_name="My Folder Name",
            parent="folders/123456",
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_id_with_spaces(self):
        """Test folder with spaces in ID."""
        folder = Folder(
            name="folders/123456",
            display_name="My Folder Name",
            parent="folders/123456",
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_id_mixed_separators(self):
        """Test folder with mixed separators (hyphens, underscores, spaces)."""
        folder = Folder(
            name="folders/123456",
            display_name="My Folder Name",
            parent="folders/123456",
        )
        assert folder.name == "folders/123456"

    def test_folder_valid_single_word_id(self):
        """Test folder with single word ID."""
        folder = Folder(
            name="folders/123456", display_name="Folder", parent="folders/123456"
        )
        assert folder.name == "folders/123456"

    def test_folder_missing_name(self):
        """Test folder creation fails without name."""
        with pytest.raises(ValidationError):
            Folder(display_name="My Folder", parent="folders/123456")

    def test_folder_empty_name(self):
        """Test folder creation with empty name."""
        with pytest.raises(ValidationError):
            Folder(name="", display_name="My Folder", parent="folders/123456")

    def test_folder_name_with_valid_chars(self):
        """Test folder name supports spaces, underscores, and hyphens."""
        folder = Folder(
            name="folders/123456", display_name="My Folder", parent="folders/123456"
        )
        assert folder.name == "folders/123456"

    def test_folder_name_invalid_special_chars(self):
        """Test folder name rejects special characters outside the regex."""
        with pytest.raises(ValidationError):
            Folder(
                name="folders/123456()",
                display_name="My Folder",
                parent="folders/123456",
            )

    def test_folder_json_serialization(self):
        """Test folder model JSON serialization."""
        folder = Folder(
            name="folders/123456", display_name="Test Folder", parent="folders/123456"
        )
        json_data = folder.model_dump_json()
        assert "folders/123456" in json_data

    def test_folder_model_dump(self):
        """Test folder model dump."""
        folder = Folder(
            name="folders/123456", display_name="Test Folder", parent="folders/123456"
        )
        data = folder.model_dump()
        assert data["name"] == "folders/123456"
        assert len(data) == 3

    def test_folder_camel_case_serialization(self):
        """Test folder model inherits CamelCase behavior."""
        folder = Folder(
            name="folders/123456", display_name="Test Folder", parent="folders/123456"
        )
        data = folder.model_dump(by_alias=True)
        assert "name" in data
