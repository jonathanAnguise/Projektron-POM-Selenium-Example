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

from typing import List, Tuple
from selenium.webdriver.remote.webelement import WebElement
from utils.locators import MainPageLocators
from utils.time_parser import parse_time_string
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

    def validate_popup_button(self) -> None:
        """
        Validate and click on the popup button.
        """
        self.wait_element(MainPageLocators.POP_UP_YES_BUTTON).click()

    def click_on_booking_tab(self) -> None:
        """
        Click on the booking tab.
        """
        self.wait_element(MainPageLocators.DAY_BOOKING_TAB).click()

    def type_attendance_duration(
        self, hours: int = 8, minutes: int = 0
    ) -> None:
        """
        Type in the attendance duration in hours and minutes.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        self.wait_element(MainPageLocators.ATTANDENCE_HOUR).clear()
        self.wait_element(MainPageLocators.ATTANDENCE_HOUR).send_keys(
            str(hours)
        )
        self.wait_element(MainPageLocators.ATTANDENCE_MINUTE).clear()
        self.wait_element(MainPageLocators.ATTANDENCE_MINUTE).send_keys(
            str(minutes)
        )

    def type_break_duration(self, hours: int = 1, minutes: int = 0) -> None:
        """
        Type in the break duration in hours and minutes.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        self.wait_element(MainPageLocators.BREAK_HOUR).clear()
        self.wait_element(MainPageLocators.BREAK_HOUR).send_keys(str(hours))
        self.wait_element(MainPageLocators.BREAK_MINUTE).clear()
        self.wait_element(MainPageLocators.BREAK_MINUTE).send_keys(
            str(minutes)
        )

    def get_tasks_budget_list(self) -> List[str]:
        """
        Get a list of elements representing tasks budgets.

        Returns:
            list: A list of string representing tasks budgets.
        """
        return [
            budget.text
            for budget in self.find_elements_by_xpath(
                MainPageLocators.TASKS_BUDGET
            )
        ]

    def get_tasks_duration_list(self) -> List[str]:
        """
        Get a list of elements representing tasks durations.

        Returns:
            list: A list of string representing tasks durations.
        """
        return [
            duration.text
            for duration in self.find_elements_by_xpath(
                MainPageLocators.TASKS_DURATION
            )
        ]

    def type_task_duration(
        self, task_line: int = 0, hours: int = 1, minutes: int = 0
    ) -> None:
        """
        Type in the duration of a specific task in hours and minutes.

        Args:
            task_line (int): The line number of the task.
            hours (int): The number of hours.
            minutes (int): The number of minutes.
        """
        tasks_hours: List[WebElement] = self.find_elements_by_xpath(
            MainPageLocators.TASKS_DURATION_INPUT_HOURS
        )
        tasks_minutes: List[WebElement] = self.find_elements_by_xpath(
            MainPageLocators.TASKS_DURATION_INPUT_MINUTES
        )
        tasks_minutes[task_line].clear()
        tasks_hours[task_line].clear()
        tasks_minutes[task_line].send_keys(str(minutes))
        tasks_hours[task_line].send_keys(str(hours))

    def type_task_description(
        self, task_line: int = 0, text: str = "test"
    ) -> None:
        """
        Type in the description of a specific task.

        Args:
            task_line (int): The line number of the task.
            text (str): The description text.
        """
        tasks: List[WebElement] = self.find_elements_by_xpath(
            MainPageLocators.TASKS_DESCRIPTION_INPUT
        )
        tasks[task_line].clear()
        tasks[task_line].send_keys(text)

    def type_task_reference(
        self, task_line: int = 0, text: str = "test"
    ) -> None:
        """
        Type in the reference of a specific task.

        Args:
            task_line (int): The line number of the task.
            text (str): The description text.
        """
        tasks: List[WebElement] = self.find_elements_by_xpath(
            MainPageLocators.TASKS_REFERENCE_INPUT
        )
        tasks[task_line].clear()
        tasks[task_line].send_keys(text)

    def type_task_title(self, task_line: int = 0, text: str = "test") -> None:
        """
        Type in the title of a specific task.

        Args:
            task_line (int): The line number of the task.
            text (str): The description text.
        """
        tasks: List[WebElement] = self.find_elements_by_xpath(
            MainPageLocators.TASKS_TITLE_INPUT
        )
        tasks[task_line].clear()
        tasks[task_line].send_keys(text)

    def get_unrecorded_efforts(self) -> str:
        """
        Get text string of unrecorded effort

        Returns:
            string: A string of unrecorded time efforts
        """
        unrecorded_minutes: str = (
            self.find_element_by_xpath(
                MainPageLocators.UNRECORDED_EFFORTS_MINUTE
            ).get_attribute("value")
            or "00"
        )
        unrecorded_hours: str = (
            self.find_element_by_xpath(
                MainPageLocators.UNRECORDED_EFFORTS_HOUR
            ).get_attribute("value")
            or "00"
        )
        return f"{unrecorded_hours}:{unrecorded_minutes}h"

    def click_on_save_button(self) -> None:
        """
        Click on the save button.
        """
        self.find_element_by_xpath(MainPageLocators.SAVE_BUTTON).click()

    def get_first_available_task(self) -> int:
        """
        Return the index of the first available task line.

        This function retrieves task budget, task duration, and unrecorded time
        from the main page.
        It compares the total budgeted time for tasks with the sum of
        task durations and unrecorded time.
        If the total budgeted time exceeds the sum of durations and
        unrecorded time for a task,
        it returns the index of task line in the main page.

        Returns:
            int: Index of the line or -1 if now budget is available
        """
        task_budget_list: List[str] = self.get_tasks_budget_list()
        task_duration_list: List[str] = self.get_tasks_duration_list()
        unrecorded_time: str = self.get_unrecorded_efforts()
        unrecorded_time_seconds: int = parse_time_string(unrecorded_time)
        task_index: int = -1

        merge_list: List[Tuple[int, int]] = [
            (parse_time_string(budget), parse_time_string(duration))
            for budget, duration in zip(task_budget_list, task_duration_list)
        ]
        for index, tasks_values in enumerate(merge_list, start=0):
            if tasks_values[0] <= tasks_values[1] + unrecorded_time_seconds:
                continue
            task_index = index
            break
        return task_index
