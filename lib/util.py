
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



#加密函数
def hash_code(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()


#修改响应值中 的内容的格式和ymal中的数据进行匹配
def set_res_data(res):
    if res:
        return res.replace('":"',"=").replace('":',"=")
#获取动态的token和uuid
def get_token(login_url,app_key,username,password):
    password = hash_code(password)
    data = {
        'app_key':app_key,
        'username':username,
        'password':password
    }
    #获取响应值
    result = requests.post(url=login_url,data=data)
    res = result.json()
    #获取token
    token = res.get('data').get('token')
    #获取uuid
    uuid = res.get('data').get('uuid')
    #返回token和uuid
    return uuid,token
