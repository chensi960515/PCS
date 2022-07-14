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
import json
import requests

from tools import DemoLogger
from pcs_package import conf, meeting
from pcs_package import PCS_getToken

logging = DemoLogger()
url_sec_token = conf['parameter']['url_sec_token']

sec_token = PCS_getToken.Get_Token()
token = sec_token.get_Token(url_sec_token)
sec_cancelMeeting_url = conf['parameter']['url_sec_cancelMeeting']
sec_startMeeting_url = conf['parameter']['url_sec_startMeeting']
sec_closeMeeting_url = conf['parameter']['url_sec_colseMeeting']
sec_cookie = conf['parameter']['sec_cookie']
sec_path = '../eph_data/sec.txt'


def get_sec_parameter(file_path, start_index, end_index):
    list_meetingCode = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for x in f:
            list_meetingCode.append(x[start_index:end_index])

    return list_meetingCode


def cancelMeeting():
    """
    取消 畅听会议
    :param meetingCode:  创建时保留
    :return:
    """
    meetingCodes = get_sec_parameter('../eph_data/sec.txt', 0, 12)
    url = sec_cancelMeeting_url
    headers = {'Content-Type': 'application/json'}
    for meetingCode in meetingCodes:
        payload = json.dumps({
            "token": token,
            "meetingCode": meetingCode
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        logging.logger.info(response.text)


def startMeeting():
    """
    开启 畅听会议
    :return:
    """
    hostPasscodes = get_sec_parameter('../eph_data/sec.txt', 13, 22)
    phoneNumbers = get_sec_parameter('../eph_data/sec.txt', 13, -1)
    url = sec_startMeeting_url

    for hostPasscode in hostPasscodes:
        for phoneNumber in phoneNumbers:
            if phoneNumber[0:9] == hostPasscode:
                phoneNumber_str_split = phoneNumber[11:-1].split(",")
                phoneNumber_list = []
                for i in phoneNumber_str_split:
                    phoneNumber_list.append(i.replace("\'", "").strip())
                payload = json.dumps({
                    "hostPasscode": hostPasscode,
                    "hostCode": phoneNumber_list[0:1],
                    "partyCode": phoneNumber_list[1:]
                })
                logging.logger.info(payload)
                headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept":"*/*", "Accept-Encoding":"gzip, deflate, br","Connection": "keep-alive", "cookie": sec_cookie}

                response = requests.request("POST", url, headers=headers, data=payload, files=[])
                logging.logger.info(response.text)


def closeMeeting():
    """
    结束 畅听会议
    :return:
    """
    hostPasscodes = get_sec_parameter('../eph_data/sec.txt', 13, 22)
    url = sec_closeMeeting_url
    headers = {'Content-Type': 'application/json',"Cookie": sec_cookie}
    for hostPasscode in hostPasscodes:
        payload = json.dumps({
            "hostPasscode": hostPasscode
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        logging.logger.info(response.text)

if __name__ == '__main__':
#    cancelMeeting()
    startMeeting()
#    closeMeeting()
