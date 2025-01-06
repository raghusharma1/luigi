# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=_get_with_default_aeb85b75c1
ROOST_METHOD_SIG_HASH=_get_with_default_19a36c0a1b


Scenario 1: Test the method with valid section and option
Details:
  TestName: test_get_with_default_valid_section_option
  Description: This test is intended to verify that the method correctly retrieves the value of a valid section/option, and does not raise any exceptions.
Execution:
  Arrange: Initialize a ConfigParser object with a sample configuration containing a valid section and option.
  Act: Invoke the _get_with_default method with the valid section and option.
  Assert: Verify that the method returns the correct value for the given section/option.
Validation:
  Rationalize: It's important to ensure that the method correctly retrieves values from the configuration, as this is its primary function.

Scenario 2: Test the method with invalid section and option
Details:
  TestName: test_get_with_default_invalid_section_option
  Description: This test is intended to verify that the method correctly handles a situation where an invalid section/option is requested.
Execution:
  Arrange: Initialize a ConfigParser object with a sample configuration.
  Act: Invoke the _get_with_default method with an invalid section and option.
  Assert: Verify that the method returns the default value provided in the parameters.
Validation:
  Rationalize: It's crucial to ensure that the method can gracefully handle invalid sections/options and return a default value when necessary.

Scenario 3: Test the method with a default value that doesn't match the expected type
Details:
  TestName: test_get_with_default_default_value_type_mismatch
  Description: This test is intended to verify that the method raises an exception if the default value provided does not match the expected type.
Execution:
  Arrange: Initialize a ConfigParser object with a sample configuration.
  Act: Invoke the _get_with_default method with a default value that does not match the expected type.
  Assert: Verify that the method raises an exception.
Validation:
  Rationalize: Ensuring that the method raises an exception when the default value doesn't match the expected type is important for maintaining type consistency.

Scenario 4: Test the method with dash-style option names
Details:
  TestName: test_get_with_default_dash_option
  Description: This test is intended to verify that the method can handle dash-style option names, but raises a DeprecationWarning.
Execution:
  Arrange: Initialize a ConfigParser object with a sample configuration containing a dash-style option name.
  Act: Invoke the _get_with_default method with the dash-style option name.
  Assert: Verify that the method returns the correct value and raises a DeprecationWarning.
Validation:
  Rationalize: It's important to ensure that the method can handle dash-style option names for backwards compatibility, but correctly warns the user about deprecation.
"""

# ********RoostGPT********
import os
import re
import warnings
import pytest
from configparser import ConfigParser, NoOptionError, NoSectionError, InterpolationError
from configparser import Interpolation, BasicInterpolation
from base_parser import BaseParser
from configuration.cfg_parser import LuigiConfigParser

class Test_LuigiConfigParserGetWithDefault:

    @pytest.mark.regression
    def test_get_with_default_valid_section_option(self):
        config = ConfigParser()
        config.add_section('test_section')
        config.set('test_section', 'test_option', 'test_value')
        parser = LuigiConfigParser(config)

        assert parser._get_with_default(config.get, 'test_section', 'test_option', None) == 'test_value'

    @pytest.mark.regression
    def test_get_with_default_invalid_section_option(self):
        config = ConfigParser()
        parser = LuigiConfigParser(config)

        assert parser._get_with_default(config.get, 'invalid_section', 'invalid_option', 'default_value') == 'default_value'

    @pytest.mark.negative
    def test_get_with_default_default_value_type_mismatch(self):
        config = ConfigParser()
        parser = LuigiConfigParser(config)

        with pytest.raises(TypeError):
            parser._get_with_default(config.get, 'test_section', 'test_option', 'default_value', expected_type=int)

    @pytest.mark.regression
    def test_get_with_default_dash_option(self):
        config = ConfigParser()
        config.add_section('test_section')
        config.set('test_section', 'test-option', 'test_value')
        parser = LuigiConfigParser(config)

        with pytest.warns(DeprecationWarning):
            assert parser._get_with_default(config.get, 'test_section', 'test-option', None) == 'test_value'
