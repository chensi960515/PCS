#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: PCS_getcallphone.py
@time: 2022/6/7  21:27
"""

list_hostPasscode = []


class get_passcode:

    def set_passcode(self, passcode_path, x):
        with open(passcode_path, 'a', encoding='utf-8') as f:
            f.write(str(x))
            f.write("\n")

    def get_call_phone_passcode(self, passcode_path, callOutType_custom=1, callOutType_custom_index=12, str_start=0,
                                str_end=9):
        with open(passcode_path, 'r', encoding='utf-8') as f:
            for x in f:
                if x[callOutType_custom_index].isdigit() and int(x[callOutType_custom_index]) == callOutType_custom:
                    list_hostPasscode.append(x[str_start:str_end])

        return list_hostPasscode

# p = get_passcode()
# p.get_call_phone_passcode(passcode_path="../eph_data/hostPasscode.txt", callOutType_custom=4,
#                           callOutType_custom_index=12, str_start=0, str_end=9)
