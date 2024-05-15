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
from utils.time_parser import parse_time_string, parse_hours, parse_minutes


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


def type_duration_in_the_first_available_task_line(main_page_object: MainPage):
    """
    Type duration in the first available task line.

    This function retrieves task budget, task duration, and unrecorded time
    from the main page object.
    It compares the total budgeted time for tasks with the sum of
    task durations and unrecorded time.
    If the total budgeted time exceeds the sum of durations and
    unrecorded time for a task,
    it types the duration of unrecorded time for that task in the main page.

    Args:
        main_page_object (MainPage): An instance of
        the MainPage class representing the main page object.

    Returns:
        None
    """
    task_budget_list = main_page_object.get_tasks_budget_list()
    task_duration_list = main_page_object.get_tasks_duration_list()
    unrecorded_time = main_page_object.get_unrecorded_efforts()
    unrecorded_time_seconds = parse_time_string(unrecorded_time)

    merge_list = [
        (parse_time_string(budget), parse_time_string(duration))
        for budget, duration in zip(task_budget_list, task_duration_list)
    ]
    for index, tasks_values in enumerate(merge_list, start=0):
        if tasks_values[0] <= tasks_values[1] + unrecorded_time_seconds:
            continue
        main_page_object.type_task_duration(
            task_line=index,
            hours=parse_hours(unrecorded_time)["hours"],
            minutes=parse_minutes(unrecorded_time)["minutes"],
        )
        break


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
    # breakpoint()


if __name__ == "__main__":
    main()
