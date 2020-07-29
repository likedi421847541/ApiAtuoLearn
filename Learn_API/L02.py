# -*- coding:utf-8 -*-
import  requests
# help(requests)  # requests 的官方帮助文档
'''
post 请求
以 LG 登录为例
'''
url = 'http://api2.learning-genie.com/api/v1/account/login'
data = {"email":"421847541@qq.com","password":"12345678q","from":"web","emailLoginExpireFlag":""}
headers = {
    'Accept':'application/json, text/plain, */*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Content-Type':'application/json;charset=UTF-8'
}
r = requests.post(url,json=data,headers = headers)
print(r.text)
print(r.status_code)