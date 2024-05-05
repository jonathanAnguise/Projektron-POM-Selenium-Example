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
        type_attendance_duration: Type in the attendance duration.
        type_break_duration: Type in the break duration.
        get_tasks_budget_list: Get a list of elements representing tasks budgets.
        get_tasks_duration_list: Get a list of elements representing tasks durations.
        type_task_duration: Type in the duration of a specific task.
        type_task_description: Type in the description of a specific task.
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
        """
        Validate and click on the popup button.
        """
        self.wait_element(*self.locator.POP_UP_YES_BUTTON).click()

    def click_on_booking_tab(self):
        """
        Click on the booking tab.
        """
        self.wait_element(*self.locator.DAY_BOOKING_TAB).click()

    def type_attendance_duration(self, hours=8, minutes=0):
        """
        Type in the attendance duration in hours and minutes.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        self.wait_element(*self.locator.ATTANDENCE_HOUR).send_keys(str(hours))
        self.wait_element(*self.locator.ATTANDENCE_MINUTE).send_keys(
            str(minutes)
        )

    def type_break_duration(self, hours=1, minutes=0):
        """
        Type in the break duration in hours and minutes.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        self.wait_element(*self.locator.BREAK_HOUR).send_keys(str(hours))
        self.wait_element(*self.locator.BREAK_MINUTE).send_keys(str(minutes))

    def get_tasks_budget_list(self):
        """
        Get a list of elements representing tasks budgets.

        Returns:
            list: A list of string representing tasks budgets.
        """
        return [
            budget.text
            for budget in self.find_elements(*self.locator.TASKS_BUDGET)
        ]

    def get_tasks_duration_list(self):
        """
        Get a list of elements representing tasks durations.

        Returns:
            list: A list of string representing tasks durations.
        """
        return [
            duration.text
            for duration in self.find_elements(*self.locator.TASKS_DURATION)
        ]

    def type_task_duration(self, task_line=1, hours=1, minutes=0):
        """
        Type in the duration of a specific task in hours and minutes.

        Args:
            task_line (int): The line number of the task.
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        tasks_hours = self.find_elements(
            *self.locator.TASKS_DURATION_INPUT_HOURS
        )
        tasks_minutes = self.find_elements(
            *self.locator.TASKS_DURATION_INPUT_MINUTES
        )
        tasks_minutes[task_line].send_keys(minutes)
        tasks_hours[task_line].send_keys(hours)

    def type_task_description(self, task_line=1, text="test"):
        """
        Type in the description of a specific task.

        Args:
            task_line (int): The line number of the task.
            text (str): The description text.
        """
        tasks = self.find_elements(*self.locator.TASKS_DESCRIPTION_INPUT)
        tasks[task_line].send_keys(text)

    def get_unrecorded_efforts(self):
        """
        Get text string of unrecorded effort

        Returns:
            string: A string of unrecorded time efforts
        """
        unrecorded_minutes = self.find_element(
            *self.locator.UNRECORDED_EFFORTS_MINUTE
        ).get_attribute("value")
        unrecorded_hours = self.find_element(
            *self.locator.UNRECORDED_EFFORTS_HOUR
        ).get_attribute("value")
        return f"{unrecorded_hours}:{unrecorded_minutes}h"

    def click_on_save_button(self):
        """
        Click on the save button.
        """
        self.find_element(*self.locator.SAVE_BUTTON).click()
