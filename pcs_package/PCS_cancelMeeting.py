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

pcs_token = PCS_getToken.Get_Token()
token = pcs_token.get_Token()
list_meetingId = []
del_meetingId = []


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
    logging.info(response.text)
    res = json.loads(response.text)
    if res['msg'] == 'success' and res['code'] == 0:
        del_meetingId.append(meetingId)
    else:
        logging.error("删除会议没成功.")


get_meetingId()
for i in range(len(list_meetingId)):
    delete_Meeting(list_meetingId[i])


