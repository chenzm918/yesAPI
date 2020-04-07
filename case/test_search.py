#!/usr/bin/env python
# encoding: utf-8
'''
@author:mikigo
@software:SeleniumTest
@file:test_register.py
@time:2020/1/15  16:18
@desc
'''
import os

import requests
import unittest
import ddt

from model.setting import *


@ddt.ddt
class SearchTest(unittest.TestCase):

    @ddt.file_data(os.path.join(DATA_PATH,'search.yaml'))
    def test_search(self, **kwargs):
        # 获取参数值
        url = kwargs.get("url")
        data = kwargs.get("data")
        check = kwargs.get("check")
        self._testMethodDoc = kwargs.get("detail")
        # # 数据处理
        # if "password" in data:
        #     password = pwd_hash(data["password"])
        #     data["password"] = password
        # username = data["username"]
        # number = random.randint(30,100000)
        # data["username"] = "%s_%d" % (username,number)
        # 断言
        result = requests.request('post', url, json=data)
        result = result.text.replace('":"', '=').replace('":', '=')
        for i in check:
            self.assertIn(i, result)


if __name__ == '__main__':
    unittest.main()
