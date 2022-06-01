# -*- coding: utf-8 -*-
# @Time : 2022/5/20 17:06
# @Author : chensi
# @File : PCS_createmeeing.py
# @Project : CVATest

import requests
import json
import time
import logging
from tools import read_file

logging.getLogger().setLevel(logging.INFO)

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)


class PCS_create():
    list_meetingId = []

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

    def create_Meeting_one(self, token, times, start_time, party_partyTel_0, party_partyTel_1, callOutType_custom,
                           hangUpSetting, hangUpDuration, isRecord, subscribeHostStatus, subscribeGuestStatus,
                           contactName, contactTelephone, contactEmail):

        url = conf['parameter']['url_create_Meeting']

        payload_client_one = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle": "No." + str(times) + "-场景" + str(callOutType_custom) + "-录" + str(isRecord) + "-客" + str(
                subscribeHostStatus) + "-顾" + str(subscribeGuestStatus) + "-结" + str(hangUpDuration),
            "startTime": start_time,
            "duration": "120",
            "partyList": [
                {
                    "partyName": party_partyTel_0,
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel_0,
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

        response = requests.request("POST", url, headers=headers, data=payload_client_one)
        logging.info(payload_client_one)
        logging.info(response.text)
        res = json.loads(response.text)
        self.now_meetingId = res['data']['meetingId']
        self.save_meetingID(self.now_meetingId)
        self.now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(str(now_hostPasscode) + "--2--" + str(times))
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res

    def create_Meeting_two(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2,
                           callOutType_custom, hangUpSetting, hangUpDuration, isRecord, subscribeHostStatus,
                           subscribeGuestStatus, contactName, contactTelephone, contactEmail):

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
                    "partyName": party_partyTel_0,
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel_0,
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
                },
                {
                    "partyName": party_partyTel_2,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_2,
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
        self.save_hostPasscode(str(now_hostPasscode) + "--3--" + str(times))
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res

    def create_Meeting_thred(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2,
                             party_partyTel_3, callOutType_custom, hangUpSetting, hangUpDuration, isRecord,
                             subscribeHostStatus, subscribeGuestStatus, contactName, contactTelephone, contactEmail):

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
                    "partyName": party_partyTel_0,
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel_0,
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
                },
                {
                    "partyName": party_partyTel_2,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_2,
                    "partyEmail": "",
                    "isCallOut": "1"
                },
                {
                    "partyName": party_partyTel_3,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_3,
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
        self.save_hostPasscode(str(now_hostPasscode) + "--4--" + str(times))
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res

    def create_Meeting_four(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2,
                            party_partyTel_3, party_partyTel_4, callOutType_custom, hangUpSetting, hangUpDuration,
                            isRecord, subscribeHostStatus, subscribeGuestStatus, contactName, contactTelephone,
                            contactEmail):

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
                    "partyName": party_partyTel_0,
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel_0,
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
                },
                {
                    "partyName": party_partyTel_2,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_2,
                    "partyEmail": "",
                    "isCallOut": "1"
                },
                {
                    "partyName": party_partyTel_3,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_3,
                    "partyEmail": "",
                    "isCallOut": "1"
                },
                {
                    "partyName": party_partyTel_4,
                    "partyType": "1",
                    "countryCode": "",
                    "partyTel": party_partyTel_4,
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
        self.save_hostPasscode(str(now_hostPasscode) + "--5--" + str(times))
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res
