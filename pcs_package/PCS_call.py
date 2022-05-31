#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: PCS_call.py
@time: 2022/5/30  23:34
"""
import json

"""
    主动外呼客户
    
"""

import requests
import logging
from tools import read_file

logging.getLogger().setLevel(logging.INFO)
logging.Formatter("%(lineno)d")

list_hostPasscode = []
data_parties = []
user_dict = {"name":"","phone":"","role":""}


ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)


class Call():


    def get_hostPasscode(self):
        with open('../eph_data/custom_4_hostPasscode.txt', 'r', encoding='utf-8') as f:
            for x in f:
                list_hostPasscode.append(x[0:9])


    def  query_meetingInfo(self,hostPasscode):

        url = conf["parameter"]["url_query_Meeting"] + str(hostPasscode)
        payload = {}
        headers = {
            'Content-Type' : conf["parameter"]["Content-Type-json"],
            'cookie': conf["parameter"]["cookie"]
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        data_parties = res['parties']

        for i in range(len(data_parties)):
            user_info = []
            if data_parties[i]["role"] != 'g':
                user_dict["name"] = data_parties[i]["name"]
                user_dict["phone"] = data_parties[i]["phone"]
                user_dict["role"] = data_parties[i]["role"]
                user_info.append({'name': user_dict["name"], 'phone': user_dict["phone"], 'role': user_dict["role"]})
#            logging.info(user_dict)
            self.callParty(hostPasscode,user_info)


    def callParty(self,hostPasscode,user_info):
        url = conf["parameter"]["url_callParty"]

        payload = {"hostPasscode": hostPasscode,
                   "parties": str(user_info)
        }

        files = []
        headers = {
            'Content-Type' : conf["parameter"]["Content-Type-form-data"],
            'cookie': conf["parameter"]["cookie"]
        }
        if len(payload["parties"]) != 0:
            requests.request("POST", url, headers=headers, data=payload, files=files)
            logging.info(payload)

call = Call()
call.get_hostPasscode()

for i in range(len(list_hostPasscode)):
    call.query_meetingInfo(list_hostPasscode[i])
