# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=add_config_path_388d3ffdb1
ROOST_METHOD_SIG_HASH=add_config_path_05e54720ac


Scenario 1: Verify the addition of a new config path.
Details:
  TestName: test_add_config_path
  Description: This test verifies if a new path can be added successfully to the config paths. 
Execution:
  Arrange: Initialize an instance of the class with a known set of config paths.
  Act: Call the add_config_path method with a new, unique path.
  Assert: Check if the new path is added to the list of config paths and the reload method is called.
Validation:
  The test ensures that the method can successfully add a new path to the config paths. This is crucial for the function's ability to manage multiple configurations.

Scenario 2: Verify the addition of an existing config path.
Details:
  TestName: test_add_existing_config_path
  Description: This test validates the behavior of the function when an existing path is added to the config paths.
Execution:
  Arrange: Initialize an instance of the class with a known set of config paths.
  Act: Call the add_config_path method with a path that already exists in the config paths.
  Assert: Check if the path is not duplicated in the list of config paths and the reload method is called.
Validation:
  The test checks if the function can handle the addition of an existing path without creating duplicates, maintaining the integrity of the config paths.

Scenario 3: Verify the addition of a null config path.
Details:
  TestName: test_add_null_config_path
  Description: This test examines the function's behavior when a null or empty path is added.
Execution:
  Arrange: Initialize an instance of the class with a known set of config paths.
  Act: Call the add_config_path method with a null or empty path.
  Assert: Check if the null or empty path is not added to the list of config paths and the reload method is not called.
Validation:
  This test is important to ensure that the function can handle invalid inputs gracefully without causing unexpected behavior.

Scenario 4: Verify the addition of a config path when reload fails.
Details:
  TestName: test_add_config_path_reload_fail
  Description: This test checks the function's behavior when the reload method fails after adding a new path.
Execution:
  Arrange: Initialize an instance of the class with a known set of config paths. Mock the reload method to throw an exception.
  Act: Call the add_config_path method with a new, unique path.
  Assert: Check if the new path is added to the list of config paths and an appropriate error is logged when the reload method fails.
Validation:
  This test ensures that the function can handle failures in the reload method gracefully and log appropriate errors.
"""

# ********RoostGPT********
import logging
import pytest
from unittest.mock import patch, MagicMock
from configuration.base_parser import BaseParser

class Test_BaseParserAddConfigPath:
    @pytest.mark.valid
    def test_add_config_path(self):
        # Arrange
        base_parser = BaseParser()
        base_parser._config_paths = ['path1', 'path2']
        new_path = 'path3'

        # Act
        base_parser.add_config_path(new_path)

        # Assert
        assert new_path in base_parser._config_paths
        assert base_parser.reload.called

    @pytest.mark.valid
    def test_add_existing_config_path(self):
        # Arrange
        base_parser = BaseParser()
        base_parser._config_paths = ['path1', 'path2']
        existing_path = 'path1'

        # Act
        base_parser.add_config_path(existing_path)

        # Assert
        assert base_parser._config_paths.count(existing_path) == 1
        assert base_parser.reload.called

    @pytest.mark.invalid
    def test_add_null_config_path(self):
        # Arrange
        base_parser = BaseParser()
        base_parser._config_paths = ['path1', 'path2']
        null_path = ''

        # Act
        base_parser.add_config_path(null_path)

        # Assert
        assert null_path not in base_parser._config_paths
        assert not base_parser.reload.called

    @pytest.mark.negative
    def test_add_config_path_reload_fail(self):
        # Arrange
        base_parser = BaseParser()
        base_parser._config_paths = ['path1', 'path2']
        new_path = 'path3'
        base_parser.reload = MagicMock(side_effect=Exception('Reload failed'))

        # Act
        with pytest.raises(Exception) as excinfo:
            base_parser.add_config_path(new_path)
        
        # Assert
        assert new_path in base_parser._config_paths
        assert 'Reload failed' in str(excinfo.value)
        assert base_parser.reload.called
