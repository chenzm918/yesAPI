#!/usr/bin/env python
# encoding: utf-8
'''
@author:chenzhimin
@software:APITest
@file:util.py
@time:2020/4/3  10:47
@desc
'''
import hashlib
import requests

def hash_code(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()



def set_res_data(res):
    if res:
        return res.replace('":"',"=").replace('":',"=")

def get_token(login_url,app_key,username,password):
    password = hash_code(password)
    login_data={
        "app_key":app_key,
        "username":username,
        "password":password
    }

    result = requests.get(url=login_url,params=login_data)
    res = result.json()
    print(res)
    token = res.get('data').get('token')
    uuid = res.get('data').get('uuid')
    return uuid,token





