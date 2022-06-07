"""
目的：
作者：小刚刚
日期：2021年11月19日
"""
import requests

# 1. 指定URL
URL = 'https://www.sogou.com/'

# 2.发起请求
response = requests.get(url=URL)  # 返回一个响应对象
print(response)

# 3. 获取响应数据, .text 返回得是字符串形式的响应数据
page_text = response.text
print(page_text)

# 4. 持久化数据
with open('搜狗.html', 'w', encoding='UTF-8') as fp:
    # print(fp)
    fp.write(page_text)
