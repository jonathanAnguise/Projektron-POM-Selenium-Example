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

from selenium import webdriver
from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.time_parser import parse_hours, parse_minutes


def validate_resting_budget_is_enough(
    unrecorded_effort, duration_time, budget_time
) -> bool:
    """
    Validates if the resting budget is enough for the given duration
    and unrecorded effort.

    Args:
        unrecorded_effort (struct_time): The unrecorded effort time.
        duration_time (struct_time): The duration time.
        budget_time (struct_time): The resting budget time.

    Returns:
        bool: True if the resting budget is enough, False otherwise.
    """
    return unrecorded_effort + duration_time <= budget_time


def main():
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
    my_secret = dotenv_values(".env")
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        user=my_secret.get("USERNAME"), password=my_secret.get("PASSWORD")
    )
    main_page = MainPage(driver)
    main_page.validate_popup_button()
    main_page.click_on_booking_tab()
    main_page.validate_popup_button()
    main_page.type_attendance_duration(hours=7, minutes=45)
    main_page.type_break_duration(hours=0, minutes=45)
    task_index_to_input = main_page.get_first_available_task()
    unrecorded_effort_time = main_page.get_unrecorded_efforts()
    unrecorded_effort_hours = parse_hours(unrecorded_effort_time)["hours"]
    unrecorded_effort_minutes = parse_minutes(unrecorded_effort_time)[
        "minutes"
    ]
    main_page.type_task_duration(
        hours=unrecorded_effort_hours,
        minutes=unrecorded_effort_minutes,
        task_line=task_index_to_input,
    )
    main_page.type_task_description(
        task_line=task_index_to_input, text="JEMBERTA-333"
    )
    main_page.type_task_reference(task_line=task_index_to_input, text="TA")
    main_page.type_task_title(task_line=task_index_to_input, text="TA")
    # breakpoint()


if __name__ == "__main__":
    main()
