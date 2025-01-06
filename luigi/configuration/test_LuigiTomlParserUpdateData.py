# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonBigProjectTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=_update_data_15ecc0721f
ROOST_METHOD_SIG_HASH=_update_data_7cc237bafe


Scenario 1: Test when both data and new_data are not empty
Details:
  TestName: test_update_data_both_not_empty
  Description: This test is intended to verify if the function _update_data correctly merges the contents of new_data into data when both are not empty.
Execution:
  Arrange: Initialize data and new_data with different section-content pairs.
  Act: Call the function _update_data with data and new_data as parameters.
  Assert: Check if the returned dictionary contains all section-content pairs from both data and new_data, and that the content from new_data overwrites the same section's content in data.
Validation:
  This test ensures that the function correctly handles the most common use case, where both data and new_data have contents that need to be merged.

Scenario 2: Test when data is empty and new_data is not empty
Details:
  TestName: test_update_data_data_empty
  Description: This test is intended to verify if the function _update_data correctly returns new_data when data is empty.
Execution:
  Arrange: Initialize data as an empty dictionary and new_data with some section-content pairs.
  Act: Call the function _update_data with data and new_data as parameters.
  Assert: Check if the returned dictionary is the same as new_data.
Validation:
  This test ensures that the function correctly handles the case where data is empty and only new_data provides the section-content pairs.

Scenario 3: Test when new_data is empty and data is not empty
Details:
  TestName: test_update_data_new_data_empty
  Description: This test is intended to verify if the function _update_data correctly returns data when new_data is empty.
Execution:
  Arrange: Initialize new_data as an empty dictionary and data with some section-content pairs.
  Act: Call the function _update_data with data and new_data as parameters.
  Assert: Check if the returned dictionary is the same as data.
Validation:
  This test ensures that the function correctly handles the case where new_data is empty and only data provides the section-content pairs.

Scenario 4: Test when both data and new_data are empty
Details:
  TestName: test_update_data_both_empty
  Description: This test is intended to verify if the function _update_data correctly returns an empty dictionary when both data and new_data are empty.
Execution:
  Arrange: Initialize both data and new_data as empty dictionaries.
  Act: Call the function _update_data with data and new_data as parameters.
  Assert: Check if the returned dictionary is also an empty dictionary.
Validation:
  This test ensures that the function correctly handles the case where both data and new_data are empty.
"""

# ********RoostGPT********
import pytest
from configuration.toml_parser import LuigiTomlParser

class Test_LuigiTomlParserUpdateData:

    def test_update_data_both_not_empty(self):
        data = {"section1": {"key1": "value1"}, "section2": {"key2": "value2"}}
        new_data = {"section2": {"key2": "new_value2"}, "section3": {"key3": "value3"}}

        expected_output = {"section1": {"key1": "value1"}, "section2": {"key2": "new_value2"}, "section3": {"key3": "value3"}}

        output = LuigiTomlParser._update_data(data, new_data)
        assert output == expected_output, "Test failed when both data and new_data are not empty"

    def test_update_data_data_empty(self):
        data = {}
        new_data = {"section1": {"key1": "value1"}, "section2": {"key2": "value2"}}

        expected_output = new_data

        output = LuigiTomlParser._update_data(data, new_data)
        assert output == expected_output, "Test failed when data is empty and new_data is not empty"

    def test_update_data_new_data_empty(self):
        data = {"section1": {"key1": "value1"}, "section2": {"key2": "value2"}}
        new_data = {}

        expected_output = data

        output = LuigiTomlParser._update_data(data, new_data)
        assert output == expected_output, "Test failed when new_data is empty and data is not empty"

    def test_update_data_both_empty(self):
        data = {}
        new_data = {}

        expected_output = {}

        output = LuigiTomlParser._update_data(data, new_data)
        assert output == expected_output, "Test failed when both data and new_data are empty"
