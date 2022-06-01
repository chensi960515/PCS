# -*- coding: utf-8 -*-
# @Time : 2022/5/30 17:44
# @Author : chensi
# @File : PCS_cancelMeeting.py
# @Project : CVATest

"""
    只针对未开启或者已经过期的倾听会议
    取消会议

"""
import requests
import json
import logging
from tools import read_file
from pcs_package import PCS_getToken

# 设置loggin.info 可控制台输出
logging.getLogger().setLevel(logging.INFO)

# 配置文件的路径,名称是固定的
ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meet_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)

#还需要优化下,让其他人调用吧



list_meetingId = []


def get_Token():
    url = conf['parameter']['url_token']

    payload = json.dumps({
        "customerId": conf['parameter']['customerId'],
        "secret": conf['parameter']['secret']
    })
    headers = conf['parameter']['headers']

    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)
    new_token = res['data']['token']
    return new_token

def get_meetingId():
    with open('../eph_data/meetingID.txt', 'r', encoding='utf-8') as f:
        for x in f:
            list_meetingId.append(x[0:4])

def delete_Meeting(meetingId):
    url = conf['parameter']['url_cancelMeeting']

    payload = json.dumps({
        "token": token,
        "userAccount": conf['parameter']['userAccount'],
        "meetingId": meetingId
    })
    headers = conf['parameter']['headers']

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

token = get_Token()
get_meetingId()

for i in range(len(list_meetingId)):
    delete_Meeting(list_meetingId[i])
    logging.info(list_meetingId[i])

#清空操作
def remove_meetingId():
    with open('../eph_data/meetingID.txt', 'a+', encoding='utf-8') as f:
        f.truncate(0)
