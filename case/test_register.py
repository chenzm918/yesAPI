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
#接口说明：用户注册接口
#进行新用户注册，创建一个新的会员账号，注册密码需要使用md5后的密码。
#必须要传的参数有app_key、username、password
#选填参数：uuid、token、ext_info
#密码必须md5加密
#app_key长度为32、uuid长度为32、token64位、usename(1,50)
# ext_info注册时的用户扩展信息，注册后可修改，需要JSON编码后传递。
# 格式：ext_info={"扩展字段名":"值"}，可以同时更新多个字段。

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