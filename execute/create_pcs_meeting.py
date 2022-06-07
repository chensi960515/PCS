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


class Create_Pcs_Meeting():

    def create_pcs_test(self, token):

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
                                            callOutType_custom=4, isRecord=1,
                                            subscribeHostStatus=0, subscribeGuestStatus=0, contactName="",
                                            contactTelephone="", contactEmail="")
            del phone1[0:5]


    def create_pcs_batch_1(self, token):

        start_phone = meet['meeting']['start_phone_1']
        end_phone = meet['meeting']['end_phone_1']
        phone1 = phone[start_phone:end_phone]  # 220 + 120*3 + 100*5
        meeting_sum = meet['Mode']['meeting_num1']
#        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 100:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115700000,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=2, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

            elif i > 100 and i <= 120:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115700000,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

            elif i > 120 and i <= 170:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115700000,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=1, hangUpDuration=60,
                                               callOutType_custom=6, isRecord=1,
                                               subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:5]

            elif i > 170 and i <= 220:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115700000,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=1, hangUpDuration=60,
                                               callOutType_custom=7, isRecord=1,
                                               subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:5]

    def create_pcs_batch_2(self, token):

        start_phone = meet['meeting']['start_phone_2']
        end_phone = meet['meeting']['end_phone_2']
        phone1 = phone[start_phone:end_phone]  # 220 + 120*3 + 100*5
        meeting_sum = meet['Mode']['meeting_num2']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 39:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115880000,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

            elif i > 39 and i <= 59:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115880000,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=0, hangUpDuration=0,
                                               callOutType_custom=6, isRecord=1,
                                               subscribeHostStatus=0, subscribeGuestStatus=3, contactName="陈旭",
                                               contactTelephone="13391619661", contactEmail="xu.chen1@net263.com")
                del phone1[0:5]

            elif i > 59 and i <= 79:
                pcs_create.create_Meeting_four(token=token, times=i, start_time=1654115880000,
                                               party_partyTel_0=phone1[i],
                                               party_partyTel_1=phone1[i + 1],
                                               party_partyTel_2=phone1[i + 2], party_partyTel_3=phone1[i + 3],
                                               party_partyTel_4=phone1[i + 4], hangUpSetting=0, hangUpDuration=0,
                                               callOutType_custom=7, isRecord=1,
                                               subscribeHostStatus=3, subscribeGuestStatus=3, contactName="陈旭",
                                               contactTelephone="13391619661", contactEmail="xu.chen1@net263.com")
                del phone1[0:5]

            elif i > 79 and i <= 129:
                pcs_create.create_Meeting_two(token=token, times=i, start_time=1654115880000,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1],
                                              party_partyTel_2=phone1[i + 2], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=4,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:3]

    def create_pcs_batch_3(self, token):

        start_phone = meet['meeting']['start_phone_3']
        end_phone = meet['meeting']['end_phone_3']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num3']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 100:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 100 and i <= 150:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=6, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 150 and i <= 200:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=7, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

    def create_pcs_batch_4(self, token):

        start_phone = meet['meeting']['start_phone_4']
        end_phone = meet['meeting']['end_phone_4']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num4']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 100:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 100 and i <= 150:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=6, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 150 and i <= 200:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=7, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

    def create_pcs_batch_5(self, token):

        start_phone = meet['meeting']['start_phone_5']
        end_phone = meet['meeting']['end_phone_5']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num5']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 100:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 100 and i <= 150:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=6, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 150 and i <= 200:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=6, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

    def create_pcs_batch_6(self, token):

        start_phone = meet['meeting']['start_phone_6']
        end_phone = meet['meeting']['end_phone_6']
        phone1 = phone[start_phone:end_phone]
        meeting_sum = meet['Mode']['meeting_num6']
        start_time = conf['parameter']['start_time']

        pcs_create = PCS_createmeeing.PCS_create()

        for i in range(meeting_sum + 1):
            if i > 0 and i <= 20:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=1,
                                              isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 20 and i <= 35:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=6, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]

            elif i > 35 and i <= 50:
                pcs_create.create_Meeting_one(token=token, times=i, start_time=start_time,
                                              party_partyTel_0=phone1[i],
                                              party_partyTel_1=phone1[i + 1], hangUpSetting=0, hangUpDuration=0,
                                              callOutType_custom=7, isRecord=1,
                                              subscribeHostStatus=0, subscribeGuestStatus=0,contactName="",
                                              contactTelephone="", contactEmail="")
                del phone1[0:2]


pcs_token = PCS_getToken.Get_Token()
token = pcs_token.get_Token()

cpm = Create_Pcs_Meeting()

cpm.create_pcs_test(token)



# cpm.create_pcs_batch_1(token)

# cpm.create_pcs_batch_2(token)

# cpm.create_pcs_batch_3(token)

# cpm.create_pcs_batch_4(token)

# cpm.create_pcs_batch_5(token)

# cpm.create_pcs_batch_6(token)
