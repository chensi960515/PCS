#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: read_file.py
@time: 2022/5/30  21:26
"""

import yaml
import xlrd


class GetData:

    def get_data_list(self, file):
        ya = open(file, 'r', encoding='UTF-8')
        cfg = ya.read()
        ya.close()
        data = yaml.safe_load(cfg)
        return data

    def get_phone_excel(self, excelFile, list_index):
        data = xlrd.open_workbook(excelFile)
        table = data.sheet_by_index(list_index)
        row_count = table.nrows
        col_count = table.ncols
        dataFile = []
        res = []

        for rowNum in range(row_count):
            for colNum in range(col_count):
                dataFile.append(table.row_values(rowNum, colNum))
        for i in dataFile:
            if len(i[0]) > 0 and i not in res:
                res.append(i[0])

        return res
