# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=_get_default_parser_da6898e1c5
ROOST_METHOD_SIG_HASH=_get_default_parser_61b2c6fc97


Scenario 1: Test with LUIGI_CONFIG_PARSER in Environment Variables
Details:
  TestName: test_default_parser_with_env_var
  Description: This test is intended to verify that the function correctly retrieves the parser from the environment variables.
Execution:
  Arrange: Set the 'LUIGI_CONFIG_PARSER' in environment variables to a valid parser.
  Act: Call the _get_default_parser() function.
  Assert: Confirm that the function returns the parser set in the environment variables.
Validation:
  This test is important to ensure that the function can correctly retrieve and return the parser from environment variables, which is a key part of its functionality.

Scenario 2: Test with Invalid LUIGI_CONFIG_PARSER in Environment Variables
Details:
  TestName: test_default_parser_with_invalid_env_var
  Description: This test is intended to verify that the function correctly handles an invalid parser in the environment variables and defaults to DEFAULT_PARSER.
Execution:
  Arrange: Set the 'LUIGI_CONFIG_PARSER' in environment variables to an invalid parser.
  Act: Call the _get_default_parser() function.
  Assert: Confirm that the function returns the DEFAULT_PARSER and logs a warning.
Validation:
  This test is crucial to ensure that the function can handle invalid inputs from the environment variables gracefully and fall back to the DEFAULT_PARSER.

Scenario 3: Test without LUIGI_CONFIG_PARSER in Environment Variables
Details:
  TestName: test_default_parser_without_env_var
  Description: This test is intended to verify that the function correctly defaults to DEFAULT_PARSER when 'LUIGI_CONFIG_PARSER' is not set in the environment variables.
Execution:
  Arrange: Ensure that 'LUIGI_CONFIG_PARSER' is not set in the environment variables.
  Act: Call the _get_default_parser() function.
  Assert: Confirm that the function returns the DEFAULT_PARSER.
Validation:
  This test is important to ensure that the function can correctly default to the DEFAULT_PARSER when 'LUIGI_CONFIG_PARSER' is not set in the environment variables. This is a common scenario and the function should handle it correctly. 

Scenario 4: Test with LUIGI_CONFIG_PARSER and DEFAULT_PARSER Both Invalid
Details:
  TestName: test_default_parser_with_both_invalid
  Description: This test is intended to verify that the function correctly handles a situation where both 'LUIGI_CONFIG_PARSER' and DEFAULT_PARSER are invalid.
Execution:
  Arrange: Set 'LUIGI_CONFIG_PARSER' and DEFAULT_PARSER to invalid values.
  Act: Call the _get_default_parser() function.
  Assert: Confirm that the function raises an appropriate error or logs a warning.
Validation:
  This test is important to ensure the function can handle edge cases where both the 'LUIGI_CONFIG_PARSER' and DEFAULT_PARSER are invalid. It should fail gracefully in such a scenario.
"""

# ********RoostGPT********
import os
import warnings
import pytest
from unittest.mock import patch
from configuration.core import _get_default_parser

class Test_CoreGetDefaultParser:

    @pytest.mark.regression
    def test_default_parser_with_env_var(self):
        os.environ['LUIGI_CONFIG_PARSER'] = 'toml'
        assert _get_default_parser() == 'toml'
        del os.environ['LUIGI_CONFIG_PARSER']

    @pytest.mark.negative
    def test_default_parser_with_invalid_env_var(self):
        os.environ['LUIGI_CONFIG_PARSER'] = 'invalid'
        with pytest.warns(UserWarning, match="Invalid parser: cfg"):
            assert _get_default_parser() == 'cfg'
        del os.environ['LUIGI_CONFIG_PARSER']

    @pytest.mark.smoke
    def test_default_parser_without_env_var(self):
        if 'LUIGI_CONFIG_PARSER' in os.environ:
            del os.environ['LUIGI_CONFIG_PARSER']
        assert _get_default_parser() == 'cfg'

    @pytest.mark.negative
    def test_default_parser_with_both_invalid(self):
        os.environ['LUIGI_CONFIG_PARSER'] = 'invalid'
        with patch.dict('configuration.core.PARSERS', {'cfg': None}, clear=True):
            with pytest.warns(UserWarning, match="Invalid parser: cfg"):
                assert _get_default_parser() == 'cfg'
        del os.environ['LUIGI_CONFIG_PARSER']
