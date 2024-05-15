"""
Module: time_parser

This module provides functions for parsing time strings and converting them into seconds.
"""


def parse_days(time_string: str) -> int:
    """
    Parse a time string and return the corresponding time interval in seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        int: The time of days in seconds.
    """
    seconds = 0
    if "d" in time_string:
        seconds += int(time_string.split("d")[0]) * 24 * 60 * 60
    return seconds


def parse_hours(time_string: str) -> int:
    """
    Parse a time string and return the corresponding time interval in seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        int: The time of hours in seconds.
    """
    hours = int(time_string[:-1].split()[-1].split(":")[0])
    seconds = hours * 60 * 60
    return seconds


def parse_minutes(time_string: str) -> int:
    """
    Parse a time string and return the corresponding time interval in seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        int: The time of minutes in seconds.
    """
    minutes = int(time_string[:-1].split()[-1].split(":")[1])
    seconds = minutes * 60
    return seconds


def parse_time_string(time_string: str) -> int:
    """
    This function is taking a string time and return a float in seconds

    Arguments:
        string: time string in the format "xd xx:xxh" or "xx:xx"
    Return:
        int corresponding of the time interval in second
    """
    seconds = (
        parse_days(time_string)
        + parse_hours(time_string)
        + parse_minutes(time_string)
    )
    return seconds
