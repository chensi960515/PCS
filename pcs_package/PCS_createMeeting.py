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
from pcs_package import PCS_getToken
from tools import sava_info

logging.getLogger().setLevel(logging.INFO)

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meeting_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)
meeting = ya.get_data_list(meeting_path)

Token = PCS_getToken.Get_Token()
token = Token.get_Token()


class PCS_create:
    list_meetingId = []
    # 电话列表
    party_partyTel = []

    # 参数提取出来,便于控制
    create_data = meeting['data']

    def setUserInfo(self, party_partyTel: list, counsellor: int):
        """
        分配 每场会议顾问和客户的虚拟接入号
        :param party_partyTel:  每场会议中,所用到的接入号
        :param counsellor:  顾问数量
        :return:
        """
        partyList = []
        user_sum = len(party_partyTel) + 1
        counsellor_num = counsellor
        user_num = user_sum - counsellor_num

        for i in range(user_sum):
            if i < counsellor_num:
                partyList.append({
                    "partyName": party_partyTel[i],
                    "partyType": "0",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel[i],
                    "partyEmail": "",
                    "isCallOut": "1"
                })
            elif counsellor_num <= i < user_num:
                partyList.append({
                    "partyName": party_partyTel[i],
                    "partyType": "1",
                    "countryCode": "",
                    "areaCode": "",
                    "partyTel": party_partyTel[i],
                    "partyEmail": "",
                    "isCallOut": "1"
                })

        return partyList

    def single_meeting_partyTel(self, party_partyTel: list, counsellor_num: int, user_num: int, meeting_num: int):
        """
        切割 虚拟接入号,为每场会议进行分配
        :param party_partyTel:
        :param counsellor_num:
        :param user_num:
        :param meeting_num:
        :return:
        """
        try:
            single_meeting_list = []
            partyTel = []
            del_num = len(party_partyTel) % (counsellor_num + user_num)
            creat_num = int(len(party_partyTel) / (counsellor_num + user_num))
            # 足够  不管是否有余,直接切
            if creat_num >= meeting_num:
                logging.info("==========接入号足够,正常分配==========")
                partyTel = party_partyTel[:(counsellor_num + user_num) * meeting_num]
            # 不够,无余 不切,全部分配
            elif creat_num < meeting_num and del_num == 0:
                logging.info("==========接入号不足1,只能分配" + str(creat_num) + "场会议==========")
                partyTel = party_partyTel
            # 不够,有余 剩余全删,再分配
            elif creat_num < meeting_num and del_num > 0:
                logging.info("==========接入号不足2,只能分配" + str(creat_num) + "场会议==========")
                partyTel = party_partyTel[:-del_num]

            if type(counsellor_num) is int and 0 < counsellor_num <= 3:
                for i in range(0, len(partyTel), counsellor_num + user_num):
                    single_meeting_list.append(partyTel[i: i + counsellor_num + user_num])
                return single_meeting_list
            elif counsellor_num == 0:
                logging.error("==========会议必须存在一个顾问===========")
            elif counsellor_num > 3:
                logging.error("==========每场会议中,顾问人数不可超过3人===========")
            else:
                logging.error("==========counsellor_num参数错误===========")
        except Exception as e:
            logging.error(e)

    def create_Meeting(self, param: dict, party_partyTel: list, counsellor_num, user_num, meeting_num):
        """
        组装 参数
        请求
        :param meeting_num:
        :param param:
        :param party_partyTel:  需要使用的电话列表(只对每一场会议来说的)
        :param counsellor_num:  需要创建的顾问数量(一场会议中)
        :param user_num:
        :return:
        """

        try:
            party_partyTel = self.single_meeting_partyTel(party_partyTel=party_partyTel, counsellor_num=counsellor_num,
                                                          user_num=user_num, meeting_num=meeting_num)
            data = param
            data['token'] = token
            data['meetingTitle'] = "No." + "场景" + str(data['callOutType']) + "人数" + str(
                len(party_partyTel))
            url = conf['parameter']['url_create_Meeting']
            headers = conf['parameter']['headers']

            if type(counsellor_num) is int and counsellor_num > 0:
                for i in range(len(party_partyTel)):
                    data['partyList'] = self.setUserInfo(party_partyTel[i], counsellor_num)
                    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
                    res = json.loads(response.text)
                    if res['msg'] == 'success' and res['code'] == 0:
                        logging.info(res)
                        meetingId = res['data']['meetingId']
                        hostPasscode = res['data']['hostPasscode']
                        sava_info.save_Meeting_Info('../eph_data/meetingID.txt', meetingId)
                        sava_info.save_Meeting_Info('../eph_data/hostPasscode.txt', hostPasscode)

                    else:
                        logging.info(json.dumps(data))
                        logging.info(res)

            elif counsellor_num == 0:
                logging.error("==========会议必须存在一个顾问===========")
            else:
                logging.error("==========counsellor_num参数错误===========")

        except Exception as e:
            logging.error(e)
