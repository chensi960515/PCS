# -*- coding: utf-8 -*-
# @Time : 2022/6/22 14:39
# @Author : chensi
# @File : PCS_createMeeting.py
# @Project : PCS

import requests
import json
import time
import logging
from tools import read_file

logging.getLogger().setLevel(logging.INFO)

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)


class PCS_create:
    list_meetingId = []
    #电话列表
    party_partyTel = []

    def save_meetingID(self, x):
        with open('../eph_data/meetingID.txt', 'a', encoding='utf-8') as f:
            f.write(str(x))
            f.write("\n")
        with open('../eph_data/meetingID.txt', 'r', encoding='utf-8') as f:
            x = f.read()

    def save_hostPasscode(self, z):
        with open('../eph_data/hostPasscode.txt', 'a', encoding='utf-8') as f:
            f.write(str(z))
            f.write("\n")
        with open('../eph_data/hostPasscode.txt', 'r', encoding='utf-8') as f:
            z = f.read()

    def save_4_hostPasscode(self, k):
        with open('../eph_data/custom_4_hostPasscode.txt', 'a', encoding='utf-8') as f:
            f.write(str(k))
            f.write("\n")
        with open('../eph_data/custom_4_hostPasscode.txt', 'r', encoding='utf-8') as f:
            k = f.read()

    #参数提取出来,便于控制
    partyList = []
    counsellor_dict = {
        "partyName": party_partyTel[0],
        "partyType": "0",
        "countryCode": "",
        "areaCode": "",
        "partyTel": party_partyTel[0],
        "partyEmail": "",
        "isCallOut": "1"
    }
    user_dict = {
        "partyName": party_partyTel[0],
        "partyType": "1",
        "countryCode": "",
        "areaCode": "",
        "partyTel": party_partyTel[0],
        "partyEmail": "",
        "isCallOut": "1"
    }

    def create_Meeting(self,token, times, start_time, counsellor_num=1, user_num=0):
        try:
            if type(counsellor_num) is int and counsellor_num > 0:
                for i in range(counsellor_num):
                    pass

            elif counsellor_num == 0:
                    logging.error("==========会议必须存在一个顾问===========")
            else :
                logging.error("==========counsellor_num参数错误===========")


        except Exception as e:
            logging.error(e)



    def create_Meeting_four(self, token, times, start_time, num_guwen,num_user,party_partyTel, callOutType_custom, hangUpSetting=0, hangUpDuration=0,
                            isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,
                            contactName="", contactTelephone="", contactEmail=""):

        url = conf['parameter']['url_create_Meeting']
        payload_client_two = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle": "No." + str(times) + "-场景" + str(callOutType_custom) + "-录" + str(isRecord) + "-客" + str(
                subscribeHostStatus) + "-顾" + str(subscribeGuestStatus) + "-结" + str(hangUpDuration),
            "startTime": start_time,
            "duration": "120",
            "partyList": [
                {
                    "partyName": party_partyTel[0],
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel[0],
                    "partyEmail": "",
                    "isCallOut": "1"
                },
                {
                    "partyName": party_partyTel_1,
                    "partyType": "1",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel_1,
                    "partyEmail": "",
                    "isCallOut": "1"
                }
            ],
            "contactList": [
                {
                    "contactName": contactName,
                    "contactTelephone": contactTelephone,
                    "contactEmail": contactEmail
                }
            ],
            "hangUpSetting": hangUpSetting,
            "hangUpDuration": hangUpDuration,
            "callOutType": callOutType_custom,
            "isRecord": isRecord,
            "joinType": 0,
            "meetingExplain": "倾听,类型:" + str(callOutType_custom),
            "subscribeHostStatus": subscribeHostStatus,
            "subscribeGuestStatus": subscribeGuestStatus
        })
        headers = conf['parameter']['headers']

        response = requests.request("POST", url, headers=headers, data=payload_client_two)
        logging.info(payload_client_two)
        logging.info(response.text)
        res = json.loads(response.text)
        now_meetingId = res['data']['meetingId']
        self.save_meetingID(now_meetingId)
        now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(
            str(now_hostPasscode) + "场景:" + str(callOutType_custom) + "人数:5" + "第" + str(times) + "场")
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res
