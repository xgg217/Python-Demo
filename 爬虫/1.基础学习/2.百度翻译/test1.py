"""
目的：
作者：小刚刚
日期：2021年11月19日
"""
import requests, json

# 1. 指定URL
URL = 'https://fanyi.baidu.com/sug'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

data = {
    'kw': '1'
}
# 发送请求
a = requests.post(url=URL, data=data, headers=headers)

# json() 返回一个对象
print(a.json())
req_obj = a.json()

print(req_obj['data'][0]['v'])
