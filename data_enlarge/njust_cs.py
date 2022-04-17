# # -*- coding:utf-8 -*-
# # @Time    : 2022/4/4 13:26
# # @Author  : Yinkai Yang
# # @FileName: njust_cs.py
# # @Software: PyCharm
# # @Description: this is a program related to
# import requests
# from bs4 import BeautifulSoup
# from numpy import random
# from detail_information.util import cofig
# # import httpx
#
# information = []
#
#
# def get_page_text(url):
#     # proxies = cofig.Preparation.proxies
#     headers = cofig.Preparation.headers
#     page = requests.get(url=url, headers=random.choice(headers))
#     # page = httpx.get(url=url, headers=random.choice(headers))
#
#     content = page.text
#     print(content)
#     return content
#
#
# def get_information(text):
#     soup = BeautifulSoup(text, 'html.parser')
#     for i in soup.find_all('div', attrs={'class': 'box2'}):
#         print(i)
#         item = i.select('a')
#         temp = item[0].get('href')
#         print(temp)
#     return
#
#
# def write_file():
#     return
#
#
# def main():
#     url = [
#         'https://cs.njust.edu.cn/js_11705/list.htm',
#         'https://cs.njust.edu.cn/fjs_11707/list.htm',
#         'https://cs.njust.edu.cn/1735/list.htm'
#     ]
#     for i in url:
#         print(i)
#         content = get_page_text(url=i)
#         get_information(content)
#     return
#
#
# if __name__ == '__main__':
#     main()
