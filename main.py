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

from time import strptime, mktime
from selenium import webdriver
from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.main_page import MainPage


def parse_time_string(time_string) -> float:
    """
    This function is taking a string time and return a float in seconds

    Arguments:
        string: time string in the format "xd xx:xxh" or "xx:xx"
    Return:
        float corresponding of the time interval in second
    """
    one_day_in_sec = 86400
    if "d" in time_string and "h" in time_string:
        parsed_time = (
            mktime(strptime(time_string, "%dd %H:%Mh")) + one_day_in_sec
        )

    else:
        parsed_time = mktime(strptime(time_string, "%H:%Mh"))
    return parsed_time - mktime(
        strptime("1900, 1, 1, 0, 0", "%Y, %m, %d, %H, %M")
    )


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
    print(my_secret)
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        user=my_secret.get("USERNAME"), password=my_secret.get("PASSWORD")
    )
    main_page = MainPage(driver)
    main_page.validate_popup_button()
    main_page.click_on_booking_tab()
    # breakpoint()
    main_page.validate_popup_button()
    main_page.type_attendance_duration(hours=7, minutes=45)
    main_page.type_break_duration(hours=0, minutes=45)


if __name__ == "__main__":
    budget = parse_time_string("2d 04:00h")
    duration = parse_time_string("2d 02:00h")
    unrec = parse_time_string("02:00h")
    print(f"{budget=}, {duration=}, {unrec=}")
    print(
        validate_resting_budget_is_enough(
            unrecorded_effort=unrec, duration_time=duration, budget_time=budget
        )
    )
