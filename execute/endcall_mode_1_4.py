#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: endcall_mode_1_4.py
@time: 2022/6/7  20:40
"""


from pcs_package import PCS_call


call = PCS_call.Call()

#call.end_callParty(callOutType_custom=4)


call.end_callParty(callOutType_custom=1)