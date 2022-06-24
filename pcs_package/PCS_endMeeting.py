# -*- coding: utf-8 -*-
# @Time : 2022/5/30 15:35
# @Author : chensi
# @File : PCS_endMeeting.py
# @Project : CVATest

"""
    只针对 已经开启的倾听会议
    执行结束会议

"""


import requests
import json
import logging
import PCS_getcallphone
from tools import read_file
from pcs_package import PCS_getToken

# 设置loggin.info 可控制台输出
logging.getLogger().setLevel(logging.INFO)

# 配置文件的路径,名称是固定的
ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meet_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)

passcode = PCS_getcallphone.get_passcode()


cookie = conf['parameter']['cookie']

test_url = conf['parameter']['url_endMeeting']

list_hostPasscode = []

def get_hostPasscode():
    with open('../eph_data/hostPasscode.txt', 'r', encoding='utf-8') as f:
        for x in f:
            list_hostPasscode.append(x[0:9])


def end_meeting(hostPasscode):
    url = test_url + str(hostPasscode)

    headers = {
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers)
    print(url)
    print(response.text)

get_hostPasscode()
for i in range(len(list_hostPasscode)):
    end_meeting(list_hostPasscode[i])