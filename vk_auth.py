from .base_page import BasePage
from .locators import  AuthLocators
from .config import base_url
from selenium.webdriver.support.ui import WebDriverWait

class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = base_url
        driver.get(url)


        self.email = driver.find_element(*AuthLocators.EMAIL)
        self.password = driver.find_element(*AuthLocators.PASSWORD)
        self.btn = driver.find_element(*AuthLocators.BTN)

    def enter_email(self, value):
        self.email.clear()
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.clear()
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
