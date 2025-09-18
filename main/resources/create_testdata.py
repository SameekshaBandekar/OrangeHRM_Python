import os
from openpyxl import Workbook

#os.makedirs("OrangeHRMTest/main/resources", exist_ok=True)
file_path = "C:/Users/samee/Python_Workspace/OrangeHRMTest/main/resources/testdata.xlsx"

wb = Workbook()
sheet = wb.active
sheet.title = "Sheet1"

# Header row (note the "result" column)
sheet.append(["username", "password", "expected_result", "result"])

# Example data rows
sheet.append(["Admin", "admin123", "success", ""])
sheet.append(["user1", "wrongPass", "failure", ""])

wb.save(file_path)
print(f"Created {file_path}")
