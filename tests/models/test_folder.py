"""Test Folder Model."""

import pytest
from pydantic import ValidationError

from gcp.domain.models.folder import Folder


@pytest.mark.unit
class TestFolder:
    """Test suite for Folder model."""

    def test_folder_valid_creation(self):
        """Test valid folder creation."""
        folder = Folder(id="my-folder-123", name="my folder")
        assert folder.id == "my-folder-123"
        assert folder.name == "my folder"

    def test_folder_valid_id_lowercase(self):
        """Test folder with lowercase ID."""
        folder = Folder(id="test-folder", name="test folder")
        assert folder.id == "test-folder"

    def test_folder_valid_id_with_numbers(self):
        """Test folder with numbers in ID."""
        folder = Folder(id="folder-123-abc", name="folder with numbers 123")
        assert folder.id == "folder-123-abc"

    def test_folder_valid_id_with_hyphens(self):
        """Test folder with hyphens in ID."""
        folder = Folder(id="my-test-folder-name", name="folder-with-hyphens")
        assert folder.id == "my-test-folder-name"

    def test_folder_valid_id_with_underscores(self):
        """Test folder with underscores in ID."""
        folder = Folder(id="my-folder-name", name="folder_with_underscores")
        assert folder.id == "my-folder-name"

    def test_folder_valid_id_with_spaces(self):
        """Test folder with spaces in ID."""
        folder = Folder(id="my-folder-name", name="folder with spaces")
        assert folder.id == "my-folder-name"

    def test_folder_valid_id_mixed_separators(self):
        """Test folder with mixed separators (hyphens, underscores, spaces)."""
        folder = Folder(id="my-folder-name", name="my-folder_name test")
        assert folder.id == "my-folder-name"

    def test_folder_valid_single_word_id(self):
        """Test folder with single word ID."""
        folder = Folder(id="folder", name="my folder")
        assert folder.id == "folder"

    def test_folder_invalid_id_uppercase(self):
        """Test folder creation fails with uppercase in ID."""
        with pytest.raises(ValidationError) as exc_info:
            Folder(id="MyFolder", name="my folder")
        assert "string should match pattern" in str(exc_info.value).lower()

    def test_folder_invalid_id_special_chars(self):
        """Test folder creation fails with special characters in ID."""
        with pytest.raises(ValidationError):
            Folder(id="my_folder!", name="my folder")

    def test_folder_invalid_id_at_symbol(self):
        """Test folder creation fails with @ symbol in ID."""
        with pytest.raises(ValidationError):
            Folder(id="my@folder", name="my folder")

    def test_folder_invalid_id_hash_symbol(self):
        """Test folder creation fails with # symbol in ID."""
        with pytest.raises(ValidationError):
            Folder(id="my#folder", name="my folder")

    def test_folder_invalid_id_period(self):
        """Test folder creation fails with period in ID."""
        with pytest.raises(ValidationError):
            Folder(id="my.folder", name="my folder")

    def test_folder_invalid_id_uppercase_and_special(self):
        """Test folder creation fails with uppercase and special chars."""
        with pytest.raises(ValidationError):
            Folder(id="My-Folder@123", name="my folder")

    def test_folder_missing_id(self):
        """Test folder creation fails without ID."""
        with pytest.raises(ValidationError):
            Folder(name="my folder")

    def test_folder_missing_name(self):
        """Test folder creation fails without name."""
        with pytest.raises(ValidationError):
            Folder(id="my-folder")

    def test_folder_empty_id(self):
        """Test folder creation fails with empty ID."""
        with pytest.raises(ValidationError):
            Folder(id="", name="my folder")

    def test_folder_empty_name(self):
        """Test folder creation with empty name."""
        with pytest.raises(ValidationError):
            folder = Folder(id="my-folder", name="")

    def test_folder_name_with_valid_chars(self):
        """Test folder name supports spaces, underscores, and hyphens."""
        folder = Folder(id="my-folder", name="my folder_name-prod 1")
        assert folder.name == "my folder_name-prod 1"

    def test_folder_name_invalid_uppercase(self):
        """Test folder name rejects uppercase characters."""
        with pytest.raises(ValidationError):
            Folder(id="my-folder", name="My Folder")

    def test_folder_name_invalid_special_chars(self):
        """Test folder name rejects special characters outside the regex."""
        with pytest.raises(ValidationError):
            Folder(id="my-folder", name="my folder@prod")

    def test_folder_id_edge_case_numbers_only(self):
        """Test folder with numeric-only ID."""
        folder = Folder(id="123456", name="numeric folder")
        assert folder.id == "123456"

    def test_folder_id_edge_case_spaces_only(self):
        """Test folder with spaces-only ID fails."""
        with pytest.raises(ValidationError):
            Folder(id="   ", name="spaces only")

    def test_folder_id_edge_case_underscores_only(self):
        """Test folder with underscores-only ID fails."""
        with pytest.raises(ValidationError):
            Folder(id="___", name="underscores only")

    def test_folder_id_edge_case_hyphens_only(self):
        """Test folder with hyphens-only ID."""
        folder = Folder(id="---", name="hyphens only")
        assert folder.id == "---"

    def test_folder_id_starts_with_space(self):
        """Test folder ID starting with space fails."""
        with pytest.raises(ValidationError):
            Folder(id=" my-folder", name="folder")

    def test_folder_id_ends_with_space(self):
        """Test folder ID ending with space fails."""
        with pytest.raises(ValidationError):
            Folder(id="my-folder ", name="folder")

    def test_folder_id_starts_with_underscore(self):
        """Test folder ID starting with underscore fails."""
        with pytest.raises(ValidationError):
            Folder(id="_my_folder", name="folder")

    def test_folder_id_starts_with_hyphen(self):
        """Test folder ID starting with hyphen."""
        folder = Folder(id="-my-folder", name="folder")
        assert folder.id == "-my-folder"

    def test_folder_long_id(self):
        """Test folder with long ID."""
        long_id = "a" * 30 + "-123"
        folder = Folder(id=long_id, name="long id folder")
        assert folder.id == long_id

    def test_folder_json_serialization(self):
        """Test folder model JSON serialization."""
        folder = Folder(id="test-folder", name="test folder")
        json_data = folder.model_dump_json()
        assert "test-folder" in json_data
        assert "test folder" in json_data

    def test_folder_model_dump(self):
        """Test folder model dump."""
        folder = Folder(id="test-folder", name="test folder")
        data = folder.model_dump()
        assert data["id"] == "test-folder"
        assert data["name"] == "test folder"
        assert len(data) == 2

    def test_folder_camel_case_serialization(self):
        """Test folder model inherits CamelCase behavior."""
        folder = Folder(id="test-folder", name="test folder")
        data = folder.model_dump(by_alias=True)
        assert "id" in data
        assert "name" in data
