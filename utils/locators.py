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
from selenium.webdriver.common.by import By


@dataclass
class MainPageLocators:
    """
    Locator class for web elements on the main page of the web application.

    Attributes:
        LOGO: Locator for the logo element.
        ACCOUNT: Locator for the account link.
        SIGNUP: Locator for the signup link.
        LOGIN: Locator for the login link.
        SEARCH: Locator for the search input field.
        SEARCH_LIST: Locator for the search results list.
        POP_UP_YES_BUTTON: Locator for the popup confirmation button.
        DAY_BOOKING_TAB: Locator for the booking tab.
    """

    LOGO = (By.ID, "nav-logo")
    ACCOUNT = (By.ID, "nav-link-accountList")
    SIGNUP = (By.CSS_SELECTOR, "#nav-signin-tooltip > div > a")
    LOGIN = (By.CSS_SELECTOR, "#nav-signin-tooltip > a")
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_LIST = (
        By.CSS_SELECTOR,
        'div[data-component-type="s-search-result"]',
    )
    POP_UP_YES_BUTTON = (
        By.XPATH,
        "//input[@class='button notificationPermissionConfirm defaultbutton' and \
@type='submit' and @value='Yes']",
    )
    DAY_BOOKING_TAB = (
        By.XPATH,
        "//a[@id='PageTab_Link_jq_dayeffortrecording']",
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

    EMAIL = (By.XPATH, "//input[@id='label_user']")
    PASSWORD = (By.XPATH, "//input[@id='label_pwd']")
    SUBMIT = (By.XPATH, "//input[@id='loginbutton']")
    ERROR_MESSAGE = (By.ID, "message_error")
