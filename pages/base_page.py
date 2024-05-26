"""
Module: base_page
Author: Jonathan

This module provides a base class for web pages using Selenium for automation.

Dependencies:
    - selenium

Usage:
    This module provides a base class ``BasePage`` that can be inherited by other page classes.
    It includes common methods for interacting with web pages such as finding elements,
    opening URLs, getting page titles and URLs, and waiting for elements to load.

Classes:
    - :class:`BasePage`: Base class for web pages, 
    providing common methods for Selenium-based automation.

Functions:
    - :func:`_get_base_url`: Retrieve the base URL from a secret manager.

Attributes:
    - **driver** (*WebDriver*): The Selenium WebDriver instance.
    - **base_url** (*str*): The base URL of the web application.
    - **timeout** (*int*): Timeout duration for waiting for elements to load, default is 30 seconds.

Methods:
    - :meth:`BasePage.find_element`: Find a web element using a locator.
    - :meth:`BasePage.find_element_by_xpath`: Find a web element using an XPath locator.
    - :meth:`BasePage.find_elements`: Find multiple web elements using a locator.
    - :meth:`BasePage.find_elements_by_xpath`: Find multiple web elements using an XPath locator.
    - :meth:`BasePage.open`: Open a URL in the web browser.
    - :meth:`BasePage.get_title`: Get the title of the current web page.
    - :meth:`BasePage.get_url`: Get the URL of the current web page.
    - :meth:`BasePage.wait_element`: Wait for an element to be located on the page.
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
    """
    Retrieve the base URL from a secret manager.

    :return: The base URL as a string.
    :rtype: str
    """
    base_url = get_secret_value(SecretValues.URL)
    return base_url


class BasePage:
    """
    Base class for web pages using Selenium for automation.

    :param driver: The Selenium WebDriver instance.
    :type driver: WebDriver

    :Attributes:
        - **driver** (*WebDriver*): The Selenium WebDriver instance.
        - **base_url** (*str*): The base URL of the web application.
        - **timeout** (*int*): Timeout duration for waiting for elements
        to load, default is 30 seconds.

    :Methods:
        - :meth:`find_element`: Find a web element using a locator.
        - :meth:`find_element_by_xpath`: Find a web element using an XPath locator.
        - :meth:`find_elements`: Find multiple web elements using a locator.
        - :meth:`find_elements_by_xpath`: Find multiple web elements using an XPath locator.
        - :meth:`open`: Open a URL in the web browser.
        - :meth:`get_title`: Get the title of the current web page.
        - :meth:`get_url`: Get the URL of the current web page.
        - :meth:`wait_element`: Wait for an element to be located on the page.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage.

        :param driver: The Selenium WebDriver instance.
        :type driver: WebDriver
        """
        self.base_url: str = _get_base_url()
        self.driver: WebDriver = driver
        self.timeout: int = 30

    def find_element(self, *locator: str) -> WebElement:
        """
        Find a web element using a locator.

        :param locator: Variable-length argument list representing the locator strategy and value.
        :type locator: str
        :return: The web element found.
        :rtype: WebElement
        """
        return self.driver.find_element(*locator)

    def find_element_by_xpath(self, locator: str) -> WebElement:
        """
        Find a web element using an XPath locator.

        :param locator: The XPath locator.
        :type locator: str
        :return: The web element found.
        :rtype: WebElement
        """
        return self.driver.find_element(by=By.XPATH, value=locator)

    def find_elements(self, *locator: str) -> List[WebElement]:
        """
        Find multiple web elements using a locator.

        :param locator: Variable-length argument list representing the locator strategy and value.
        :type locator: str
        :return: A list of web elements found.
        :rtype: List[WebElement]
        """
        return self.driver.find_elements(*locator)

    def find_elements_by_xpath(self, locator: str) -> List[WebElement]:
        """
        Find multiple web elements using an XPath locator.

        :param locator: The XPath locator.
        :type locator: str
        :return: A list of web elements found.
        :rtype: List[WebElement]
        """
        return self.driver.find_elements(by=By.XPATH, value=locator)

    def open(self, url: str = "") -> None:
        """
        Open a URL in the web browser.

        :param url: The URL to open. Default is an empty string.
        :type url: str, optional
        """
        self.driver.get(self.base_url + url)

    def get_title(self) -> str:
        """
        Get the title of the current web page.

        :return: The title of the current web page.
        :rtype: str
        """
        return self.driver.title

    def get_url(self) -> str:
        """
        Get the URL of the current web page.

        :return: The URL of the current web page.
        :rtype: str
        """
        return self.driver.current_url

    def wait_element(
        self,
        locator: str,
        by_method: str = By.XPATH,
    ) -> WebElement:
        """
        Wait for an element to be located on the page.

        :param locator: The locator of the element.
        :type locator: str
        :param by_method: The method to locate the element, default is By.XPATH.
        :type by_method: str, optional
        :return: The web element found.
        :rtype: WebElement
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, locator))
        )
