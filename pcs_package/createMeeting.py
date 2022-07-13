# -*- coding: utf-8 -*-
# @Time : 2022/7/13 10:23
# @Author : chensi
# @File : createMeeting.py
# @Project : PCS


import requests
import json
import time
import random
import string
from tools import DemoLogger
from tools import read_file
from pcs_package import PCS_getToken
from tools import sava_info

logging = DemoLogger()

ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meeting_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)
meeting = ya.get_data_list(meeting_path)
url_scp_token = conf['parameter']['url_scp_token']
url_sec_token = conf['parameter']['url_sec_token']

Token = PCS_getToken.Get_Token()
scp_token = Token.get_Token(url_scp_token)
sec_token = Token.get_Token(url_sec_token)


class create:
    list_meetingId = []

    # 电话列表
    party_partyTel = []

    # 参数提取出来,便于控制
    meetingID_path = "../eph_data/meetingID.txt"
    hostPasscode_path = "../eph_data/hostPasscode.txt"
    meetingCode_path = "../eph_data/meetingCode.txt"

    def generate_random_str(self, randomlength):
        '''
        string.digits = 0123456789
        string.ascii_letters = 26个小写,26个大写
        '''
        str_list = random.sample(string.digits + string.ascii_letters, randomlength)
        random_str = ''.join(str_list)
        return random_str


    def setUserInfo(self, request_type: str, party_partyTel: list, counsellor: int):
        """
        分配 每场会议顾问和客户的虚拟接入号
        :param request_type: 区分scp 和 sec
        :param party_partyTel:  每场会议中,所用到的接入号
        :param counsellor:  顾问数量
        :return:
        """
        partyList = []
        user_sum = len(party_partyTel)
        counsellor_num = counsellor
        user_num = user_sum - counsellor_num

        if request_type.lower() == "scp":
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
        elif request_type.lower() == "sec":
            partyList.append({
                "partyName": "主持人-" + str(party_partyTel[0]),
                "partyType": "HOST",
                "phoneNumber": str(party_partyTel[0]),
                "partyEmail": ""
            })
            for i in range(user_num):
                partyList.append({
                    "partyName": party_partyTel[i + 1],
                    "partyType": "GUEST",
                    "phoneNumber": party_partyTel[i + 1],
                    "partyEmail": ""

                })
            return partyList
        else:
            logging.logger.error("参数异常")

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
                logging.logger.info("==========接入号足够,正常分配==========")
                partyTel = party_partyTel[:(counsellor_num + user_num) * meeting_num]
            # 不够,无余 不切,全部分配
            elif creat_num < meeting_num and del_num == 0:
                logging.logger.info("==========接入号不足1,只能分配" + str(creat_num) + "场会议==========")
                partyTel = party_partyTel
            # 不够,有余 剩余全删,再分配
            elif creat_num < meeting_num and del_num > 0:
                logging.logger.info("==========接入号不足2,只能分配" + str(creat_num) + "场会议==========")
                partyTel = party_partyTel[:-del_num]

            if type(counsellor_num) is int and 0 < counsellor_num <= 3:
                for i in range(0, len(partyTel), counsellor_num + user_num):
                    single_meeting_list.append(partyTel[i: i + counsellor_num + user_num])
                return single_meeting_list
            elif counsellor_num == 0:
                logging.logger.error("==========会议必须存在一个顾问===========")
            elif counsellor_num > 3:
                logging.logger.error("==========每场会议中,顾问人数不可超过3人===========")
            else:
                logging.logger.error("==========counsellor_num参数错误===========")

        except Exception as e:
            logging.logger.error(e)

    def create_Request(self, method, url, headers, data):
        response = requests.request(method=method, url=url, headers=headers, data=json.dumps(data))
        res = json.loads(response.text)
        if res['msg'] == 'success' and res['code'] == 0:
            return res
        else:
            logging.logger.info(json.dumps(data))
            logging.logger.info(res)

    def create_Meeting(self, request_type: str, param: dict, party_partyTel: list, counsellor_num, user_num,
                       meeting_num):
        """
        组装 参数
        请求
        :param request_type:
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

            if request_type.lower() == "scp":
                data['token'] = scp_token
                data['meetingTitle'] = "共" + str(meeting_num) + "场-场景" + str(data['callOutType']) + "-人数" + str(
                    counsellor_num + user_num)
                url = conf['parameter']['url_create_Meeting']
                headers = conf['parameter']['headers']

                if type(counsellor_num) is int and counsellor_num > 0:
                    for i in range(len(party_partyTel)):
                        data['partyList'] = self.setUserInfo(request_type,party_partyTel[i], counsellor_num)
                        data['userAccount'] = conf['parameter']['userAccount']
                        res = self.create_Request('POST',url,headers,data)
                        meetingId = res['data']['meetingId']
                        hostPasscode = res['data']['hostPasscode']
                        sava_info.save_Meeting_Info(self.meetingID_path, meetingId)
                        sava_info.save_Meeting_Info(self.hostPasscode_path, hostPasscode)

                elif counsellor_num == 0:
                    logging.logger.error("==========会议必须存在一个顾问===========")
                else:
                    logging.logger.error("==========counsellor_num参数错误===========")

            elif request_type.lower() == "sec":
                data['token'] = sec_token
                data['userAccount'] = conf['parameter']['userAccount']
                data['meetingTitle'] = "畅听会议,人数" + str(counsellor_num + user_num)
                url = conf['parameter']['url_sec_createMeeting']
                headers = conf['parameter']['headers']
                if type(counsellor_num) is int and counsellor_num == 1:
                    for i in range(len(party_partyTel)):
                        data['meetingCode'] = self.generate_random_str(12)
                        data['partyList'] = self.setUserInfo(request_type,party_partyTel[i], counsellor_num)
                        res = self.create_Request('POST',url,headers,data)
                        sava_info.save_Meeting_Info(self.meetingCode_path, data['meetingCode'])
                        logging.logger.info(res)
                elif counsellor_num == 0:
                    logging.logger.error("==========会议必须存在一个主持人===========")
                else:
                    logging.logger.error("==========参数异常===========")

            else:
                logging.logger.error("出现异常,请查看")
        except Exception as e:
            logging.logger.info(e)
