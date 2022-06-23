#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: test_read_file.py
@time: 2022/5/30  21:39
"""
from itertools import count

from tools import read_file


ya = read_file.GetData()

conf_path = f".\config\meeting.yaml"


conf = ya.get_data_list(conf_path)

# data = conf['data']
# data['token'] = '123123'

keys = conf.keys()
print(type(conf))
print(type(keys))
for key in keys:
    if key[:4] == 'data':
        print(key)


