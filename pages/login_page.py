"""
Module: login_page
Author: Jonathan

This module contains a page class for the login page of a web application, designed 
for Selenium automation.

Dependencies:
    - pages.base_page.BasePage
    - utils.locators.LoginPageLocators

Usage:
    This module provides a class ``LoginPage`` representing
    the login page of a web application.
    It inherits from the ``BasePage`` class and includes methods
    for interacting with the login page,
    such as entering email and password, clicking the login button,
    and performing login actions.

Classes:
    - :class:`LoginPage`: Page class representing the login page, providing
    methods for interacting with the login page.

Methods:
    - :meth:`LoginPage.enter_email`: Enter the email into the email input field.
    - :meth:`LoginPage.enter_password`: Enter the password into the password input field.
    - :meth:`LoginPage.click_login_button`: Click the login button.
    - :meth:`LoginPage.login`: Perform login with provided credentials.
"""

from utils.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page class representing the login page of a web application.

    :Attributes:
        - **locator** (:class:`LoginPageLocators`): Locators for elements on the login page.

    :Methods:
        - :meth:`enter_email`: Enter the email into the email input field.
        - :meth:`enter_password`: Enter the password into the password input field.
        - :meth:`click_login_button`: Click the login button.
        - :meth:`login`: Perform login with provided credentials.
    """

    def enter_email(self, email: str) -> None:
        """
        Enter the email into the email input field.

        :param email: The email to enter.
        :type email: str
        """
        self.wait_element(LoginPageLocators.EMAIL.value).send_keys(email)

    def enter_password(self, password: str) -> None:
        """
        Enter the password into the password input field.

        :param password: The password to enter.
        :type password: str
        """
        self.wait_element(LoginPageLocators.PASSWORD.value).send_keys(password)

    def click_login_button(self) -> None:
        """
        Click the login button.
        """
        self.find_element_by_xpath(LoginPageLocators.SUBMIT.value).click()

    def login(self, user: str, password: str) -> None:
        """
        Log in with provided credentials.

        :param user: The username/email.
        :type user: str
        :param password: The password.
        :type password: str
        """
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()
