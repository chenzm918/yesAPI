#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:test_personalinfo.py
@time:2020/4/3  16:02
@desc
'''
import unittest
import ddt
import os
from model.setting import*
from lib.util import *
import requests


@ddt.ddt
class Personalinfo(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'personalinfo.yaml'))
    def test_personalinfo(self,**case):
        url = case.get('url')#获取的是个人信息的url
        data = case.get("data") #获取data中的数据
        app_key = case.get("data").get('app_key')#获取data中的app_key
        uuid = case.get('data').get('uuid')#获取data中的uuid
        token = case.get('data').get('token')#获取data中的token
        _token = case.get('_token')#获取_token中的值。为后面判断提供依据
        _uuid = case.get('_uuid')#获取_token中的值。为后面判断提供依据
        check = case.get('check')
        self._testMethodDoc = case.get('doc', '无')
        if _token == True and _uuid==True:
            login_app_key = case.get("data_login").get('login_app_key')#获取的是登录data中的app_key
            username = case.get("data_login").get('username')#获取的是登录data中的username
            password = case.get("data_login").get('password')#获取的是登录data中的password
            login_url = case.get("data_login").get('login_url')#获取的是登录的url
            _token = get_token(login_url, login_app_key, username, password)[1]#获取动态的token
            _uuid = get_token(login_url, login_app_key, username, password)[0]#获取动态的uuid
            dic = {'app_key': app_key, 'uuid': _uuid, 'token': _token}
            result = requests.post(url=url, data=dic)
        elif _uuid == False:
            login_app_key = case.get("data_login").get('login_app_key')#获取的是登录data中的app_key
            username = case.get("data_login").get('username')#获取的是登录data中的username
            password = case.get("data_login").get('password')#获取的是登录data中的password
            login_url = case.get("data_login").get('login_url')#获取的是登录的url
            _token = get_token(login_url, login_app_key, username, password)[1]#获取动态的uuid
            dic = {'app_key': app_key, 'uuid': uuid, 'token': _token}
            result = requests.post(url=url, data=dic)
        elif _token == False:
            login_app_key = case.get("data_login").get('login_app_key')#获取的是登录data中的app_key
            username = case.get("data_login").get('username')#获取的是登录data中的username
            password = case.get("data_login").get('password')#获取的是登录data中的password
            login_url = case.get("data_login").get('login_url')#获取的是登录的url
            _uuid = get_token(login_url, login_app_key, username, password)[0]#获取动态的token
            dic = {'app_key': app_key, 'uuid': _uuid, 'token':token}
            result = requests.post(url=url, data=dic)
        else:
            result = requests.post(url=url, data=data)

        ass = set_res_data(result.text)
        for c in check:
            self.assertIn(c, ass)



if __name__=='__main__':
    unittest.main()