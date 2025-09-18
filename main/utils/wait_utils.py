from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    def __init__(self, driver, timeout_seconds=20):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout_seconds)

    #wait for element
    def wait_for_visibility(self, element):
        return self.wait.until(EC.visibility_of(element))

    #wait for by locator
    def wait_for_visibility_of_locator(self,element):
        return self.wait.until(EC.visibility_of_element_located(element))

    #wait for element to be clickable
    def wait_for_element_to_be_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visibility_of_locators(self, locators):
        return self.wait.until(EC.visibility_of_all_elements_located(locators))






