from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    POP_UP_YES_BUTTON = (By.XPATH, "//input[@class='button notificationPermissionConfirm defaultbutton' and @type='submit' and @value='Yes']")
    DAY_BOOKING_TAB = (By.XPATH, "//a[@id='PageTab_Link_jq_dayeffortrecording']")


class LoginPageLocators(object):
    EMAIL = (By.XPATH, "//input[@id='label_user']")
    PASSWORD = (By.XPATH, "//input[@id='label_pwd']")
    SUBMIT = (By.XPATH, "//input[@id='loginbutton']")
    ERROR_MESSAGE = (By.ID, 'message_error')
