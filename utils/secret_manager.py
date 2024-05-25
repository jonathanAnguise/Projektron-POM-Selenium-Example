"""
Module: secret_manager
Author: Jonathan

This module provides functionality for securely reading and accessing secret values
from a .env file. It includes custom exceptions for handling empty secrets files and
missing keys, and uses an Enum to define valid keys for secret values.

Classes:
    EmptySecretsError: Exception raised when the secrets file is found to be empty.
    MissingKeyError: Exception raised when a specific key is not found in the secrets file.
    SecretValues: Enum representing the keys for secrets.

Functions:
    get_secrets(secret_file: str) -> Dict[str, Union[str, None]]:
        Reads the secrets from a given file and returns them as a dictionary.
    get_secret_value(key: secret_key, secret_file: str) -> str:
        Retrieves a specific secret value from the secrets file.
"""

from enum import Enum
from typing import Dict, Union
from dotenv import dotenv_values


class EmptySecretsError(Exception):
    """Custom exception for empty secrets."""


class MissingKeyError(Exception):
    """Custom exception for empty secrets."""


class SecretValues(str, Enum):
    """Enum representing the keys for secrets."""

    USERNAME: str = "USERNAME"
    PASSWORD: str = "PASSWORD"
    URL: str = "URL"


def get_secrets(secret_file: str = ".env") -> Dict[str, Union[str, None]]:
    """
    Reads the secrets from a given file and returns them as a dictionary.
    Raises an EmptySecretsError if the secrets file is empty.

    :param secret_file: The path to the secrets file.
    :return: Dictionary of secrets.
    """
    secrets: Dict = dotenv_values(secret_file)
    if not secrets:
        raise EmptySecretsError("The secrets file is empty.")
    return secrets


def get_secret_value(key: str, secret_file: str = ".env") -> str:
    """
    Retrieves a specific secret value from the secrets file.
    Raises a MissingKeyError if the key is not found in the secrets.

    :param key: The key of the secret to retrieve.
    :param secret_file: The path to the secrets file.
    :return: The secret value as a string.
    """
    username: Union[str, None] = get_secrets(secret_file).get(key)
    if not username:
        raise MissingKeyError(f"{key} not found in {secret_file}")
    return str(username)
