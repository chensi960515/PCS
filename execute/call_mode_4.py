#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: call_mode_4.py
@time: 2022/6/7  20:40
"""


from pcs_package import PCS_call


call = PCS_call.Call()

call.callParty(callOutType_custom=4)