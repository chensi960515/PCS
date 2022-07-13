#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: test_read_file.py
@time: 2022/5/30  21:39
"""

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import time

# driver = webdriver.Chrome()
#
# driver.get("http://selenium.dev")
#
# driver.quit()

# opt = ChromeOptions()  # 创建Chrome参数对象
# opt.headless = True  # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
# driver = Chrome(options=opt)  # 创建Chrome无界面对象
#
# driver.get('http://www.baidu.com')
# print(driver.current_window_handle)
# print(driver.page_source)
# driver.close()

print(int(round(time.time() * 1000)))
