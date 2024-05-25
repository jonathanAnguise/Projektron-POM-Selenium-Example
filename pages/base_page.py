"""
Module: base_page
Author: Jonathan

This module contains a base class for web pages using Selenium for automation.

Dependencies:
    - selenium

Usage:
    This module provides a base class `BasePage` that can be inherited by other page classes.
    It includes common methods for interacting with web pages such as finding elements,
    opening URLs, getting page titles and URLs, and waiting for elements to load.

Example:
    To use this module, import the `BasePage` class into your script:
        from base_page import BasePage

    Then, inherit from `BasePage` in your page classes and utilize its methods.

"""

from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.secret_manager import (
    get_secret_value,
    SecretValues,
)


def _get_base_url() -> str:
    base_url = get_secret_value(SecretValues.URL)
    return base_url


class BasePage:
    """
    Base class for web pages using Selenium for automation.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance.
        base_url (str): The base URL of the web application.
        timeout (int): Timeout duration for waiting for elements to load, default is 30 seconds.

    Methods:
        find_element: Find a web element using a locator.
        open: Open a URL in the web browser.
        get_title: Get the title of the current web page.
        get_url: Get the URL of the current web page.
        wait_element: Wait for an element to be located on the page.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.base_url: str = _get_base_url()
        self.driver: WebDriver = driver
        self.timeout: int = 30

    def find_element(self, *locator: str) -> WebElement:
        """
        Find a web element using a locator.

        Args:
            *locator: Variable-length argument list representing the locator strategy and value.

        Returns:
            WebElement: The web element found.
        """
        return self.driver.find_element(*locator)

    def find_element_by_xpath(self, locator: str) -> WebElement:
        """
        Find a web element using a locator.

        Args:
            *locator: Variable-length argument list representing the locator strategy and value.

        Returns:
            WebElement: The web element found.
        """
        return self.driver.find_element(by=By.XPATH, value=locator)

    def find_elements(self, *locator: str) -> List[WebElement]:
        """
        Find a web element using a locator.

        Args:
            locator: String of the xpath locator.

        Returns:
            list of WebElement: The list of  web elements found.
        """
        return self.driver.find_elements(*locator)

    def find_elements_by_xpath(self, locator: str) -> List[WebElement]:
        """
        Find a web element using a locator.

        Args:
            locator: String of the xpath locator.

        Returns:
            list of WebElement: The list of  web elements found.
        """
        return self.driver.find_elements(by=By.XPATH, value=locator)

    def open(self, url: str = "") -> None:
        """
        Open a URL in the web browser.

        Args:
            url (str, optional): The URL to open. Default is an empty string.
        """
        self.driver.get(self.base_url + url)

    def get_title(self) -> str:
        """
        Get the title of the current web page.

        Returns:
            str: The title of the current web page.
        """
        return self.driver.title

    def get_url(self) -> str:
        """
        Get the URL of the current web page.

        Returns:
            str: The URL of the current web page.
        """
        return self.driver.current_url

    def wait_element(
        self,
        locator: str,
        by_method: str = By.XPATH,
    ) -> WebElement:
        """
        Wait for an element to be located on the page.

        Args:
            *locator: Variable-length argument list representing the locator strategy and value.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, locator))
        )
