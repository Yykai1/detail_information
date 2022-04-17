# -*- coding:utf-8 -*-
# @Time    : 2022/4/4 7:54
# @Author  : Yinkai Yang
# @FileName: seu_cs.py
# @Software: PyCharm
# @Description: this is a program related to
from numpy import random
from bs4 import BeautifulSoup

import requests


def get_page_text(url):
    # 协议
    proxies = [
        {'proxy': 'https://183.166.162.182:9999'},
        {'proxy': 'https://112.111.217.76:9999'},
        {'proxy': 'https://114.239.150.98:9999'},
        {'proxy': 'https://115.218.7.204:9000'}
    ]
    # 用户代理
    headers = [
        {
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
        {
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'},
        {
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
        {
            'user-agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'},
        {
            'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)'},
        {
            'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)'},
        {
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)'},
        {
            'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'}
    ]
    page = requests.get(url=url, proxies=random.choice(proxies), headers=random.choice(headers))
    content = page.text
    return content


def get_result(text):
    page = []
    count = 0
    soup = BeautifulSoup(text, 'html.parser')
    for i in soup.find_all('td'):
        item = i.select('a')
        if not [] == item:
            temp = item[0].get('href')
            if len(temp) > 45:
                print('-------------', count)
                count = count + 1
                page.append(temp)
                print(temp)
    write_file(page)
    return


def write_file(page):
    with open('seu_cs_teachers.txt', 'w+') as f:
        for i in page:
            print(i)
            f.write(i)
            f.write('\n')
    f.close()
    return


def main():
    url = 'https://cse.seu.edu.cn/22622/list.htm'
    text = get_page_text(url=url)
    get_result(text)
    return


if __name__ == '__main__':
    main()
