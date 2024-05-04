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
    main()
