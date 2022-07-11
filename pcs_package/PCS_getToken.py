# -*- coding: utf-8 -*-
# @Time : 2022/5/30 18:20
# @Author : chensi
# @File : PCS_getToken.py
# @Project : CVATest

import json
import requests
from tools import read_file

conf_path = f"../config/config.yaml"
ya = read_file.GetData()
conf = ya.get_data_list(conf_path)


class Get_Token:
    def __init__(self):
        pass

    headers = conf['parameter']['headers']
    payload = json.dumps({
        "customerId": conf['parameter']['customerId'],
        "secret": conf['parameter']['secret']
    })

    def get_Token(self, url_token):
        url = url_token
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        res = json.loads(response.text)
        new_token = res['data']['token']
        return new_token
