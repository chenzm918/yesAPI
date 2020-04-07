#!/usr/bin/env python
# encoding: utf-8
'''
@author:chengbaiquan
@software:apitest
@file:test_login_all.py
@time:2020-04-01  21:53
@desc
'''
import os
import unittest

import ddt
import requests

from lib.util import *
from model.setting import *

@ddt.ddt
class Yesapi_find_pwd(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'yesapi_find_pwd.yaml'))
    def test_yesapi_find_pwd(self,**case_data):
        url=case_data.get('url')
        data=case_data.get('data')
        check=case_data.get('check')
        method=case_data.get('method')
        jiami=case_data.get('jiami')
        print(jiami)
        if jiami == True:
            if 'new_password'in data:
                data['new_password'] = hash_code(str(data['new_password']))
        if method.lower() == 'post':
            res=requests.post(url,data=data)
            resp=res.text
        else:
            res=requests.get(url,params=data)
            resp = res.text
        resp=set_res_data(resp)
        for c in check:
            self.assertIn(c,resp)

