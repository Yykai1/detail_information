# -*- coding:utf-8 -*-
# @Time    : 2022/3/20 16:51
# @Author  : Yinkai Yang
# @FileName: web_information.py
# @Software: PyCharm
# @Description: this is a program related to
import json

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }
    # 获取页面的内容，然后进行soup操作
    page = requests.get(url=url, headers=header)
    content = page.text
    # 创建soup
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def link_get(soup):
    # 通过soup进行操作，这里才是操作的关键
    for item in soup.find_all('a'):
        print(item.get('href'))
    return


def main():
    url = 'https://simp.njupt.edu.cn/szqkjj/list.htm'
    soup = get_soup(url)
    link_get(soup)


if __name__ == '__main__':
    main()


