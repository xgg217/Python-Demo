"""
目的：
作者：小刚刚
日期：2021年11月19日
"""
import requests, json, copy, time

# 1. 指定URL
URL = 'https://movie.douban.com/j/chart/top_list'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

param_obj = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}


def get_dbdy_list():
    arr = []
    obj = {}
    for x in range(0, 21, 20):
        time.sleep(5)
        print(x)
        new_arr = get_dy_data(x)
        arr.extend(new_arr)

    for x in arr:
        val = x['title']
        obj[val] = x
    print(obj)
    json.dump(obj, open('豆瓣电影.json', 'w', encoding='UTF-8'), indent=4,ensure_ascii=False)


def get_dy_data(x):
    new_param_obj = copy.copy(param_obj)
    new_param_obj['start'] = x
    res = requests.get(url=URL, params=new_param_obj, headers=headers)
    print(res.json())
    return res.json()


get_dbdy_list()
