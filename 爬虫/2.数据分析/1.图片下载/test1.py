"""
目的：
作者：小刚刚
日期：2021年11月19日
"""
import requests,bs4,os

URL = 'https://www.qiushibaike.com/imgrank/'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 获取页面数据
def get_page_data():
    res = requests.get(url=URL,headers=headers).text
    return res

# 获取所有img 标签的 src
def get_img_src(str):
    soup = bs4.BeautifulSoup(str, 'html.parser')
    # list = soup.find_all(class_='article')
    img_arr = soup.select('.article>.thumb>a>img')
    src_arr = []
    for item in img_arr:
        src = item.get('src')
        src_arr.append(src)

    print(src_arr)

def get_img_data(arr):
     i = 1
    # for src in arr:
    #     img = requests.get(url=src,headers=headers).content
        # with open()


# page_str = get_page_data()
# src_list = get_img_src(page_str)
# get_img_data(src_list)
# content
ss = 'https://pic.qiushibaike.com/system/pictures/12489/124899934/medium/URLCP6CYZB0MSHF9.jpg'
hz = os.path.splitext(ss)[1]
print(hz)
a = requests.get(url=ss, headers=headers).content
with open('images/' + str(1) + hz, 'wb') as fp:
    fp.write(a)


