# -*- coding:utf-8 -*-
import requests
import json

class RunMain():
    def send_post(self,url,data):  # 定义一个方法，封装 post 方法，传入需要的参数 url 和data，参数必须按照顺序传入
        result = requests.post(url,data).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        # dump 方法提供一些可选参数，让输出格式提高可读性
        # sort_keys 是告诉编码器按照字典顺序（a到z）输出
        # ident 是参数根据数据格式缩进显示，读起来更加清晰
        # ensure_ascii =False 便是输出的是真正的中文
        return res
    def send_get(self,url,data):
        result = requests.get(url=url,params=data).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def run_main(self,method,url=None,data=None): # 定义一个 run_main 函数，通过传来的 method来执行不同get或 post 请求
        result = None
        if  method ==  'post':
            result = self.send_post(url,data)
        elif method == 'get':
            result = self.send_get(url,data)
        else:
            print('method值错误！！！')
        return result
if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login'
    result1 = RunMain().run_main('post',url,{'name':'xiaoming','pwd':'111'})
    result2 = RunMain().run_main('get',url,'name=xiaoming&pwd=111')
    print(result1)
    print(result2)