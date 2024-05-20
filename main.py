"""
Module: projektron_automator
Author: Jonathan

This module contains a script for automating web interactions using Selenium.
It includes functions to log in to a web application and perform
various actions on the main page.

Dependencies:
    - selenium
    - dotenv

Usage:
    This module can be executed directly.
    It reads credentials from a '.env' file and uses them to log in to
    the specified web application.

Example:
    To run this module, execute it directly from the command line:
        $ python web_automation.py
"""

import sys
from typing import Dict, Optional, Union
from selenium import webdriver
from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.time_parser import parse_hours, parse_minutes


def parse_arguments(
    defaults: Optional[Dict[str, Union[int, str]]] = None
) -> Dict[str, Union[int, str]]:
    """
    Parse command-line arguments into a dictionary.

    Args:
        defaults (dict, optional): A dictionary containing default values for
        the arguments.
            If provided, these defaults will be used for any arguments not
            specified on the command line.
            Defaults to None.

    Returns:
        dict: A dictionary containing the parsed command-line arguments.
    """
    arguments: Dict[str, Union[int, str]] = defaults if defaults else {}
    for arg in sys.argv[1:]:
        key, value = arg.split("=")
        arguments[key] = value
    return arguments


def main() -> None:
    """
    Main function that executes the web automation script.

    Reads credentials from a '.env' file, initializes a Selenium WebDriver,
    logs in to the specified web application,
    and performs actions on the main page.

    Usage:
        main()

    Returns:
        None
    """
    defaults: Dict[str, Union[int, str]] = {
        "hours": 9,
        "minutes": 0,
        "title": "TA",
        "reference": "TA",
        "task_description": "RACK maintenance",
    }
    arguments: Dict[str, Union[int, str]] = parse_arguments(defaults)

    my_secret: Dict[str, Union[str, None]] = dotenv_values(".env")
    driver: webdriver.Chrome = webdriver.Chrome()
    login_page: LoginPage = LoginPage(driver)
    login_page.open()
    if isinstance(my_secret.get("USERNAME"), str) and isinstance(
        my_secret.get("PASSWORD"), str
    ):
        login_page.login(
            user=str(my_secret.get("USERNAME")),
            password=str(my_secret.get("PASSWORD")),
        )
    else:
        print("Credentials are not valid")
        sys.exit(1)
    main_page: MainPage = MainPage(driver)
    main_page.validate_popup_button()
    main_page.click_on_booking_tab()
    main_page.validate_popup_button()
    if not (isinstance(arguments["hours"], int) and isinstance(
        arguments["minutes"], int
    )):
        print("arguments are incorrect")
        sys.exit(1)
    main_page.type_attendance_duration(
        hours=int(arguments["hours"]), minutes=int(arguments["minutes"])
    )
    main_page.type_break_duration(hours=0, minutes=45)
    task_index_to_input: int = main_page.get_first_available_task()
    unrecorded_effort_time: str = main_page.get_unrecorded_efforts()
    unrecorded_effort_hours: int = parse_hours(unrecorded_effort_time)["hours"]
    unrecorded_effort_minutes: int = parse_minutes(unrecorded_effort_time)[
        "minutes"
    ]
    main_page.type_task_duration(
        hours=unrecorded_effort_hours,
        minutes=unrecorded_effort_minutes,
        task_line=task_index_to_input,
    )
    if not (
        isinstance(arguments["task_description"], str)
        and isinstance(arguments["reference"], str)
        and isinstance(arguments["title"], str)
    ):
        print("arguments not valid")
        sys.exit(1)
    main_page.type_task_description(
        task_line=task_index_to_input,
        text=str(arguments["task_description"]),
    )
    main_page.type_task_reference(
        task_line=task_index_to_input, text=str(arguments["reference"])
    )
    main_page.type_task_title(
        task_line=task_index_to_input, text=str(arguments["title"])
    )
    input("Please double check and validate manually")


if __name__ == "__main__":
    main()
