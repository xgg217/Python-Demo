"""
目的：
作者：小刚刚
日期：2021年11月19日
"""

import requests, json, time

# 1. 指定URL
URL = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do'
# ?method=getXkzsList'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

one_data = {
    'on': True,
    'page': 1,
    'pageSize': 5,
    'productName': '',
    'conditionType': 1,
    'applyname': '',
    'applysn': ''
}


def get_one_list(url):
    '''
    获取列表数据
    :return:
    '''
    new_url = url + '?method=getXkzsList'
    res = requests.post(url=new_url, data=one_data, headers=headers)
    print(res)
    # return res.json()['list']
    print(res.json())
    arr = []
    for item in res.json()['list']:
        arr.append(item['ID'])
    return arr


def get_two_list(arr):
    '''
    获取详情数据
    :param arr:
    :return:
    '''
    obj = {}
    for x in arr:
        time.sleep(1)
        two_obj = get_two_list_xq(x)
        print('---')
        print(two_obj)
        val = two_obj['epsName']
        obj[val] = two_obj

    json.dump(obj, open('国家药监监督管理局.json', 'w', encoding='UTF-8'), ensure_ascii=False, indent=4)
    print('结束')


def get_two_list_xq(ids):
    new_url = URL + '?method=getXkzsById'
    datas = {
        'id': ids
    }
    res = requests.post(url=new_url, data=datas, headers=headers)
    print(res.json())
    print('***')
    return res.json()


id_list = get_one_list(URL)
print(id_list)
get_two_list(id_list)
