# -*- coding: utf-8 -*-
# @Time : 2022/5/20 17:06
# @Author : chensi
# @File : PCS_createmeeing.py
# @Project : CVATest

import requests
import json
import time
import xlrd
import logging
from tools import read_file


logging.getLogger().setLevel(logging.INFO)

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)

class PCS_create():

    list_meetingId = []


    def save_meetingID(self,x):
        with open('../eph_data/meetingID.txt', 'a', encoding='utf-8') as f:
            f.write(str(x))
            f.write("\n")
        with open('../eph_data/meetingID.txt', 'r', encoding='utf-8') as f:
            x = f.read()

    def save_hostPasscode(self,z):
        with open('../eph_data/hostPasscode.txt', 'a', encoding='utf-8') as f:
            f.write(str(z))
            f.write("\n")
        with open('../eph_data/hostPasscode.txt', 'r', encoding='utf-8') as f:
            z = f.read()

    def save_4_hostPasscode(self,k):
        with open('../eph_data/custom_4_hostPasscode.txt', 'a', encoding='utf-8') as f:
            f.write(str(k))
            f.write("\n")
        with open('../eph_data/custom_4_hostPasscode.txt', 'r', encoding='utf-8') as f:
            k = f.read()

    def create_Meeting_one(self, token, times, start_time, party_partyTel_0, party_partyTel_1, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus):

        url = conf['parameter']['url_create_Meeting']

        payload_client_one = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle": "No." + str(times) + "-场景"+ str(callOutType_custom)  +"-录"+ str(isRecord) +"-客"+ str(subscribeHostStatus)+"-顾"+ str(subscribeGuestStatus) ,
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
                    "contactName": "紧急联络人列表",
                    "contactTelephone": "16621292683",
                    "contactEmail": "test@net263.com"
                }
            ],
            "callOutType": callOutType_custom,
            "isRecord": isRecord,
            "joinType": 1,
            "meetingExplain": "倾听,类型:" + str(callOutType_custom),
            "subscribeHostStatus": subscribeHostStatus,
            "subscribeGuestStatus": subscribeGuestStatus
        })
        headers = conf['parameter']['headers']

        response = requests.request("POST", url, headers=headers, data=payload_client_one)
        logging.info(response.text)
        res = json.loads(response.text)
        self.now_meetingId = res['data']['meetingId']
        self.save_meetingID(self.now_meetingId)
        self.now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(self.now_hostPasscode)
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return res


    def create_Meeting_two(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus):

        url = conf['parameter']['url_create_Meeting']
        payload_client_two = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle": "No." + str(times) + "-场景"+ str(callOutType_custom)  +"-录"+ str(isRecord) +"-客"+ str(subscribeHostStatus)+"-顾"+ str(subscribeGuestStatus) ,
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
                    "contactName": "紧急联络人列表",
                    "contactTelephone": "16621292683",
                    "contactEmail": "test@net263.com"
                }
            ],
            "callOutType": callOutType_custom,
            "isRecord": isRecord,
            "joinType": 1,
            "meetingExplain": "倾听,类型:" + str(callOutType_custom),
            "subscribeHostStatus": subscribeHostStatus,
            "subscribeGuestStatus": subscribeGuestStatus
        })
        headers = conf['parameter']['headers']

        response = requests.request("POST", url, headers=headers, data=payload_client_two)
        logging.info(response.text)
        res = json.loads(response.text)
        now_meetingId = res['data']['meetingId']
        self.save_meetingID(now_meetingId)
        now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(now_hostPasscode)
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return  res


    def create_Meeting_thred(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus):

        url = conf['parameter']['url_create_Meeting']
        payload_client_two = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle": "No." + str(times) + "-场景"+ str(callOutType_custom)  +"-录"+ str(isRecord) +"-客"+ str(subscribeHostStatus)+"-顾"+ str(subscribeGuestStatus) ,
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
                    "contactName": "紧急联络人列表",
                    "contactTelephone": "16621292683",
                    "contactEmail": "test@net263.com"
                }
            ],
            "callOutType": callOutType_custom,
            "isRecord": isRecord,
            "joinType": 1,
            "meetingExplain": "倾听,类型:" + str(callOutType_custom),
            "subscribeHostStatus": subscribeHostStatus,
            "subscribeGuestStatus": subscribeGuestStatus
        })
        headers = conf['parameter']['headers']

        response = requests.request("POST", url, headers=headers, data=payload_client_two)
        logging.info(response.text)
        res = json.loads(response.text)
        now_meetingId = res['data']['meetingId']
        self.save_meetingID(now_meetingId)
        now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(now_hostPasscode)
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return  res


    def create_Meeting_four(self, token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3, party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus):

        url = conf['parameter']['url_create_Meeting']
        payload_client_two = json.dumps({
            "token": token,
            "userAccount": conf['parameter']['userAccount'],
            "meetingTitle":"No." + str(times) + "-场景"+ str(callOutType_custom)  +"-录"+ str(isRecord) +"-客"+ str(subscribeHostStatus)+"-顾"+ str(subscribeGuestStatus) ,
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
                    "contactName": "紧急联络人列表",
                    "contactTelephone": "16621292683",
                    "contactEmail": "test@net263.com"
                }
            ],
            "callOutType": callOutType_custom,
            "isRecord": isRecord,
            "joinType": 1,
            "meetingExplain": "倾听,类型:" + str(callOutType_custom),
            "subscribeHostStatus": subscribeHostStatus,
            "subscribeGuestStatus": subscribeGuestStatus
        })
        headers = conf['parameter']['headers']

        response = requests.request("POST", url, headers=headers, data=payload_client_two)
        logging.info(response.text)
        res = json.loads(response.text)
        now_meetingId = res['data']['meetingId']
        self.save_meetingID(now_meetingId)
        now_hostPasscode = res['data']['hostPasscode']
        self.save_hostPasscode(now_hostPasscode)
        if callOutType_custom == 4:
            custom_4_hostPasscode = res['data']['hostPasscode']
            self.save_4_hostPasscode(custom_4_hostPasscode)
        return  res


    def create_Meeting(self, meeting_num, user_num,token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3, party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus):
        if user_num == 1:
            logging.error("不给咨询客户信息的吗? 那你手动创建吧")
            return
        elif user_num == 2:
            for i in range(meeting_num+1):
                self.create_Meeting_one(token, start_time, party_partyTel_0, party_partyTel_1, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus, times=i)
        elif user_num == 3:
            for i in range(meeting_num+1):
                self.create_Meeting_two(token, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus, times=i)
        elif user_num == 4:
            for i in range(meeting_num+1):
                self.create_Meeting_thred(token, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus, times=i)
        elif user_num == 5:
            for i in range(meeting_num + 1):
                self.create_Meeting_four(token, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3, party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus, times=i)
        else:
            logging.error("现在不支持创建 "+ user_num +"人的会议,后续可优化")


"""

PCS = PCS_createmeeting()
token = PCS.get_Token()


excelFile = conf['parameter']['excelFile']
res_guwen = PCS.read_xlrd(excelFile=excelFile, list_index=0)
res_user1 = PCS.read_xlrd(excelFile=excelFile, list_index=1)
res_user2 = PCS.read_xlrd(excelFile=excelFile, list_index=2)
res_user3 = PCS.read_xlrd(excelFile=excelFile, list_index=3)
res_false = PCS.read_xlrd(excelFile=excelFile, list_index=4)



ttime = conf['parameter']['start_time']
num = conf['parameter']['num']
step = conf['parameter']['step']

for i in range(0, num+1) :
    if i > 0 and i<= step:
        PCS.create_Meeting_one(token=token, times=i, start_time=ttime, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], callOutType_custom='1')
    elif i > step and i<= 2*step:

        PCS.create_Meeting_two(token=token, times=i, start_time=ttime, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_user2[i-2], callOutType_custom='6')
    elif i > 2*step and i <= 3*step:
        PCS.create_Meeting_two(token=token, times=i, start_time=ttime, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_false[i - 4], callOutType_custom='7')
    elif i > 3*step:
        res = PCS.create_Meeting_two(token=token, times=i, start_time=ttime, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_user3[i-6], callOutType_custom='4')
        custom_4_hostPasscode = res['data']['hostPasscode']
        PCS.save_4_hostPasscode(custom_4_hostPasscode)

"""
