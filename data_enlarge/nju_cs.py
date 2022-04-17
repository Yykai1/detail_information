# -*- coding:utf-8 -*-
# @Time    : 2022/4/4 13:26
# @Author  : Yinkai Yang
# @FileName: nju_cs.py
# @Software: PyCharm
# @Description: this is a program related to
import requests
from bs4 import BeautifulSoup
from numpy import random
from detail_information.util import cofig

# import httpx

information = []


def get_page_text(url):
    # proxies = cofig.Preparation.proxies
    headers = cofig.Preparation.headers
    page = requests.get(url=url, headers=random.choice(headers))
    # page = httpx.get(url=url, headers=random.choice(headers))

    content = page.text
    # print(content)
    return content


def get_information(text):
    soup = BeautifulSoup(text, 'html.parser')
    for i in soup.find_all('span', attrs={'class': 'Article_Title'}):
        # print(i)
        item = i.select('a')
        temp = 'https://cs.nju.edu.cn/'+item[0].get('href')
        # print(temp)
        information.append(temp)
    return


def write_file():
    with open('nju_cs_teachers.txt','w+') as f:
        for i in information:
            print(i)
            f.write(i)
            f.write('\n')
    f.close()
    return


def main():
    url = [
        'https://cs.nju.edu.cn/2639/list.htm',
        'https://cs.nju.edu.cn/2640/list.htm',
        'https://cs.nju.edu.cn/2641/list.htm'
    ]
    for i in url:
        # print(i)
        content = get_page_text(url=i)
        get_information(content)
    write_file()
    return


if __name__ == '__main__':
    main()
