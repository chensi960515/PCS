#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: multi-process.py
@time: 2022/6/7  21:12
"""

from multiprocessing import Pool


def get_params():
    # construct all params
    all_params = []

    for i in range(10):
        params = {'name': 'xxx', 'index': i}

        all_params.append(params)

    # multi process request
    with Pool() as p:

        all_response = p.map(test, all_params)

    # process results

    return all_response



def test(params: dict):
    # ni zi jide fang fa
    return 0


if __name__ == '__main__':
    print(get_params())