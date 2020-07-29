# -*- coding:utf-8 -*-
'''
python 接口自动化1 -- 发送 get 请求
'''
import requests
# 请求博客首页  get 请求
r1 = requests.get('https://home.cnblogs.com/u/1893292')
print(r1.text)
print(r1.status_code)  # 查看状态码

# 参数 params
'''
发送一个带有参数的 get 请求
请求参数 ： 参数名 = 值  如 keyword = hello 或者字典形式 {"keyword":"hello"}
多个参数格式：{"key1":"value1","key2":"value2"}
'''
par = {"keyword":"hello"}
url = 'https://group.cnblogs.com/group/search'
r2 = requests.get(url,par)
print(r2.text)
print(r2.status_code)

'''
content : 百度首页如果使用 r.text 会发现获取到的内容有乱码，因为百度首页响应内容是 gzip 压缩（非 text文本）
在代码里 可以用 r.content 这个方法，content 会自动解码 gzip 和 deflate 压缩
'''

'''
response 的返回内容还有其他更多信息
-- r.status_code 响应状态码
-- r.headers 以字典对象存储服务器响应头
-- r.json()  Requests 中内置的 Json 解码器
-- r.url  获取 url
-- r.encoding 获取编码格式
-- r.cookies 获取 cookies

'''