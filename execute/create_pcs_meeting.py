#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: create_pcs_meeting.py
@time: 2022/6/1  2:16
"""

import logging
from pcs_package import createMeeting
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

sec_params_cx1 = meet['sec_meeting_cx1']
sec_params_cx2 = meet['sec_meeting_cx1']
sec_params_cx3 = meet['sec_meeting_cx1']

create = createMeeting.create()

# 创建会议



# SEC 畅听会议  cx1 账号 第一个60场
create.create_Meeting(request_type='sec', param=sec_params_cx1, party_partyTel=phone[0:350], counsellor_num=1, user_num=4, meeting_num=60)

create.create_Meeting(request_type='sec', param=sec_params_cx1, party_partyTel=phone[350:700], counsellor_num=1, user_num=4, meeting_num=60)

create.create_Meeting(request_type='sec', param=sec_params_cx1, party_partyTel=phone[700:1050], counsellor_num=1, user_num=4, meeting_num=60)

# PCS 倾听会议  kaoyao 账号. 唯一120场   时间与 哪个保持一致?

create.create_Meeting(request_type='pcs', param=params, party_partyTel=phone[1100:2000], counsellor_num=1, user_num=4, meeting_num=60)
