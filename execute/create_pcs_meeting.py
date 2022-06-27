#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: create_pcs_meeting.py
@time: 2022/6/1  2:16
"""

import logging
from pcs_package import PCS_createMeeting
from pcs_package import PCS_getToken
from tools import read_file

# 设置loggin.info 可控制台输出
logging.getLogger().setLevel(logging.INFO)

# 配置文件的路径,名称是固定的
ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meet_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)
meet = ya.get_data_list(meet_path)

excel_path = conf['parameter']['excelFile']

phone = ya.get_phone_excel(excelFile=excel_path, list_index=0)
params = meet['data']

pcs_create = PCS_createMeeting.PCS_create()


# 测试创建会议
pcs_create.create_Meeting(param=params, party_partyTel=phone, counsellor_num=1, user_num=2, meeting_num=5)


# 创建 100场xxx的会议

# 创建 20场xxx的会议