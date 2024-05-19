"""
Module: time_parser

This module provides functions for parsing time strings and converting them into seconds.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TimeConstant:
    """
    A class to represent various time-related constants.

    Attributes:
    -----------
    working_hours : int
        The standard number of working hours in a day.
    seconds_in_hour : int
        The number of seconds in an hour.
    seconds_in_minute : int
        The number of seconds in a minute.
    """

    working_hours: int = 8
    seconds_in_hour: int = 3600
    seconds_in_minute: int = 60


def parse_days(time_string: str) -> dict:
    """
    Parse a time string and return the corresponding time interval in days and seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        dict: The time of days in days and seconds.
    """
    days = 0
    seconds = 0
    if "d" in time_string:
        days = int(time_string.split("d")[0])
        seconds = (
            days * TimeConstant.working_hours * TimeConstant.seconds_in_hour
        )
    return {"days": days, "equivalent_seconds": seconds}


def parse_hours(time_string: str) -> dict:
    """
    Parse a time string and return the corresponding time interval in hours and seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        dict: The time of hours in minutes and seconds.
    """
    hours = int(time_string[:-1].split()[-1].split(":")[0])
    seconds = hours * TimeConstant.seconds_in_hour
    return {"hours": hours, "equivalent_seconds": seconds}


def parse_minutes(time_string: str) -> dict:
    """
    Parse a time string and return the corresponding time interval in minutes and seconds.

    Args:
        string: time string in the format "xd xx:xxh" or "xx:xx"

    Returns:
        dict: The time of minutes in minutes and seconds.
    """
    minutes = int(time_string[:-1].split()[-1].split(":")[1])
    seconds = minutes * TimeConstant.seconds_in_minute
    return {"minutes": minutes, "equivalent_seconds": seconds}


def parse_time_string(time_string: str) -> int:
    """
    This function is taking a string time and return a float in seconds

    Arguments:
        string: time string in the format "xd xx:xxh" or "xx:xx"
    Return:
        int corresponding of the time interval in second
    """
    seconds = (
        parse_days(time_string)["equivalent_seconds"]
        + parse_hours(time_string)["equivalent_seconds"]
        + parse_minutes(time_string)["equivalent_seconds"]
    )
    return seconds
