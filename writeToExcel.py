import openpyxl


def writeToExcelFunction(rowNum, colNum, value):
    print("------saved excel file open------")
    wb_obj = openpyxl.load_workbook("top100BooksByMedium.xlsx")
    sheet_obj = wb_obj.active
    m_row = sheet_obj.max_row
    print("rows=" + str(m_row))
    sheet_obj.cell(row=rowNum + 1, column=colNum).value = str(value)  # col num 4


if __name__ == '__main__':
    print("unexpected calling")
