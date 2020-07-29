# -*- coding:utf-8 -*-
import requests
s = requests.session()
url = 'http://api2.learning-genie.com/api/v1/account/login'
data = {"email":"421847541@qq.com","password":"12345678q","from":"web","emailLoginExpireFlag":""}
headers = {
   'Accept':'application/json, text/plain, */*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Content-Type':'application/json;charset=UTF-8',
    'X-UID':'10CACAAF-B403-4EE8-AB74-2F20D97D8C7D'
}
r = s.post(url,json = data,headers = headers)
result = r.json()
print( result['token'])

# headers1 = {
#     'Accept':'application/json, text/plain, */*',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
#     'Content-Type':'application/json;charset=UTF-8',
#     'X-LG-Token':"result['token']",
#     'X-UID':'10CACAAF-B403-4EE8-AB74-2F20D97D8C7D'
# }
headers["X-LG-Token"] = result['token']
url2 = 'https://api2.learning-genie.com/api/v1/centers'
data1 = {"name":"test002","user_id":"10CACAAF-B403-4EE8-AB74-2F20D97D8C7D","send_report_time":"18:00:00","timezone":"Asia/Shanghai"}
r1 = s.post(url2,json=data1,headers = headers,verify = False)
print(r1.text)