#!/usr/bin/env python
# encoding: utf-8
'''
@author:chengbaiquan
@software:apitest
@file:test_findpwd_with_EmailCode.py
@time:2020-04-03  15:16
@desc
'''
import os
import unittest
import ddt
import requests

from lib.util import set_res_data
from model.setting import DATA_PATH, API_URL


@ddt.ddt
class Findpwd_With_EmailCode(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH, 'yesapi_find_pwd.yaml'))
    def test_find_pwd(self, **case):
        data = case.get('data')
        check = case.get('check')
        method = case.get('method')
        self._testMethodDoc = case.get('doc', "用例没有描述")
        print(method)
        if method.lower() == 'post':
            res = requests.post(API_URL, data=data)
            resp = res.text
        else:
            res = requests.get(API_URL, params=data)
            resp = res.text
        resp = set_res_data(resp)
        for c in check:
            self.assertIn(c, resp)
