

""" 
WORKING CHART/ COPY ONLY
import pandas as pd
import numpy as np
import xlsxwriter


data = {"name": ["ali", "mohammad", "reza"],
        "sales": [1100, 1223, 1344]}

df = pd.DataFrame(data)


def make_chart(what, name):

    columns = list(what.columns)

    workbook = xlsxwriter.Workbook(f"{name}.xlsx")
    worksheet = workbook.add_worksheet("Sheet1")

    worksheet.write_column('A1', what[columns[0]])
    worksheet.write_column('B1', what[columns[1]])

    chart = workbook.add_chart({'type': 'column'})

    chart.add_series({
        'values': "=Sheet1!$B$1:$B$1",
        'name': "=Sheet1!$A$1:$A$1"
    })

    chart.add_series({
        'values': "=Sheet1!$B$2:$B$2",
        'name': "=Sheet1!$A$2:$A$2"
    })

    chart.add_series({
        'values': "=Sheet1!$B$3:$B$3",
        'name': "=Sheet1!$A$3:$A$3"
    })

    worksheet.insert_chart('E1', chart)

    workbook.close()


make_chart(df, "MyCHart") """
