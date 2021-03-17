from  pages.vk_auth import AuthPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.config import invalid_email, invalid_password

def test_vk_auth(selenium):

    page = AuthPage(selenium)
    page.enter_email(invalid_email)
    page.enter_password(invalid_password)
    page.btn_click()
    error = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_message"]/div/div/b[1]')))
    '''Явное ожидание'''

    assert page.get_relative_link() == '/login', 'warning'
