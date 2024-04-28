"""
Module: main_page
Author: Jonathan

This module contains a page class for the main page of a web application,
built for Selenium automation.

Dependencies:
    - pages.base_page.BasePage
    - utils.locators.MainPageLocators

Usage:
    This module provides a class `MainPage` representing the main page of a web application.
    It inherits from the `BasePage` class and includes methods for interacting with the main page,
    such as validating popup buttons and clicking on booking tabs.

Example:
    To use this module, import the `MainPage` class into your script:
        from main_page import MainPage

    Then, create an instance of `MainPage` and utilize its methods for interacting with
    the main page.

"""

from utils.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Page class representing the main page of a web application.

    Attributes:
        locator (MainPageLocators): Locators for elements on the main page.

    Methods:
        validate_popup_button: Validate and click on the popup button.
        click_on_booking_tab: Click on the booking tab.
    """

    def __init__(self, driver):
        """
        Initialize the MainPage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.locator = MainPageLocators
        super().__init__(driver)

    def validate_popup_button(self):
        """Validate and click on the popup button."""
        self.wait_element(*self.locator.POP_UP_YES_BUTTON).click()

    def click_on_booking_tab(self):
        """Click on the booking tab."""
        self.wait_element(*self.locator.DAY_BOOKING_TAB).click()
