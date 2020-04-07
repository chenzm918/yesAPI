#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:setting.py
@time:2020/4/3  10:45
@desc
'''
import os
import time



API_URL="http://hn216.api.yesapi.cn/"
#获取动态时间

TIME = time.strftime("%Y_%m_%d_%H_%S")
# print(TIME)
#获取当前路径current
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# print(CURRENT_PATH)
# #获取基本路径
BATH_PATH ='\\'.join(CURRENT_PATH.split('\\')[0:-1])

# #获取数据的路径
DATA_PATH = os.path.join(BATH_PATH,'data')
TEST_DATA_PATH = os.path.join(DATA_PATH,'test_19and20')
#获取报告的路径
REPORT_PATH = os.path.join(BATH_PATH,"report")
# #获取用例的路径
CASE_PATH = os.path.join(BATH_PATH,"case")
print(CASE_PATH)
# #获取模板的路径
TEMPLATE_PATH = os.path.join(BATH_PATH,"template")



