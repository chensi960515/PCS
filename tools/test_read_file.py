#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: test_read_file.py
@time: 2022/5/31  22:22
"""

import xlrd
import pandas as pd

excel_path = "F:\\263\\电话.xlsx"


def get_phone_excel(excelFile, list_index):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(list_index)
    row_count = table.nrows
    col_count = table.ncols

    dataFile = []
    res = []

    for rowNum in range(row_count):
        for colNum in range(col_count):
            dataFile.append(table.row_values(rowNum,colNum))
    for i in dataFile :
        if len(i[0]) > 0 and i[0] not in res:
            res.append(i[0])

    return res


phone_guwen = get_phone_excel(excelFile=excel_path, list_index=0)
# phone_user1 = get_phone_excel(excelFile=excel_path, list_index=1)
# phone_user2 = get_phone_excel(excelFile=excel_path, list_index=2)
# phone_user3 = get_phone_excel(excelFile=excel_path, list_index=3)

print(len(phone_guwen))
print(phone_guwen[-1])


# xls = pd.ExcelFile(r'F:\\263\\电话.xlsx')#创建一个ExcelFile对象
# df = pd.DataFrame()
# for name in xls.sheet_names:
# 	## xls.sheet_names是一个包含所有sheet名称的列表
# 	data = pd.ExcelFile.parse(xls,sheet_name=name)#读取单个sheet的数据
# 	df = df.append(data)
#
# print(df)
