"""
目的：
作者：小刚刚
日期：2021年11月20日
"""
from bs4 import BeautifulSoup
fp = open('index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup)
