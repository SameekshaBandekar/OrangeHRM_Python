from selenium.webdriver.common.by import By

from main.pages.pim_page import PimPage
from main.utils.wait_utils import WaitUtils


class DashBoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)


# locators
    dashboard_header = (By.CSS_SELECTOR, 'h6.oxd-text--h6.oxd-topbar-header-breadcrumb-module')
    pim_menu = (By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewPimModule']")

    def get_dashboard_header(self):
        header_element = self.wait.wait_for_visibility_of_locator(self.dashboard_header)
        return header_element.text

    def navigate_to_pim(self):
        pim_element = self.wait.wait_for_visibility_of_locator(self.pim_menu)
        pim_element.click()
        return PimPage(self.driver)