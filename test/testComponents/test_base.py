import configparser
import os

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from main.utils.screenshot_utils import take_screenshot


class BaseTest:
    driver = None
    config = None

    def setup_method(self, method):
        self.config = configparser.RawConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), "../../main/resources/config.properties")
        self.config.read(config_path)

        browser_name = self.config.get("DEFAULT", "browser")
        url_path = self.config.get("DEFAULT", "url")

        # Initialize browser
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
        else:
            raise Exception(f"Browser '{browser_name}' not supported")

        # Launch application
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url_path)

    def capture_screenshot_for_result(self, method):

        import sys
        failed = False
        if hasattr(self, "_outcome"):
            for name, error in self._outcome.errors:
                if error:
                    failed = True


        status = "FAIL" if failed else "PASS"

        # Take screenshot
        screenshot_path = take_screenshot(self.driver, f"{method.__name__}_{status}")

        # Attach to Allure
        with open(screenshot_path, "rb") as f:
            allure.attach(f.read(), name=f"{method.__name__}_{status}", attachment_type=allure.attachment_type.PNG)

    def teardown_method(self, method):
        self.capture_screenshot_for_result(method)
        if self.driver:
            self.driver.quit()