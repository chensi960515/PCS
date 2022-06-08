#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: create_pcs_meeting.py
@time: 2022/6/1  2:16
"""

import logging
from pcs_package import PCS_createmeeing
from pcs_package import PCS_getToken
from tools import read_file

# 设置loggin.info 可控制台输出
logging.getLogger().setLevel(logging.INFO)

# 配置文件的路径,名称是固定的
ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meet_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)
meet = ya.get_data_list(meet_path)

excel_path = conf['parameter']['excelFile']

phone = ya.get_phone_excel(excelFile=excel_path, list_index=0)

pcs_token = PCS_getToken.Get_Token()
token = pcs_token.get_Token()





class Create_Pcs_Meeting:
    pcs_create = PCS_createmeeing.PCS_create()

    def create_pcs_test(self,token):

        start_phone = meet['meeting']['start_phone_test']
        end_phone = meet['meeting']['end_phone_test']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num_test']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            """
            if i > 0 and i <= 2:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=1, hangUpDuration=60,
                                              callOutType_custom=1,
                                              isRecord=2, subscribeHostStatus=0, subscribeGuestStatus=0, contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

            elif i > 2 and i <= 4:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

            elif i > 4 and i <= 7:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=0, hangUpDuration=0,
                                               callOutType_custom=6, isRecord=1,
                                               subscribeHostStatus=0, subscribeGuestStatus=3, contactName="陈思",
                                               contactTelephone="1662192683", contactEmail="si.chen@net263.com")
                del phone1[0:5]

            elif i > 7 and i <= 10:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=0, hangUpDuration=0,
                                               callOutType_custom=7, isRecord=1,
                                               subscribeHostStatus=3, subscribeGuestStatus=0, contactName="陈思",
                                               contactTelephone="16621292683", contactEmail="si.chen@net263.com")
                del phone1[0:5]
            elif i > 10:
                pcs_create.create_Meeting_thred(token=token, times=i, start_time=start_time,
                                                party_partyTel_0=phone1[i],
                                                party_partyTel_1=phone1[i + 1],
                                                party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                                party_partyTel_3=phone1[i + 3],
                                                callOutType_custom=4, isRecord=1,
                                                subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:5]

            """
            pcs_create.create_Meeting_thred(token=token, times=i, start_time=start_time,
                                            party_partyTel_0=phone1[i],
                                            party_partyTel_1=phone1[i + 1],
                                            party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                            party_partyTel_3=phone1[i + 3],
                                            callOutType_custom=1, isRecord=1,
                                            subscribeHostStatus=0, subscribeGuestStatus=0, contactName="",
                                            contactTelephone="", contactEmail="")
            del phone1[0:5]

    def create_pcs_batch_350(self, token):
        """
        350 场  批次一 + 批次二  各种场景
        :param token:
        :return:
        """

        start_phone = meet['meeting']['start_phone']
        end_phone = meet['meeting']['end_phone']
        phone_350 = phone[start_phone:end_phone]  # 100*3  20*3 50*5 50*5 39*3 20*5 20*5 50*3    1500
        meeting_sum = meet['Mode']['meeting_num']
        start_time = conf['parameter']['start_time']

        for i in range(meeting_sum + 1):
            if 0 < i <= 100:
                self.pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115700000,
                                                   party_partyTel_0=phone_350[i],
                                                   party_partyTel_1=phone_350[i + 1],
                                                   party_partyTel_2=phone_350[i + 2],
                                                   callOutType_custom=1,
                                                   isRecord=2)
                del phone_350[0:3]

            elif 100 < i <= 120:
                self.pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115700000,
                                                   party_partyTel_0=phone_350[i],
                                                   party_partyTel_1=phone_350[i + 1],
                                                   party_partyTel_2=phone_350[i + 2],
                                                   callOutType_custom=1)
                del phone_350[0:3]

            elif 120 < i <= 170:
                self.pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115700000,
                                                    party_partyTel_0=phone_350[i],
                                                    party_partyTel_1=phone_350[i + 1],
                                                    party_partyTel_2=phone_350[i + 2],
                                                    party_partyTel_3=phone_350[i + 3],
                                                    party_partyTel_4=phone_350[i + 4],
                                                    callOutType_custom=6
                                                    )
                del phone_350[0:5]

            elif 170 < i <= 220:
                self.pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115700000,
                                                    party_partyTel_0=phone_350[i],
                                                    party_partyTel_1=phone_350[i + 1],
                                                    party_partyTel_2=phone_350[i + 2],
                                                    party_partyTel_3=phone_350[i + 3],
                                                    party_partyTel_4=phone_350[i + 4],
                                                    callOutType_custom=7
                                                    )
                del phone_350[0:5]
            elif 220 < i <= 259:
                self.pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time + 180000,
                                                   party_partyTel_0=phone_350[i],
                                                   party_partyTel_1=phone_350[i + 1],
                                                   party_partyTel_2=phone_350[i + 2],
                                                   callOutType_custom=1)
                del phone_350[0:3]

            elif 259 < i <= 279:
                self.pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time + 180000,
                                                    party_partyTel_0=phone_350[i],
                                                    party_partyTel_1=phone_350[i + 1],
                                                    party_partyTel_2=phone_350[i + 2],
                                                    party_partyTel_3=phone_350[i + 3],
                                                    party_partyTel_4=phone_350[i + 4],
                                                    callOutType_custom=6)
                del phone_350[0:5]
            elif 279 < i <= 299:
                self.pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time + 180000,
                                                    party_partyTel_0=phone_350[i],
                                                    party_partyTel_1=phone_350[i + 1],
                                                    party_partyTel_2=phone_350[i + 2],
                                                    party_partyTel_3=phone_350[i + 3],
                                                    party_partyTel_4=phone_350[i + 4],
                                                    callOutType_custom=7)
                del phone_350[0:5]
            elif 299 < i:
                self.pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time + 180000,
                                                   party_partyTel_0=phone_350[i],
                                                   party_partyTel_1=phone_350[i + 1],
                                                   party_partyTel_2=phone_350[i + 2],
                                                   callOutType_custom=4)
                del phone_350[0:3]

    def create_pcs_batch_350_2(self, token):
        """
        350 场,只有场景6  每场4人入会
        :param token:
        :return:
        """

        start_phone = meet['meeting']['start_phone']
        end_phone = meet['meeting']['end_phone']
        phone1 = phone[start_phone:end_phone]  # 350*4
        meeting_sum = meet['Mode']['meeting_num']
        start_time = conf['parameter']['start_time']

        for i in range(meeting_sum + 1):
            if 0 < i <= 220:
                self.pcs_create.create_Meeting_thred(token=token, times=i, start_time=start_time,
                                                     party_partyTel_0=phone1[i],
                                                     party_partyTel_1=phone1[i + 1],
                                                     party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                                     callOutType_custom=6)
                del phone1[0:4]

            elif 220 < i:
                self.pcs_create.create_Meeting_thred(token=token, times=i, start_time=start_time + 180000,
                                                     party_partyTel_0=phone1[i],
                                                     party_partyTel_1=phone1[i + 1],
                                                     party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                                     callOutType_custom=6)
                del phone1[0:5]

    def create_pcs_batch_650(self, token):

        start_phone = meet['meeting']['start_phone_650']
        end_phone = meet['meeting']['end_phone_650']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num_650']  # 600* 2  50 *2
        start_time = conf['parameter']['start_time_650']

        for i in range(meeting_sum + 1):
            if 0 < i <= 100:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=1)
                del phone1[0:2]

            elif 100 < i <= 150:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=6)
                del phone1[0:2]

            elif 150 < i <= 200:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=7)
                del phone1[0:2]

            elif 200 < i <= 300:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 180000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=1)
                del phone1[0:2]

            elif 300 < i <= 350:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 180000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=6)
                del phone1[0:2]

            elif 350 < i <= 400:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 180000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=7)
                del phone1[0:2]

            elif 400 < i <= 500:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 360000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=1)
                del phone1[0:2]

            elif 500 < i <= 550:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 360000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=6)
                del phone1[0:2]

            elif 550 < i <= 600:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 360000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=7)
                del phone1[0:2]

            elif 600 < i <= 625:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 540000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=6)
            elif 625 < i <= 650:
                self.pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time + 540000,
                                                   party_partyTel_0=phone1[i],
                                                   party_partyTel_1=phone1[i + 1],
                                                   callOutType_custom=7)


pcs_token = PCS_getToken.Get_Token()
token = pcs_token.get_Token()

cpm = Create_Pcs_Meeting()



#cpm.create_pcs_test(token)

# cpm.create_pcs_batch_350(token)

# cpm.create_pcs_batch_350_2(token)

# cpm.create_pcs_batch_650(token)
