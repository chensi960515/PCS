#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: PCS_call.py
@time: 2022/5/30  23:34
"""
import json
import time
import PCS_getcallphone
from tools import DemoLogger
import requests
from tools import read_file

log = DemoLogger().logger
list_hostPasscode = []
data_parties = []
user_dict = {"name": "", "phone": "", "role": ""}

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)

passcode = PCS_getcallphone.get_passcode()


class Call:

    # 获取会议详情信息 得user_info  用户外呼和挂断
    def query_meetingInfo(self, hostPasscode):
        """
        获取会议信息方法中,获取一次,直接请求外呼一次,后续调用无需再调用callParty方法
        :param hostPasscode:
        :return:
        """
        user_info = []
        url = conf["parameter"]["url_query_Meeting"] + str(hostPasscode)
        payload = {}
        headers = {
            'Content-Type': conf["parameter"]["Content-Type-json"],
            'cookie': conf["parameter"]["cookie"]
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        if res['status'] == 403:
            log.error("检查下配置文件中的cookie,是否过期")
        else:
            try:
                data_parties = res['parties']
            except Exception as e:
                log.error(e)

        try:
            # 提取外呼所需参数
            for i in range(len(data_parties)):
                # 只外呼咨询客户,剔除顾问 g
                if data_parties[i]["role"] != 'g':
                    user_dict["name"] = data_parties[i]["name"]
                    user_dict["phone"] = data_parties[i]["phone"]
                    user_dict["role"] = data_parties[i]["role"]
                    user_info.append(
                        {'name': user_dict["name"], 'phone': user_dict["phone"], 'role': user_dict["role"]})
        except  Exception as e:
            log.error(e)
        # log.info(user_info)
        return user_info

    def request_Party(self, url, passcode_path, callOutType_custom,
                      callOutType_custom_index,
                      str_start, str_end):
        files = []
        headers = {
            'Content-Type': conf["parameter"]["Content-Type-form-data"],
            'cookie': conf["parameter"]["cookie"]
        }

        hostPasscode_list = passcode.get_call_phone_passcode(passcode_path=passcode_path,
                                                             callOutType_custom=callOutType_custom,
                                                             callOutType_custom_index=callOutType_custom_index,
                                                             str_start=str_start,
                                                             str_end=str_end)
        for i in range(len(hostPasscode_list)):
            parties_list = self.query_meetingInfo(hostPasscode_list[i])
            for j in range(len(parties_list)):
                parties_one = [parties_list[j]]
                payload = {"hostPasscode": hostPasscode_list[i],
                           "parties": str(parties_one)
                           }
                if len(payload["parties"]) != 0:
                    time.sleep(1)
                    log.info(payload)
                    res = requests.request("POST", url, headers=headers, data=payload, files=files)
                    log.info(res.text)

    def callParty(self, passcode_path="../eph_data/hostPasscode.txt", callOutType_custom=4,
                  callOutType_custom_index=12,
                  str_start=0, str_end=9):
        url = conf["parameter"]["url_callParty"]
        self.request_Party(url=url, passcode_path=passcode_path, callOutType_custom=callOutType_custom,
                           callOutType_custom_index=callOutType_custom_index,
                           str_start=str_start, str_end=str_end)

    def end_callParty(self, passcode_path="../eph_data/hostPasscode.txt", callOutType_custom=4,
                      callOutType_custom_index=12,
                      str_start=0, str_end=9):
        url = conf["parameter"]["url_endcallParty"]
        self.request_Party(url=url, passcode_path=passcode_path, callOutType_custom=callOutType_custom,
                           callOutType_custom_index=callOutType_custom_index,
                           str_start=str_start, str_end=str_end)

# call = Call()

# call.callParty(passcode_path='../eph_data/custom_4_hostPasscode.txt', str_start=0, str_end=9)

# call.end_callParty(passcode_path='../eph_data/custom_4_hostPasscode.txt', str_start=0, str_end=9)
