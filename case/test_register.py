#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:test_register.py
@time:2020/4/3  12:06
@desc
'''
import unittest
import ddt
import os
from model.setting import*
from lib.util import *
import requests


@ddt.ddt
class Register(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'register.yaml'))
    def test_register(self,**case):
        url = case.get('url')
        data = case.get("data")
        check = case.get('check')
        MD_5 = case.get('MD_5')

        self._testMethodDoc = case.get('doc','无')
        if MD_5 == True:
            if 'password' in data:
                data['password'] = hash_code(data['password'])


        result = requests.post(url=url,data=data)
        ass = set_res_data(result.text)
        for c in check:
            self.assertIn(c,ass)




if __name__=='__main__':
    unittest.main()