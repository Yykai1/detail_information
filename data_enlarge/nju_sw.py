# -*- coding:utf-8 -*-
# @Time    : 2022/4/4 16:15
# @Author  : Yinkai Yang
# @FileName: nju_sw.py
# @Software: PyCharm
# @Description: this is a program related to
import random
import requests
from bs4 import BeautifulSoup

from detail_information.util import cofig

information = []


def get_data(url):
    headers = cofig.Preparation.headers
    page = requests.get(url, headers=random.choice(headers))
    content = page.text
    return content


def get_urls(text):
    count = 0
    soup = BeautifulSoup(text, 'html.parser')
    for i in soup.find_all('td', attrs={'width': '165'}):
        item = i.select('a')
        if not [] == item:
            print(count)
            count = count + 1
            temp=item[0].get('href')
            print(temp)
            information.append(temp)
    return


def write_file():
    with open('nju_sw_teachers.txt', 'w+') as f:
        for i in information:
            print(i)
            f.write(i)
            f.write('\n')
    f.close()
    return


def main():
    url = 'https://software.nju.edu.cn/szll/szdw/index.html'
    text = get_data(url)
    get_urls(text)
    write_file()
    return


if __name__ == '__main__':
    main()
