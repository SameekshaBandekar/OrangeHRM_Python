import configparser
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    driver=None
    config=None

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    config = configparser.RawConfigParser()
    config_path=os.path.join(os.path.dirname(__file__), "../../main/resources/config.properties")
    config.read(config_path)
    browser_name=config.get("DEFAULT", "browser")
    url_path=config.get("DEFAULT", "url")

    if browser_name == "chrome":
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())  )
    elif browser_name == "firefox":
        driver=webdriver.Firefox()
    elif browser_name == "edge":
        driver=webdriver.Edge()
    else:
        raise Exception("Browser not supported")

    driver.get(url_path)
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()
