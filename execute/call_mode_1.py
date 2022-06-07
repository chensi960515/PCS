#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: call_mode_1.py
@time: 2022/6/7  20:39
"""

#   passcode_path='../eph_data/custom_1_hostPasscode.txt'


from pcs_package import PCS_call


call = PCS_call.Call()

call.callParty(callOutType_custom=1)