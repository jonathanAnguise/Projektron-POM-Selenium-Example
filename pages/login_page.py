"""
Module: login_page
Author: Jonathan

This module contains a page class for the login page of a web application, designed 
for Selenium automation.

Dependencies:
    - pages.base_page.BasePage
    - utils.locators.LoginPageLocators

Usage:
    This module provides a class `LoginPage` representing the login page of a web application.
    It inherits from the `BasePage` class and includes methods for interacting with the login page,
    such as entering email and password, clicking the login button, and performing login actions.

Example:
    To use this module, import the `LoginPage` class into your script:
        from login_page import LoginPage

    Then, create an instance of `LoginPage` and utilize its methods for interacting with the
    login page.

"""

from utils.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page class representing the login page of a web application.

    Attributes:
        locator (LoginPageLocators): Locators for elements on the login page.

    Methods:
        enter_email: Enter the email into the email input field.
        enter_password: Enter the password into the password input field.
        click_login_button: Click the login button.
        login: Perform login with provided credentials.
    """

    def __init__(self, driver):
        """
        Initialize the LoginPage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.locator = LoginPageLocators
        super().__init__(driver)  # Python2 version

    def enter_email(self, email):
        """
        Enter the email into the email input field.

        Args:
            email (str): The email to enter.
        """
        self.wait_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        """
        Enter the password into the password input field.

        Args:
            password (str): The password to enter.
        """
        self.wait_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        """
        Click the login button.

        """
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user, password):
        """
        Log in with provided credentials.

        Args:
            user (str): The username/email.
            password (str): The password.
        """
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()
