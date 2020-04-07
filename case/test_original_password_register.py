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


@ddt.ddt
class Register(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH, 'original_password_register.yaml'))
    def test_login(self, **cases_data):
        # 获取数据
        url = cases_data.get("url")
        data = cases_data.get("data",'无')
        check = cases_data.get("check")
        self._testMethodDoc = data.get('doc')

        # 发送请求
        result = requests.post(url=url, data=data)
        # 断言
        result = result.text.replace('":"', '=').replace('":', '=')
        for c in check:
            self.assertIn(c, result)
