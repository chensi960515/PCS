# -*- coding: utf-8 -*-
# @Time : 2022/5/31 15:46
# @Author : chensi
# @File : __init__.py.py
# @Project : PCS


from tools import read_file
from pcs_package import PCS_getToken


ya = read_file.GetData()
conf_path = f"../config/config.yaml"
meeting_path = f"../config/meeting.yaml"
conf = ya.get_data_list(conf_path)
meeting = ya.get_data_list(meeting_path)