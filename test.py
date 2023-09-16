import pandas as pd
import numpy as np
import xlsxwriter

name = ["ali", "mamad", "hassan"]
amount = [1, 2, 3]

workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet("Sheet1")

worksheet.write_column('A1', name)
worksheet.write_column('B1', amount)

chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'name': 'Sales',
    'categories': "=Sheet1!$A$1:$A$3",
    'values': "=Sheet1!$B$1:$B$3"
})


worksheet.insert_chart('E1', chart)

workbook.close()
