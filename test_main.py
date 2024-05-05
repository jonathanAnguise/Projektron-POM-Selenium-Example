"""
Module: test_main
Author: Jonathan

This module contains unit tests for the main module 'main.py'.
It tests the functionality of the functions defined in 'main.py'.

Dependencies:
    - unittest
    - main (the module under test)

Usage:
    This module can be executed directly to run all unit tests:
        $ python test_main.py
"""

import unittest

from main import parse_time_string, validate_resting_budget_is_enough


class TestParseTimeString(unittest.TestCase):
    """
    Test cases for the parse_time_string function.
    """

    def test_parse_time_string(self):
        """
        Test cases for the parse_time_string function.
        """
        # Test parsing time string without days
        self.assertEqual(
            parse_time_string("04:00h"), 14400
        )  # 4 hours in seconds
        # Test parsing time string with days and hours
        self.assertEqual(
            parse_time_string("2d 04:00h"), 187200
        )  # 2 days and 4 hours in seconds


class TestValidateRestingBudgetIsEnough(unittest.TestCase):
    """
    Test cases for the validate_resting_budget_is_enough function.
    """

    def test_validate_resting_budget_is_enough(self):
        """
        Test cases for the validate_resting_budget_is_enough function.
        """
        budget = 180000  # 2 days and 4 hours in seconds
        duration = 172800  # 2 days in seconds
        unrec = 7200  # 2 hours in seconds
        # Test with enough resting budget
        self.assertTrue(
            validate_resting_budget_is_enough(unrec, duration, budget)
        )
        # Test with not enough resting budget
        self.assertFalse(
            validate_resting_budget_is_enough(unrec, duration + 7200, budget)
        )


if __name__ == "__main__":
    unittest.main()
