import openpyxl
class ExcelUtils:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self, sheet_name):

        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook[sheet_name]

        data = []
        headers = [cell.value for cell in sheet[1]]  # first row as header

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))
            data.append(row_data)

        return data