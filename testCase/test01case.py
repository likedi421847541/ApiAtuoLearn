# -*- coding:utf-8 -*-
import json
import unittest
from common.configHttp import RunMain
import paramunittest
from testfile import geturlParams
import urllib.parse  # 将 url 按一定格式进行拆分
from testfile import readExcel
url = geturlParams.geturlParams().get_url()  # 调用我们的 gerurlparams 获取拼接的url
login_xls = readExcel.readExcel().get_xls('testFile.xlsx','login')
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        """
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
    def description(self):
        """
        test report description
        :return:
        """
        self.case_name
    def setUp(self):
        print(self.case_name+'测试开始前准备')
    def test01case(self):
        self.checkResult()
    def tearDown(self):
        print('测试结束，输出log完结\n\n')
    def checkResult(self): #断言
        url1 = 'http://127.0.0.1:8888/login?'
        new_url1 = url1+self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url1).query)) # 将一个完整的 url中的 name=&pwd 转为{'name':'','pwd':''}
        # 使用 urllib.parse.urlsplit 将 url 分为5个部分，返回一个包含字符串的元组：协议，位置，路径，查询，片段
        # 使用 parse_qsl 返回列表
        info = RunMain().run_main(self.method,new_url1,data1)
        ss = json.loads(info)
        if self.case_name == 'login':
            self.assertEqual(ss['code'],200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],10001)