# -*- coding:utf-8 -*-
# @Time    : 2022/3/15 8:32
# @Author  : Yinkai Yang
# @FileName: extract_version1.0.py
# @Software: PyCharm
# @Description: this is a program related to
import json

import requests
from bs4 import BeautifulSoup


def read_file():
    with open('teacher.txt', 'r') as f:
        tmp = []
        lines = f.readlines()

        for i in lines:
            tmp.append(i.rstrip('\n'))
        f.close()
        # print(list_tmp)
        return tmp


def get_data(url):
    # 获取页面的内容，然后进行soup操作
    page = requests.get(url=url)
    content = page.text

    # 创建soup
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def soup_easy(soup):
    # 通过soup进行操作，这里才是操作的关键
    for item in soup.find('li', attrs={'itemtype': 'http://schema.org/Person'}):
        # print(item)  # 获得预期的标签结果
        # 获得a标签里面的链接，写进list
        thing = " "
        thing = item.select('a')
        # print(thing)
        print(thing[0].get('href'))

    return thing[0].get('href')


def soup_difficult(soup):

    paper = []
    # 核心查询部分find_all
    for item in soup.find_all('cite', attrs={'class': 'data tts-content'}):
        i = 1
        first_author = None
        second_author = None
        third_author = None
        fourth_author = None
        fifth_author = None
        paper_title = None
        paper_from = None
        paper_page = None
        paper_year = None
        # print("{")
        for some in item.find_all('span', attrs={'itemprop': 'author'}):
            # 控制打印，便于debug
            if i == 1:
                # first_author = some.get_text().encode('utf-8')
                first_author = some.get_text()
            if i == 2:
                second_author = some.get_text()
            if i == 3:
                third_author = some.get_text()
            if i == 4:
                fourth_author = some.get_text()
            if i == 5:
                fifth_author = some.get_text()
            i = i + 1
        # print("}")
        # print("*********************************")
            # author.append(item.get_text().encode('utf-8'))
        for title in item.find('span', attrs={'class': 'title'}):
            paper_title = title.get_text()
        for pform in item.find_all('span', attrs={'itemprop': 'name'}):
            paper_from = pform.get_text()
        for page in item.find_all('span', attrs={'itemprop': 'pagination'}):
            paper_page = page.get_text()
        for year in item.find_all('span', attrs={'itemprop': 'datePublished'}):
            paper_year = year.get_text()
        paper.append(
            {
                "first_author": first_author,
                "second_author": second_author,
                "third_author": third_author,
                "fourth_author": fourth_author,
                "fifth_author": fifth_author,
                "paper_title": paper_title,
                "paper_from": paper_from,
                "paper_page": paper_page,
                "paper_year": paper_year,
            }
        )
    return paper


def write_file(data):
    with open('teacher_information_other_test.json', 'w+', encoding='gbk') as f:
        json_str = json.dumps(data, indent=4, ensure_ascii=True)  # 这就是为什么json文件中的问题，里面不是GBK
        f.write(json_str)
        f.write('\n')
    f.close()
    return


def main():
    information = []
    teacher = read_file()
    for i in teacher:
        url = 'https://dblp.uni-trier.de/search?q=' + i
        # 第一次进行链接的访问
        soup = get_data(url)
        link_url = soup_easy(soup)

        # 第二次进入核心链接进行访问
        link_soup = get_data(link_url)
        # print(soup_difficult(link_soup))
        paper = soup_difficult(link_soup)
        information.append(
            {
                "teacher": i,
                "paper": paper
            }
        )
    write_file(information)
    # print("------------------------------------")
    # print("------------------------------------")
    # print("------------------------------------")
    # print("------------------------------------")
    # print(str(information[0].get('teacher')).replace("\xf6", ""))
    return


if __name__ == '__main__':
    main()
