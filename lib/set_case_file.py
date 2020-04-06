#!/usr/bin/env python
# encoding: utf-8
'''
@author:chengbaiquan
@software:apitest
@file:set_case_file.py
@time:2020-04-02  21:25
@desc
'''
from model.setting import *
def create_case_file():
    """
    从data目录中找到所有的yaml文件
    使用case_template.txt作为模板，生成测试用例文件
    """
    file_lists=os.listdir(DATA_PATH)#取出data目录下的所有文件
    template_file=os.path.join(TEMPLATE_PATH,'case_template.txt')
    print(template_file)
    for fList in file_lists:
        if fList.endswith('.yaml')or fList.endswith('.yml'):
            #测试用例文件名和yaml文件名
            data_file=fList.replace('.yaml','').replace('.yml','')
            #测试用例方法名
            method_name=data_file.lower()
            #测试用例类名
            class_name=method_name.capitalize()
            with open(template_file,'r',encoding='utf-8')as temp:
                #从模板文件中取内容
                content=temp.read() % {#对读出来的模板文件(是字符串类型数据)进行字符串格式化把三个名字替换成用例的名字
                    'class_name':class_name,
                    'method_name':method_name,
                    'data_file':data_file
                }
             #生成的py文件名称
            test_case_file='test_%s.py'%data_file
            #根据模板生成测试用例
            with open(os.path.join(CASE_PATH,test_case_file),'w',encoding='utf-8')as f:
                f.write(content)
