# -*- coding: utf-8 -*-
# @Time : 2022/6/27 13:24
# @Author : chensi
# @File : sava_info.py
# @Project : PCS

def save_Meeting_Info(path: str, x):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(str(x))
        f.write("\n")
    with open(path, 'r', encoding='utf-8') as f:
        f.read()

