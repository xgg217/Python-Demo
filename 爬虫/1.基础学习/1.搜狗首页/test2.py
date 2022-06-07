"""
目的：简易网页采集器
作者：小刚刚
日期：2021年11月19日
"""

import requests

# 1. 指定URL
URL = 'https://www.sogou.com/web'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

param = {
    'query': '小刚刚'
}

# 2.发起请求 同时携带参数 + UA 伪装
response = requests.get(url=URL, params=param, headers=headers)  # 返回一个响应对象

# 3. 获取响应数据, .text 返回得是字符串形式的响应数据
page_text = response.text

# 4. 持久化数据
with open('搜狗.html', 'w', encoding='UTF-8') as fp:
    # print(fp)
    fp.write(page_text)
