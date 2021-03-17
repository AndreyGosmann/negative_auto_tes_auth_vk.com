from selenium.webdriver.common.by import By

class AuthLocators:
    EMAIL = (By.ID, 'index_email')
    PASSWORD = (By.ID, 'index_pass')
    BTN = (By.ID, 'index_login_button')