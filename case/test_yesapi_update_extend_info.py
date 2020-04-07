#!/usr/bin/env python
# encoding: utf-8
'''
@author:chengbaiquan
@software:apitest
@file:test_findpwd_with_EmailCode.py
@time:2020-04-03  15:16
@desc
'''
import json
import os
import unittest
import ddt
import requests

from lib.util import set_res_data, hash_code
from model.setting import DATA_PATH, API_URL


@ddt.ddt
class Yesapi_Update_Extend_Info(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH, 'yesapi_update_extend_info.yaml'))
    def test_find_pwd(self, **case):
        data = case.get('data')
        datal = case.get('datalogin')
        check = case.get('check')
        method = case.get('method')
        jiami=case.get('jiami')
        tokenis=case.get('tokenis')
        ext_infois=case.get('ext_infois')
        self._testMethodDoc = case.get('doc', "用例没有描述")
        if jiami == True:
            if 'password' in datal:
                datal['password'] = hash_code(str(datal['password']))
        if tokenis == True:
            # 获取登录的token值
            resl = requests.post(API_URL, data=datal)
            resl = resl.json()
            token = resl.get("data").get("token")
            data["token"] = token
        if method.lower() == 'post':
            if ext_infois==True:
                data["ext_info"]=json.dumps(data["ext_info"])
            res = requests.post(API_URL, data=data)
            resp = res.text
        elif method.lower()=='get':
            if ext_infois==True:
                data["ext_info"]=json.dumps(data["ext_info"])
            res = requests.get(API_URL, params=data)
            resp = res.text
        resp = set_res_data(resp)
        for c in check:
            self.assertIn(c, resp)
