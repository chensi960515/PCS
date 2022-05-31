#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: test_read_file.py
@time: 2022/5/30  21:39
"""

from tools import read_file


ya = read_file.GetPages()

conf_path = f".\config\config.yaml"


conf = ya.get_data_list(conf_path)

url = conf['test']['url_token']

print(url)
