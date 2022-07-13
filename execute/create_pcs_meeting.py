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

sec_params = meet['sec_meeting']
# pcs_create = PCS_createMeeting.PCS_create()

create = createMeeting.create()

# 创建会议


# pcs_create.create_Meeting(param=params, party_partyTel=phone[:500], counsellor_num=1, user_num=4, meeting_num=60)
#
# pcs_create.create_Meeting(param=params, party_partyTel=phone[500: 1000], counsellor_num=1, user_num=4, meeting_num=80)
#
# pcs_create.create_Meeting(param=params, party_partyTel=phone[1000:2000], counsellor_num=1, user_num=4, meeting_num=120)

#create.create_Meeting(request_type='scp', param=params, party_partyTel=phone[20:40], counsellor_num=1, user_num=4, meeting_num=3)


create.create_Meeting(request_type='sec', param=sec_params, party_partyTel=phone[:20], counsellor_num=1, user_num=4, meeting_num=1)
