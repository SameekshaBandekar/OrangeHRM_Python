import allure
import pytest
from main.pages.login_page import LoginPage
from main.utils.json_utils import read_json
from test.testComponents.test_base import BaseTest

test_data = read_json("testdata1.json")


@allure.feature("Login Feature")
class TestAddNewEmployee(BaseTest):

    @pytest.mark.parametrize("data", test_data)
    @allure.title("Login and add new employee from JSON")
    def test_add_new_employee(self,data):
        login_page = LoginPage(self.driver)
        dashboard_page = login_page.login(data["username"], data["password"])
        pim_page = dashboard_page.navigate_to_pim()
        pim_page.add_employee()
        pim_page.create_employee(data["firstname"], data["middlename"], data["lastname"])
        pim_page.navigate_to_employee_list()
        full_name = f"{data['firstname']} {data['middlename']}"
        pim_page.search_employee(full_name)
        assert pim_page.is_employee_present(full_name), f"Employee {full_name} not found"
        print(f"Employee {full_name} successfully added and found in PIM list.")


