"""
Module: locators
Author: Jonathan

This module contains locator classes for web elements on different pages of the web application.

Dependencies:
    - selenium.webdriver.common.by.By

Usage:
    This module provides locator classes for different pages of the web application.
    Each locator class contains tuples representing locators for specific web elements on the page,
    using Selenium's By class for specifying locator strategies.

Example:
    To use this module, import the desired locator class into your script:
        from locators import MainPageLocators

    Then, utilize the locator tuples within the class to locate web elements on the main page.

"""

from dataclasses import dataclass
from typing import Tuple
from selenium.webdriver.common.by import By


@dataclass
class MainPageLocators:
    """
    Locator class for web elements on the main page of the web application.

    Attributes:
        ACCOUNT: Locator for the account link.
        ATTANDENCE_HOUR: Locator for the input field for attendance hours.
        ATTANDENCE_MINUTE: Locator for the input field for attendance minutes.
        BREAK_HOUR: Locator for the input field for break hours.
        BREAK_MINUTE: Locator for the input field for break minutes.
        DAY_BOOKING_TAB: Locator for the booking tab.
        LOGIN: Locator for the login link.
        LOGO: Locator for the logo element.
        POP_UP_YES_BUTTON: Locator for the popup confirmation button.
        SAVE_BUTTON: Locator for the save button.
        SEARCH: Locator for the search input field.
        SEARCH_LIST: Locator for the search results list.
        SIGNUP: Locator for the signup link.
        TASKS_BUDGET: Locator for the tasks budget element.
        TASKS_DESCRIPTION_INPUT: Locator for the textarea for task description.
        TASKS_DURATION: Locator for the tasks duration element.
        TASKS_DURATION_INPUT_HOURS: Locator for the input field for task duration hours.
        TASKS_DURATION_INPUT_MINUTES: Locator for the input field for task duration minutes.
        UNRECORDED_EFFORTS_HOUR: Locator for the input field for unrecorded efforts hours.
        UNRECORDED_EFFORTS_MINUTE: Locator for the input field for unrecorded efforts minutes.
    """

    attandence_minute: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[1]//input[contains(@name, 'attandenceDuration_minute')]",
    )
    attandence_hour: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[1]//input[contains(@name, 'attandenceDuration_hour')]",
    )
    break_minute: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[2]//input[contains(@name, 'attandenceDuration_minute')]",
    )
    break_hour: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[2]//input[contains(@name, 'attandenceDuration_hour')]",
    )
    day_booking_tab: Tuple[str, str] = (
        By.XPATH,
        "//a[@id='PageTab_Link_jq_dayeffortrecording']",
    )
    pop_up_yes_button: Tuple[str, str] = (
        By.XPATH,
        "//input[@class='button notificationPermissionConfirm defaultbutton' and \
@type='submit' and @value='Yes']",
    )
    save_button: Tuple[str, str] = (By.XPATH, "//input[@value='Save']")
    search_list: Tuple[str, str] = (
        By.CSS_SELECTOR,
        'div[data-component-type="s-search-result"]',
    )
    tasks_budget: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']/tbody/tr/td[12]",
    )
    tasks_duration: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']/tbody/tr/td[13]",
    )
    tasks_duration_input_hours: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[9]//input[1]",
    )
    tasks_duration_input_minutes: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[9]//input[2]",
    )
    tasks_description_input: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[10]//textarea",
    )
    tasks_title_input: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']//td[6]//input",
    )
    tasks_reference_input: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']//td[5]//input",
    )
    unrecorded_efforts_minute: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[4]//input[contains(@name, 'attandenceDuration_minute')]",
    )
    unrecorded_efforts_hour: Tuple[str, str] = (
        By.XPATH,
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[4]//input[contains(@name, 'attandenceDuration_hour')]",
    )


@dataclass
class LoginPageLocators:
    """
    Locator class for web elements on the login page of the web application.

    Attributes:
        EMAIL: Locator for the email input field.
        PASSWORD: Locator for the password input field.
        SUBMIT: Locator for the submit button.
        ERROR_MESSAGE: Locator for the error message element.
    """

    email: Tuple[str, str] = (By.XPATH, "//input[@id='label_user']")
    password: Tuple[str, str] = (By.XPATH, "//input[@id='label_pwd']")
    submit: Tuple[str, str] = (By.XPATH, "//input[@id='loginbutton']")
    error_message: Tuple[str, str] = (By.ID, "message_error")
