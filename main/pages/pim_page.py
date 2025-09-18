from selenium.webdriver.common.by import By
from main.utils.wait_utils import WaitUtils


class PimPage:

    # Locators
    add_employee_button = (By.XPATH, "//a[text()='Add Employee']")
    first_name_field = (By.XPATH, "//input[@name='firstName']")
    middle_name_field = (By.XPATH, "//input[@name='middleName']")
    last_name_field = (By.XPATH, "//input[@name='lastName']")
    save_button = (By.CSS_SELECTOR, "button[type='submit']")
    employee_list = (By.XPATH, "//a[text()='Employee List']")
    employee_name = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
    search_btn = (By.XPATH, "//button[@type='submit']")
    e_record = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)

    def add_employee(self):
        add_button = self.wait.wait_for_visibility_of_locator(self.add_employee_button)
        add_button.click()
        return self

    def create_employee(self, Fname, Mname, Lname):
        first_name = self.wait.wait_for_visibility_of_locator(self.first_name_field)
        first_name.send_keys(Fname)

        middle_name = self.wait.wait_for_visibility_of_locator(self.middle_name_field)
        middle_name.send_keys(Mname)

        last_name = self.wait.wait_for_visibility_of_locator(self.last_name_field)
        last_name.send_keys(Lname)

        save_btn = self.wait.wait_for_element_to_be_clickable(self.save_button)
        save_btn.click()

        return PimPage(self.driver)

    def navigate_to_employee_list(self):
        emp_list = self.wait.wait_for_visibility_of_locator(self.employee_list)
        emp_list.click()
        return PimPage(self.driver)

    def search_employee(self, e_name):
        emp_name = self.wait.wait_for_visibility_of_locator(self.employee_name)
        emp_name.send_keys(e_name)

        search_button = self.wait.wait_for_element_to_be_clickable(self.search_btn)
        search_button.click()

    def is_employee_present(self, full_name):
        rows = self.wait.wait_for_visibility_of_locators(self.e_record)
        for row in rows:
            if full_name in row.text:
                return True
        return False