# -*- coding: utf-8 -*-
# @Time : 2022/5/31 15:50
# @Author : chensi
# @File : create_Meeting.py
# @Project : PCS


# 后续完善通用方法,暂时放弃

import logging
from tools import read_file
from pcs_package import PCS_getToken, PCS_createmeeing

# 设置loggin.info 可控制台输出
logging.getLogger().setLevel(logging.INFO)

# 配置文件的路径,名称是固定的
ya = read_file.GetData()
conf_path = f"../config/config.yaml"
conf = ya.get_data_list(conf_path)

excel_path = conf['parameter']['excelFile']

phone = ya.get_phone_excel(excelFile=excel_path, list_index=0)

phone1 = phone[0:1100]  # 220 + 120*3 + 100*5
phone2 = phone[1100:1700]
phone3 = phone[1700:2300]
phone4 = phone[2300:2900]
phone5 = phone[2900:-1]

# token, times, start_time, party_partyTel_0, party_partyTel_1, party_partyTel_2, party_partyTel_3,
# party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus

meeting_sum = conf['Mode']['num']
callOutType_1_scene_A = conf['Mode']['callOutType_1_num']['scene_A']
callOutType_1_scene_B = conf['Mode']['callOutType_1_num']['scene_B']
callOutType_1_sum = callOutType_1_scene_A + callOutType_1_scene_B
user_num_1_A = conf['Mode']['callOutType_1_num']['user_num_A']
user_num_1_B = conf['Mode']['callOutType_1_num']['user_num_B']

callOutType_4_scene_A = conf['Mode']['callOutType_4_num']['scene_A']
callOutType_4_scene_B = conf['Mode']['callOutType_4_num']['scene_B']
callOutType_4_sum = callOutType_4_scene_A + callOutType_4_scene_B
user_num_4_A = conf['Mode']['callOutType_4_num']['user_num_A']
user_num_4_B = conf['Mode']['callOutType_4_num']['user_num_B']

callOutType_6_scene_A = conf['Mode']['callOutType_6_num']['scene_A']
callOutType_6_scene_B = conf['Mode']['callOutType_6_num']['scene_B']
callOutType_6_sum = callOutType_6_scene_A + callOutType_6_scene_B
user_num_6_A = conf['Mode']['callOutType_6_num']['user_num_A']
user_num_6_B = conf['Mode']['callOutType_6_num']['user_num_B']

callOutType_7_scene_A = conf['Mode']['callOutType_7_num']['scene_A']
callOutType_7_scene_B = conf['Mode']['callOutType_7_num']['scene_B']
callOutType_7_sum = callOutType_7_scene_A + callOutType_7_scene_B
user_num_7_A = conf['Mode']['callOutType_7_num']['user_num_A']
user_num_7_B = conf['Mode']['callOutType_7_num']['user_num_B']

start_time = conf['parameter']['start_time']

pcs_create = PCS_createmeeing()

pcs_token = PCS_getToken.Get_Token()
token = pcs_token.get_Token()

now_phone = phone1

for i in range(meeting_sum):
    if i > 0 and i <= 100:
        pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                      party_partyTel_1=now_phone[i + 1],
                                      party_partyTel_2=now_phone[i + 2], callOutType_custom=1,
                                      isRecord=2, subscribeHostStatus=0, subscribeGuestStatus=0)
        del now_phone[0:2]
    elif i > 100 and i <= 120:
        pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                      party_partyTel_1=now_phone[i + 1],
                                      party_partyTel_2=now_phone[i + 2], callOutType_custom=1,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
        del now_phone[0:2]

    elif i >120 and i <= 170:
        pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                       party_partyTel_1=now_phone[i + 1],
                                       party_partyTel_2=now_phone[i + 2], party_partyTel_3=now_phone[i + 3],
                                       party_partyTel_4=now_phone[i + 4], callOutType_custom=6, isRecord=1,
                                       subscribeHostStatus=0, subscribeGuestStatus=3)
        del now_phone[0:4]
    elif i >170 and i <= 220 :
        pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                       party_partyTel_1=now_phone[i + 1],
                                       party_partyTel_2=now_phone[i + 2], party_partyTel_3=now_phone[i + 3],
                                       party_partyTel_4=now_phone[i + 4], callOutType_custom=6, isRecord=1,
                                       subscribeHostStatus=3, subscribeGuestStatus=0)
        del now_phone[0:4]









"""
for i in range(meeting_sum + 1):

    if i > 0 and i <= callOutType_1_scene_A and callOutType_1_scene_A !=0:
        if user_num_1_A == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                      party_partyTel_1=now_phone[i+1],
                                      party_partyTel_2=now_phone[i+2], callOutType_custom=1,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_1_A == 3:
            pass
            #del now_phone[i:i + 3]


    elif i > callOutType_1_scene_A and i <= callOutType_1_sum and callOutType_1_scene_B !=0:
        if user_num_1_B == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                      party_partyTel_1=now_phone[i+1],
                                      party_partyTel_2=now_phone[i+2], callOutType_custom=1,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_1_B ==3 :
            pass
        else:
            logging.error("没有")

    elif i > callOutType_1_sum and i <= callOutType_1_sum + callOutType_4_scene_A and callOutType_4_scene_A !=0:
        pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=phone1[i],
                                      party_partyTel_1=phone1[meeting_sum + i],
                                      party_partyTel_2=phone1[2 * meeting_sum + i], callOutType_custom=1,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)

    elif i > callOutType_1_sum + callOutType_4_scene_A and i <= callOutType_1_sum + callOutType_4_sum and callOutType_4_scene_B != 0:
        pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=phone1[i],
                                      party_partyTel_1=phone1[meeting_sum + i],
                                      party_partyTel_2=phone1[2 * meeting_sum + i], callOutType_custom=1,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)

    elif i > callOutType_1_sum + callOutType_4_sum and i <= callOutType_1_sum + callOutType_4_sum + callOutType_6_scene_A and callOutType_6_scene_A !=0:
        if user_num_6_A == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                      party_partyTel_1=now_phone[i+1],
                                      party_partyTel_2=now_phone[i+2], callOutType_custom=6,
                                      isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_6_A == 4:
            pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[i+1],
                                          party_partyTel_2=now_phone[i+2],party_partyTel_3=now_phone[i+3], party_partyTel_4=now_phone[i+4], callOutType_custom=6, isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=3)
            del now_phone[0:4]
        else:
            pass

    elif i > callOutType_1_sum + callOutType_4_sum + callOutType_6_scene_A and i <= callOutType_1_sum + callOutType_4_sum + callOutType_6_sum and callOutType_6_scene_B !=0:
        if user_num_6_B == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], callOutType_custom=7,
                                          isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_6_B == 4:
            pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], party_partyTel_3=now_phone[i+3], party_partyTel_4=now_phone[i+4], callOutType_custom=6, isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=3)
            del now_phone[0:4]

        else:
            pass

    elif i > callOutType_1_sum + callOutType_4_sum + callOutType_6_sum and i <= callOutType_1_sum + callOutType_4_sum + callOutType_6_sum + callOutType_7_scene_A and callOutType_7_scene_A !=0:
        if user_num_7_A == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], callOutType_custom=1,
                                          isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_7_A == 4:
            pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], party_partyTel_3, party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus)
            del now_phone[0:4]

        else:
            pass

    elif i > callOutType_1_sum + callOutType_4_sum + callOutType_6_sum + callOutType_7_scene_A and i <= callOutType_1_sum + callOutType_4_sum + callOutType_6_sum + callOutType_7_sum and callOutType_7_scene_B !=0:
        if user_num_7_B == 2:
            pcs_create.create_Meeting_two(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], callOutType_custom=1,
                                          isRecord=1, subscribeHostStatus=0, subscribeGuestStatus=0)
            del now_phone[0:2]

        elif user_num_7_B == 4:
            pcs_create.create_Meeting_four(token=token, times=i, start_time=start_time, party_partyTel_0=now_phone[i],
                                          party_partyTel_1=now_phone[meeting_sum + i],
                                          party_partyTel_2=now_phone[2 * meeting_sum + i], party_partyTel_3, party_partyTel_4, callOutType_custom, isRecord, subscribeHostStatus, subscribeGuestStatus)
            del now_phone[0:4]

        else:
            pass
    else:
        logging.error("这段太蠢了,能力有限,除此之外想不到更好得通用方法")
"""

#
# pcs_token = PCS_getToken.Get_Token()
#
# token = pcs_token.get_Token()
#
# pcs_create = PCS_createmeeing()
#
# #pcs_create.create_Meeting(2,2)
#
