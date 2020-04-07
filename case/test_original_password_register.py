#!/usr/bin/env python
# encoding: utf-8
"""
@author:huxinyuan
@software:SeleniumTest
@file:test_original_password_register.py
@time:2020/4/3  15:13
@desc
"""

import os
import requests
import unittest
import ddt

from model.setting import DATA_PATH

#接口说明：原密码用户注册接口
#进行新用户注册，创建一个新的会员账号，注册密码使用原始密码。
#必须要传的参数有app_key、username、password
#密码不用md5加密
#app_key长度为32、密码长度为大于1、usename(1,50)

@ddt.ddt
class Register(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH, 'original_password_register.yaml'))
    def test_register(self, **cases_data):
        url = cases_data.get("url")
        data = cases_data.get("data")
        check = cases_data.get("check")
        self._testMethodDoc = cases_data.get('doc')
        print(self._testMethodDoc)

        # 发送请求
        result = requests.post(url=url, data=data)
        # 断言
        result = result.text.replace('":"', '=').replace('":', '=')
        for c in check:
            self.assertIn(c, result)
