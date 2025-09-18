from selenium.webdriver.common.by import By

from main.pages.dashboard_page import DashBoardPage
from main.utils import wait_utils
from main.utils.wait_utils import WaitUtils


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)

    #locators
    username = (By.CSS_SELECTOR, 'input[name="username"]')
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH,"//p[contains(@class, 'oxd-alert-content-text') and text()='Invalid credentials']")

    def login(self,user,pwd):
        username_field = self.wait.wait_for_visibility_of_locator(self.username)
        username_field.send_keys(user)
        password_field = self.wait.wait_for_visibility_of_locator(self.password)
        password_field.send_keys(pwd)
        login_btn = self.wait.wait_for_element_to_be_clickable(self.login_button)
        login_btn.click()

        try:
            self.wait.wait_for_visibility_of_locator((By.XPATH, "//h6[text()='Dashboard']"))
            return DashBoardPage(self.driver)
        except:
            return None

    def get_error_message(self):
        error_msg = self.wait.wait_for_visibility_of_locator(self.error_message)
        return error_msg.text
