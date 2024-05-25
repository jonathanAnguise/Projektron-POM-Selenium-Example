"""
Module: locators
Author: Jonathan

This module contains locator classes for web elements on different pages of the web application.

Usage:
    This module provides locator classes for different pages of the web application.
    Each locator class contains tuples representing locators for specific web elements on the page,
    using Selenium's By class for specifying locator strategies.

Example:
    To use this module, import the desired locator class into your script:
        from locators import MainPageLocators

    Then, utilize the locator tuples within the class to locate web elements on the main page.

"""

from enum import Enum


class MainPageLocators(str, Enum):
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

    ATTANDENCE_MINUTE: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[1]//input[contains(@name, 'attandenceDuration_minute')]"
    )

    ATTANDENCE_HOUR: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[1]//input[contains(@name, 'attandenceDuration_hour')]"
    )

    BREAK_MINUTE: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[2]//input[contains(@name, 'attandenceDuration_minute')]"
    )

    BREAK_HOUR: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[2]//input[contains(@name, 'attandenceDuration_hour')]"
    )

    DAY_BOOKING_TAB: str = "//a[@id='PageTab_Link_jq_dayeffortrecording']"

    POP_UP_YES_BUTTON: str = (
        "//input[@class='button notificationPermissionConfirm defaultbutton' and \
@type='submit' and @value='Yes']"
    )

    SAVE_BUTTON: str = "//input[@value='Save']"
    TASKS_BUDGET: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']/tbody/tr/td[12]"
    )

    TASKS_DURATION: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']/tbody/tr/td[13]"
    )

    TASKS_DURATION_INPUT_HOURS: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[9]//input[1]"
    )

    TASKS_DURATION_INPUT_MINUTES: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[9]//input[2]"
    )

    TASKS_DESCRIPTION_INPUT: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']\
/tbody/tr/td[10]//textarea"
    )

    TASKS_TITLE_INPUT: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']//td[6]//input"
    )

    TASKS_REFERENCE_INPUT: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingTaskList_table']//td[5]//input"
    )

    UNRECORDED_EFFORTS_MINUTE: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[4]//input[contains(@name, 'attandenceDuration_minute')]"
    )

    UNRECORDED_EFFORTS_HOUR: str = (
        "//table[@id='daytimerecording,Content,daytimerecordingAttendance_table']\
/tbody/tr[4]//input[contains(@name, 'attandenceDuration_hour')]"
    )


class LoginPageLocators(Enum):
    """
    Locator class for web elements on the login page of the web application.

    Attributes:
        EMAIL: Locator for the email input field.
        PASSWORD: Locator for the password input field.
        SUBMIT: Locator for the submit button.
        ERROR_MESSAGE: Locator for the error message element.
    """

    EMAIL: str = "//input[@id='label_user']"
    PASSWORD: str = "//input[@id='label_pwd']"
    SUBMIT: str = "//input[@id='loginbutton']"
