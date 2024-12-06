# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=get_config_133e2e1291
ROOST_METHOD_SIG_HASH=get_config_8a95b2590c


Scenario 1: Valid Parser Passed
Details:
  TestName: test_get_config_with_valid_parser
  Description: This test verifies that the get_config function works as expected when a valid parser name is passed.
Execution:
  Arrange: Prepare a valid parser name that exists in the PARSERS dictionary.
  Act: Call the get_config function with the prepared parser name.
  Assert: Check if the returned object is an instance of the corresponding parser class.
Validation:
  This test ensures that the get_config function correctly instantiates the required parser when a valid parser name is passed. This is crucial as it validates the function's ability to provide the correct configuration parser, which is essential for the application's operation.

Scenario 2: Invalid Parser Passed
Details:
  TestName: test_get_config_with_invalid_parser
  Description: This test verifies that the get_config function raises a warning when an invalid parser name is passed.
Execution:
  Arrange: Prepare an invalid parser name that does not exist in the PARSERS dictionary.
  Act: Call the get_config function with the invalid parser name.
  Assert: Check if a warning is raised.
Validation:
  This test ensures that the get_config function correctly identifies and warns about an invalid parser. This is important for avoiding silent failures and providing feedback about incorrect configurations.

Scenario 3: No Parser Passed
Details:
  TestName: test_get_config_with_no_parser
  Description: This test verifies that the get_config function uses the default parser when no parser is passed.
Execution:
  Arrange: No preparation needed.
  Act: Call the get_config function with no parameters.
  Assert: Check if the returned object is an instance of the default parser class.
Validation:
  This test ensures that the get_config function correctly defaults to the default parser when no parser is specified. This is crucial for maintaining default functionality and ensuring the function behaves as expected in the absence of explicit parameters.

Scenario 4: Disabled Parser Passed
Details:
  TestName: test_get_config_with_disabled_parser
  Description: This test verifies that the get_config function raises an ImportError when a disabled parser name is passed.
Execution:
  Arrange: Prepare a disabled parser name that exists in the PARSERS dictionary but is not enabled.
  Act: Call the get_config function with the disabled parser name.
  Assert: Check if an ImportError is raised.
Validation:
  This test ensures that the get_config function correctly identifies and raises an error for a disabled parser. This is important for preventing the use of parsers that are not ready or suitable for use, thus ensuring the integrity and correctness of the function's operation.
"""

# ********RoostGPT********
import logging
import os
import warnings
import pytest
from cfg_parser import LuigiConfigParser
from toml_parser import LuigiTomlParser
from configuration.core import get_config

class Test_CoreGetConfig:
    def test_get_config_with_valid_parser(self):
        # Arrange
        valid_parser = 'cfg'
        
        # Act
        config = get_config(valid_parser)
        
        # Assert
        assert isinstance(config, LuigiConfigParser), "The returned object is not an instance of the corresponding parser class"

    def test_get_config_with_invalid_parser(self):
        # Arrange
        invalid_parser = 'invalid_parser'
        
        # Act and Assert
        with pytest.warns(UserWarning, match=r"Invalid parser: .*"):
            get_config(invalid_parser)
            
    def test_get_config_with_no_parser(self):
        # Act
        config = get_config()
        
        # Assert
        assert isinstance(config, LuigiConfigParser), "The returned object is not an instance of the default parser class"

    def test_get_config_with_disabled_parser(self):
        # Arrange
        disabled_parser = 'disabled_parser'
        
        # Act and Assert
        with pytest.raises(ImportError, match=r"Parser not installed yet. .*"):
            get_config(disabled_parser)
