from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


def main():
   my_secret = dotenv_values(".env")
   print(my_secret)
   driver = webdriver.Chrome()
   login_page = LoginPage(driver)
   login_page.open()
   login_page.enter_email(my_secret.get("USERNAME"))
   input()


if __name__ == "__main__":
   main()

