"""
Module: test_time_parser
Author: Jonathan

This module contains unit tests for the main module 'time_parser.py'.
It tests the functionality of the functions defined in 'main.py'.

Dependencies:
    - unittest
    - time_parser (the module under test)

Usage:
    This module can be executed directly to run all unit tests:
        $ python test_time_parser.py
"""

import unittest

from utils.time_parser import parse_time_string


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
            parse_time_string("14:32h"), 52320
        )  # 4 hours in seconds
        self.assertEqual(
            parse_time_string("04:00h"), 14400
        )  # 4 hours in seconds
        # Test parsing time string with days and hours
        self.assertEqual(
            parse_time_string("2d 04:00h"), 72000
        )  # 2 days and 4 hours in seconds
        self.assertEqual(
            parse_time_string("46d 04:44h"), 1341840
        )  # 2 days and 4 hours in seconds
        self.assertEqual(
            parse_time_string("01:01h"), 3660
        )  # 2 days and 4 hours in seconds


if __name__ == "__main__":
    unittest.main()
