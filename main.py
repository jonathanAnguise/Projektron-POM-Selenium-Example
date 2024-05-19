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

from sys import argv
from typing import Dict, Optional, Union
from selenium import webdriver
from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.time_parser import parse_hours, parse_minutes


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
    arguments: dict = parse_arguments(defaults)

    my_secret: dict = dotenv_values(".env")
    driver: webdriver.Chrome = webdriver.Chrome()
    login_page: LoginPage = LoginPage(driver)
    login_page.open()
    login_page.login(
        user=my_secret.get("USERNAME"), password=my_secret.get("PASSWORD")
    )
    main_page: MainPage = MainPage(driver)
    main_page.validate_popup_button()
    main_page.click_on_booking_tab()
    main_page.validate_popup_button()
    main_page.type_attendance_duration(
        hours=arguments["hours"], minutes=arguments["minutes"]
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
    main_page.type_task_description(
        task_line=task_index_to_input, text=arguments["task_description"]
    )
    main_page.type_task_reference(
        task_line=task_index_to_input, text=arguments["reference"]
    )
    main_page.type_task_title(
        task_line=task_index_to_input, text=arguments["title"]
    )
    input("Please double check and validate manually")


def parse_arguments(
    defaults: Optional[Dict[str, Union[int, str]]] = None
) -> dict:
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
    for arg in argv[1:]:
        key, value = arg.split("=")
        arguments[key] = value
    return arguments


if __name__ == "__main__":
    main()
