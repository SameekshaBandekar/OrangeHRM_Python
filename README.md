***** OrangeHRM Automation with Selenium Python *****

**Project Overview**

This project contains automation scripts for the OrangeHRM web application using Selenium WebDriver with Python and Pytest.
It follows the Page Object Model (POM) design pattern:
•	Data-driven testing (JSON and Excel file as input)
•	Test reporting with Allure

**Project Structure**

OrangeHRMTest/

|── main/

│    ├── pages/ 

                
│   │       ├── login_page.py

│   │        ├── dashboard_page.py

│   │          └── pim_page.py

│    ├── resources/

│   │         ├── config.properties

│   │         ├── create_testdata.py

│   │         ├── testdata.xlsx

│   │           └── testdata1.json

│   └── utils/

│               ├── screenshot_utils.py

│               ├── excel_utils.py

│               ├── json_utils.py

│                └── wait_utils.py

├── test/

│      ├── testHRM/

│   │         ├── reports/

│   │   │             └── screenshots.py

│   │        ├── test_addnew_employee.py

│   │        ├── test_login.py

│   │   └── TestComponent/

│                └── base_test.py


**Tools & Technologies**

•	IDE: PyCharm 
•	Launguage: Python v3.13
•	Selenium v4.35
•	Pytest v8.4.2
•	Reporting: - Allure 2.15
•	Version Control: Git
•	Data Source: JSON, Excel
•	Design Patther: Page Object model 

** Test Scenario**

1.	Login Test - Valid and invalid credentials
2.	Create new employee

** Pre Requisite**
•	Python Installed (v3.13.7)
•	Selenium (v4.35)
•	IDE – PyCharm (or any IDE of choice)
•	Browser – Chrome, Firefox, Edge

** How to Run **
1.	Clone the repository (https://github.com/SameekshaBandekar/OrangeHRM_Python.git)
2.	Install IDE
3.	Install all dependencies (Selenium, Pytest, WebDriver manager, Allure reports)
4.	Configure project – config.properties, Json and Excel files.
5.	Run test using PyTest

** Project Highlights**

•	Uses Page Object Model for maintainable and reusable code
•	Used data driven testing approach to fetch test data. (JSON , EXCEL)
•	Captures screenshots
•	Generates Reports

**Contact**

For any questions regarding this project, please contact:
Name: Sameeksha Bandekar
Email: sameeksha.bandekar@gmail.com




