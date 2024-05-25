"""
Module: test_secret_manager
Author: Jonathan

This module contains unit tests for the main module 'secret_manager'.
It tests the functionality of the functions defined in 'secret_manager.py'.

Dependencies:
    - unittest
    - secret_manager (the module under test)

Usage:
    This module can be executed directly to run all unit tests:
        $ python test_secret_manager.py
"""

from typing import Dict, Union
import unittest
from unittest.mock import patch
from utils.secret_manager import (
    EmptySecretsError,
    get_secrets,
    MissingKeyError,
    get_secret_value,
    SecretValues,
)


class TestGetSecrets(unittest.TestCase):
    """
    Test cases for the parse_time_string function.
    """

    @patch("utils.secret_manager.dotenv_values")
    def test_get_secrets_success(self, mock_dotenv_values):
        """
        Test get_secrets returns correct dictionary when .env file has content.
        """
        # Mock dotenv_values to return a non-empty dictionary
        mock_dotenv_values.return_value = {"SECRET_KEY": "supersecretvalue"}

        secrets: Dict[str, Union[str, None]] = get_secrets()
        self.assertEqual(secrets, {"SECRET_KEY": "supersecretvalue"})

    @patch("utils.secret_manager.dotenv_values")
    def test_get_secrets_empty(self, mock_dotenv_values):
        """
        Test get_secrets returns correct dictionary when .env is empty.
        """
        # Mock dotenv_values to return an empty dictionary
        mock_dotenv_values.return_value = {}

        with self.assertRaises(EmptySecretsError) as context:
            get_secrets()

        self.assertEqual(str(context.exception), "The secrets file is empty.")

    def test_get_secrets_with_wrong_path(self):
        """
        Test get_secrets raises EmptySecretsError when provided with a wrong file path.
        """
        with self.assertRaises(EmptySecretsError) as context:
            get_secrets("wrong_path")
        self.assertEqual(str(context.exception), "The secrets file is empty.")


class TestGetSecretValue(unittest.TestCase):
    """
    Test cases for the get_secret_value function.
    """

    @patch("utils.secret_manager.get_secrets")
    def test_get_secret_value_success(self, mock_get_secrets):
        """
        Test get_secret_value returns correct valid key.
        """
        mock_get_secrets.return_value = {
            SecretValues.USERNAME.value: "Superman",
            SecretValues.PASSWORD.value: "qwerty",
            SecretValues.URL.value: "www.google.de",
        }
        self.assertEqual(
            get_secret_value(SecretValues.USERNAME.value), "Superman"
        )
        self.assertEqual(
            get_secret_value(SecretValues.PASSWORD.value), "qwerty"
        )
        self.assertEqual(
            get_secret_value(SecretValues.URL.value), "www.google.de"
        )

    @patch("utils.secret_manager.get_secrets")
    def test_get_secret_value_missing_key(self, mock_get_secrets):
        """
        Test get_secret_value raises MissingKeyError when key is not found
        """
        mock_get_secrets.return_value = {
            SecretValues.USERNAME.value: "Superman",
            SecretValues.PASSWORD.value: "qwerty",
        }
        with self.assertRaises(MissingKeyError) as context:
            get_secret_value(SecretValues.URL.value)
        self.assertEqual(
            str(context.exception),
            f"{SecretValues.URL.value} not found in .env",
        )

    @patch("utils.secret_manager.get_secrets")
    def test_get_secret_value_no_key(self, mock_get_secrets):
        """
        Test get_secret_value raises MissingKeyError when the dictionary is empty
        """
        mock_get_secrets.return_value = {}
        with self.assertRaises(MissingKeyError) as context:
            get_secret_value(SecretValues.URL.value)
        self.assertEqual(
            str(context.exception),
            f"{SecretValues.URL.value} not found in .env",
        )

    @patch("utils.secret_manager.dotenv_values")
    def test_get_secret_value_missing_dictionnary(self, mock_dotenv_values):
        """
        Test get_secrets raises EmptySecretsError when get_secret_value is called
        but there is not secret file"""
        mock_dotenv_values.return_value = {}
        with self.assertRaises(EmptySecretsError) as context:
            get_secret_value(SecretValues.URL.value)
        self.assertEqual(str(context.exception), "The secrets file is empty.")


if __name__ == "__main__":
    unittest.main()
