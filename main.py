from dotenv import dotenv_values
from pages.login_page import LoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


def main():
   my_secret = dotenv_values(".env")
   print(my_secret)
   driver = webdriver.Chrome()

   my_page=LoginPage(driver)
   my_page.open("")
   my_page2=BasePage(driver)
   input()
   my_page2.open("")
   input()

if __name__ == "__main__":
   main()

