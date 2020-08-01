# -*- coding:utf-8 -*-
'''
json 数据处理：json 的布尔类型 是 true，false，而 python 是 True，False
以快递 100 网站为准
'''
import requests
url = "https://www.kuaidi100.com/query"
data = {
    "type":"shentong",
    "postid":"773046451247625",
    "temp":"0.8033860904945374",
    "phone":""
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
r = requests.post(url,data,headers = headers,verify = False)
r1= r.json()['data']  # 提取 返回结果里的 data 数据
r2 = r1[0]   # r1 是列表，转化为字典
print(type(r2))
print(r2['context'])
