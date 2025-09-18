import allure
import pytest

from main.pages.login_page import LoginPage
from main.utils.excel_utils import ExcelUtils
from test.testComponents.test_base import BaseTest

excel= ExcelUtils("C:/Users/samee/Python_Workspace/OrangeHRMTest/main/resources/testdata.xlsx")
test_data=excel.get_data("Sheet1")


@allure.feature("Login Feature")
class TestLogin(BaseTest):

    @pytest.mark.parametrize("data", test_data)
    @allure.title("Login Test")
    def test_login(self,data):
     with allure.step(f"Login attempt for user: {data['username']}"):
        login_page = LoginPage(self.driver)
        login_page.login(data["username"], data["password"])

        if data["expected_result"].lower() == "success":
            # Validate login success
            assert "dashboard" in self.driver.current_url.lower(), f"Login failed for user: {data['username']}"
            print(f"Login successful for user: {data['username']}")
        else:
            # Validate login failure
            error_message = login_page.get_error_message()
            assert error_message == "Invalid credentials", f"Unexpected error message for user {data['username']}: {error_message}"
            print(f"Login failed for user: {data['username']}. Error: {error_message}")