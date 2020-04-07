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


from lib.util import hash_code, set_res_data
from model.setting import *


@ddt.ddt
class ResetTest(unittest.TestCase):

    @ddt.file_data(os.path.join(DATA_PATH,'reset.yaml'))
    def test_reset(self, **kwargs):
        # 获取参数值
        global resp
        url = kwargs.get("url")
        data = kwargs.get("data")
        check = kwargs.get("check")
        self._testMethodDoc = kwargs.get("detail")
        method = kwargs.get('method')
        jiami = kwargs.get('jiami')
        tokenis = kwargs.get('tokenis')
        if jiami == True:
            if 'password' in data:
                data['password'] = hash_code(str(data['password']))
        if tokenis == True:
            # 获取登录的token值
            resl = requests.post(url, data=data)
            resl = resl.json()
            token = resl.get("data").get("token")
            data["token"] = token
        if method.lower() == 'post':
            res = requests.post(url, data=data)
            resp = res.text
        elif method.lower() == 'get':
            res = requests.get(url, params=data)
            resp = res.text
        resp = set_res_data(resp)
        # 断言
        for i in check:
            self.assertIn(i, resp)


if __name__ == '__main__':
    unittest.main()
