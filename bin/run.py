#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:run.py
@time:2020/4/3  10:44
@desc
'''
import unittest
from BeautifulReport import BeautifulReport

from lib.set_case_file import create_case_file
from model.setting import *

# 首先生成测试用例
create_case_file()


file_name = '{}接口测试.html'.format(TIME)
#选择要执行的用例
discover =unittest.defaultTestLoader.discover(CASE_PATH,'test*.py')

BeautifulReport(discover).report(description='接口测试',filename=file_name,report_dir=REPORT_PATH)




