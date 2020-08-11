# -*- coding:utf-8 -*-
import unittest
from common.Login import Login
class Login_001(unittest.TestCase):
    def test_login(self):
        url = 'http://stage.api2.learning-genie-api.com/api/v1/account/login'
        data = {"email":"3123@qq.com.bak","password":"12345678q","from":"web","emailLoginExpireFlag":""}
        login = Login(url,data).login()
        print(login.content)
