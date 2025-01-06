# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=has_option_05c7ef0949
ROOST_METHOD_SIG_HASH=has_option_f14ac78887


Scenario 1: Validate has_option with existing section and option
Details:
  TestName: test_has_option_existing_section_option
  Description: This test is intended to verify if the has_option function correctly identifies an existing section and option.
Execution:
  Arrange: Initialize the ConfigParser object and set a section and an option in it.
  Act: Call the has_option function with the existing section and option.
  Assert: Validate that the function returns True.
Validation:
  This test validates the core functionality of the has_option function. If it fails, the function cannot correctly identify existing sections and options.

Scenario 2: Validate has_option with non-existing section
Details:
  TestName: test_has_option_non_existing_section
  Description: This test is intended to verify if the has_option function correctly handles non-existing sections.
Execution:
  Arrange: Initialize the ConfigParser object and set a section and an option in it.
  Act: Call the has_option function with a non-existing section and an existing option.
  Assert: Validate that the function returns False.
Validation:
  This test validates the function's error handling capabilities. If it fails, the function may not correctly handle non-existing sections, leading to incorrect results.

Scenario 3: Validate has_option with non-existing option
Details:
  TestName: test_has_option_non_existing_option
  Description: This test is intended to verify if the has_option function correctly handles non-existing options.
Execution:
  Arrange: Initialize the ConfigParser object and set a section and an option in it.
  Act: Call the has_option function with an existing section and a non-existing option.
  Assert: Validate that the function returns False.
Validation:
  This test also validates the function's error handling capabilities. If it fails, the function may not correctly handle non-existing options, leading to incorrect results.

Scenario 4: Validate has_option with option containing dashes
Details:
  TestName: test_has_option_option_with_dashes
  Description: This test is intended to verify if the has_option function correctly handles options with dashes and issues a deprecation warning.
Execution:
  Arrange: Initialize the ConfigParser object and set a section and an option with dashes in it.
  Act: Call the has_option function with the existing section and option with dashes.
  Assert: Validate that the function returns True and issues a deprecation warning.
Validation:
  This test validates the function's ability to handle deprecated naming conventions. If it fails, the function may not correctly handle options with dashes or may not issue the appropriate warnings.

"""

# ********RoostGPT********
import os
import re
import warnings
from configparser import ConfigParser, NoOptionError, NoSectionError, InterpolationError
from configparser import Interpolation, BasicInterpolation
from base_parser import BaseParser
from configuration.cfg_parser import LuigiConfigParser
import pytest

class Test_LuigiConfigParserHasOption:

    @pytest.mark.regression
    def test_has_option_existing_section_option(self):
        # Arrange
        config = ConfigParser()
        config.add_section("TestSection")
        config.set("TestSection", "TestOption", "TestValue")
        luigiConfig = LuigiConfigParser(config)

        # Act
        result = luigiConfig.has_option("TestSection", "TestOption")

        # Assert
        assert result is True

    @pytest.mark.negative
    def test_has_option_non_existing_section(self):
        # Arrange
        config = ConfigParser()
        config.add_section("TestSection")
        config.set("TestSection", "TestOption", "TestValue")
        luigiConfig = LuigiConfigParser(config)

        # Act
        result = luigiConfig.has_option("NonExistingSection", "TestOption")

        # Assert
        assert result is False

    @pytest.mark.negative
    def test_has_option_non_existing_option(self):
        # Arrange
        config = ConfigParser()
        config.add_section("TestSection")
        config.set("TestSection", "TestOption", "TestValue")
        luigiConfig = LuigiConfigParser(config)

        # Act
        result = luigiConfig.has_option("TestSection", "NonExistingOption")

        # Assert
        assert result is False

    @pytest.mark.regression
    def test_has_option_option_with_dashes(self):
        # Arrange
        config = ConfigParser()
        config.add_section("TestSection")
        config.set("TestSection", "Test-Option", "TestValue")
        luigiConfig = LuigiConfigParser(config)

        # Act
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = luigiConfig.has_option("TestSection", "Test-Option")

        # Assert
        assert result is True
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "should be avoided" in str(w[-1].message)
