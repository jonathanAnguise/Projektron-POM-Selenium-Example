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

# def parse_days():
#     ...
# def parse_hours():
#     ...
# def parse_minutes():
#     ...

def parse_time_string(time_string: str) -> int:
    """
    This function is taking a string time and return a float in seconds

    Arguments:
        string: time string in the format "xd xx:xxh" or "xx:xx"
    Return:
        int corresponding of the time interval in second
    """
    seconds = 0
    if "d" in time_string:
        seconds += int(time_string.split("d")[0]) * 24 * 60 * 60
    time_string_list = time_string[:-1].split()[-1].split(":")
    seconds += int(time_string_list[0]) * 60 * 60 + int(time_string_list[1])
    return seconds


def validate_resting_budget_is_enough(
    unrecorded_effort, duration_time, budget_time
) -> bool:
    """
    Validates if the resting budget is enough for the given duration and unrecorded effort.

    Args:
        unrecorded_effort (struct_time): The unrecorded effort time.
        duration_time (struct_time): The duration time.
        budget_time (struct_time): The resting budget time.

    Returns:
        bool: True if the resting budget is enough, False otherwise.
    """
    return unrecorded_effort + duration_time <= budget_time


# def type_attendance_in_the_valid_line(main_page_object: MainPage):
#     task_budget_list = main_page_object.get_tasks_budget_list()
#     task_duration_list = main_page_object.get_tasks_duration_list()
#     unrecorded_time = main_page_object.get_unrecorded_efforts()
#     unrecorded_time_seconds = parse_time_string(unrecorded_time)
# 
#     merge_list = [(parse_time_string(budget), parse_time_string(duration)) for budget, duration in zip(task_budget_list, task_duration_list)]
#     for index, tasks_values in enumerate(merge_list, start=0):
#         if tasks_values[0]>= tasks_values[1] + unrecorded_time_seconds:
#             continue
#         else:
#             ...
#     ...



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
    breakpoint()


if __name__ == "__main__":
    main()
