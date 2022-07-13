# -*- coding: utf-8 -*-
# @Time : 2022/7/13 18:08
# @Author : chensi
# @File : SEC_options.py
# @Project : PCS

"""
取消会议
开启会议
结束会议
call批量用户
endcall批量用户

"""
import logging

from tools import DemoLogger
from pcs_package import conf, meeting
from pcs_package import PCS_getToken

logging = DemoLogger()
url_sec_token = conf['parameter']['url_sec_token']

sec_token = PCS_getToken.Get_Token()
token = sec_token.get_Token(url_sec_token)
list_meetingCode = []


def get_meetingCode(file_path, start_index, end_index):
    with open(file_path, 'r', encoding='utf-8') as f:
        for x in f:
            list_meetingCode.append(x[start_index:end_index])

    return list_meetingCode


class Sec_Meeting:

    def cancelMeeting(self, meetingCode):
        pass


if __name__ == '__main__':
    res = get_meetingCode('../eph_data/meetingCode.txt', 0, 11)
    print(res)
