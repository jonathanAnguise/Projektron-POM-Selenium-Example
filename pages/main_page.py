from utils.locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(MainPage, self).__init__(driver)  # Python2 version

    def validate_popup_button(self):
        self.wait_element(*self.locator.POP_UP_YES_BUTTON).click()

    def click_on_booking_tab(self, password):
        self.wait_element(*self.locator.DAY_BOOKING_TAB).click()
