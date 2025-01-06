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
  Arrange: Set a valid parser in the environment variable LUIGI_CONFIG_PARSER.
  Act: Call the function get_config with the valid parser name.
  Assert: Check if the returned object is an instance of the corresponding parser class.
Validation:
  This test ensures that the get_config function correctly identifies and returns the requested parser instance. This is crucial for the correct interpretation and processing of configuration files.

Scenario 2: No Parser Passed
Details:
  TestName: test_get_config_with_no_parser
  Description: This test verifies that the get_config function works as expected when no parser is passed.
Execution:
  Arrange: Set a valid parser in the environment variable LUIGI_CONFIG_PARSER.
  Act: Call the function get_config without a parser name.
  Assert: Check if the returned object is an instance of the default parser class.
Validation:
  This test ensures that the get_config function correctly identifies and returns the default parser instance when no specific parser is requested. This is important for maintaining the function's robustness and flexibility.

Scenario 3: Invalid Parser Passed
Details:
  TestName: test_get_config_with_invalid_parser
  Description: This test verifies that the get_config function correctly handles an invalid parser name.
Execution:
  Arrange: Set an invalid parser in the environment variable LUIGI_CONFIG_PARSER.
  Act: Call the function get_config with the invalid parser name.
  Assert: Check if a warning is issued and the returned object is an instance of the default parser class.
Validation:
  This test verifies that the get_config function correctly handles invalid input, issuing a warning and defaulting to the default parser. This is crucial for the function's robustness and error handling capabilities.

Scenario 4: Parser Not Installed
Details:
  TestName: test_get_config_with_uninstalled_parser
  Description: This test verifies that the get_config function correctly handles the case where the requested parser is not installed.
Execution:
  Arrange: Set a parser name in the environment variable LUIGI_CONFIG_PARSER for a parser that is not installed.
  Act: Call the function get_config with the uninstalled parser name.
  Assert: Check if an ImportError is raised with the correct error message.
Validation:
  This test ensures that the get_config function correctly identifies when a requested parser is not installed and raises a helpful error message. This is important for user-friendly error handling.
"""

# ********RoostGPT********
import os
import warnings
import pytest
from unittest.mock import patch
from configuration.core import get_config
from cfg_parser import LuigiConfigParser
from toml_parser import LuigiTomlParser

class Test_CoreGetConfig:

    @pytest.mark.regression
    def test_get_config_with_valid_parser(self):
        with patch.dict(os.environ, {'LUIGI_CONFIG_PARSER': 'toml'}):
            result = get_config('toml')
            assert isinstance(result, LuigiTomlParser)

    @pytest.mark.smoke
    def test_get_config_with_no_parser(self):
        with patch.dict(os.environ, {'LUIGI_CONFIG_PARSER': 'cfg'}):
            result = get_config()
            assert isinstance(result, LuigiConfigParser)

    @pytest.mark.negative
    def test_get_config_with_invalid_parser(self):
        with patch.dict(os.environ, {'LUIGI_CONFIG_PARSER': 'invalid_parser'}):
            with pytest.warns(UserWarning) as record:
                result = get_config('invalid_parser')
                assert isinstance(result, LuigiConfigParser)
            assert len(record) == 1
            assert str(record[0].message) == "Invalid parser: cfg"

    @pytest.mark.negative
    def test_get_config_with_uninstalled_parser(self):
        with patch.dict(os.environ, {'LUIGI_CONFIG_PARSER': 'uninstalled_parser'}):
            with pytest.raises(ImportError) as excinfo:
                get_config('uninstalled_parser')
            assert "Parser not installed yet. Please, install luigi with required parser:\npip install luigi[uninstalled_parser]" in str(excinfo.value)
