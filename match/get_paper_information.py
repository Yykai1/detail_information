# -*- coding:utf-8 -*-
# @Time    : 2022/4/17 13:26
# @Author  : Yinkai Yang
# @FileName: get_paper_information.py
# @Software: PyCharm
# @Description: this is a program related to
import json

import requests
from bs4 import BeautifulSoup


def get_file():
    """从teacher.txt文件中读取老师的信息，存放在临时list里面

    :return: 返回一个存储老师名字的list
    """
    with open('teacher.txt', 'r') as f:
        tmp = []
        lines = f.readlines()

        for i in lines:
            tmp.append(i.rstrip('\n'))
        f.close()
        # print(list_tmp)
        return tmp


def get_data(url):
    """根据url，将网页处理成可以操作的soup对象

    :param url: 网页的路径（html界面的路径）
    :return: 返回一个html页面的操作对象soup
    """
    # 获取页面的内容，然后进行soup操作
    page = requests.get(url=url)
    content = page.text

    # 创建soup
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def soup_easy(soup):
    """第一次界面处理，查询结果list的len==0则返回None，否则进行检索，获取a标签下面的href

    :param soup: 一个可以操作的soup对象
    :return: a标签下面的href链接，作为第二次检索的关键url
    """
    # 通过soup进行操作，这里才是操作的关键
    print("==========================================================================================================")
    if len(soup.find_all('li', attrs={'itemtype': 'http://schema.org/Person'})) == 0:
        return None
    for item in soup.find('li', attrs={'itemtype': 'http://schema.org/Person'}):
        # print(item)  # 获得预期的标签结果
        # 获得a标签里面的链接，写进list
        # print(item)
        thing = ""
        thing = item.select('a')
        # print(thing)
        print(thing[0].get('href'))

    return thing[0].get('href')


def soup_difficult(soup):
    """第二次检索，主要是获取老师的论为信息，并进行处理

    :param soup: 一个可以操作的soup对象
    :return: 返回老师论文信息处理的结果paper，json格式
    """
    paper = []
    ptype = []
    for i in soup.find_all('div', attrs={'class': 'box'}):
        thing = ""
        thing = i.select('img')
        ptype.append(thing[0].get('title'))
    # print(len(ptype))
    # 核心查询部分find_all
    count = 0
    for item in soup.find_all('cite', attrs={'class': 'data tts-content'}):
        i = 1
        first_author = None
        second_author = None
        third_author = None
        fourth_author = None
        fifth_author = None
        paper_type = None
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
                "paper_type": ptype[count],
                "paper_title": paper_title,
                "paper_from": paper_from,
                "paper_page": paper_page,
                "paper_year": paper_year,
            }
        )
        count += 1
    # print(count)  # 程序结束时print(len(ptype))==count
    return paper


def write_file(data):
    """写文件，记录老师的详细信息

    :param data: data列表信息（json格式）
    :return: 没有返回值
    """
    with open('paper_information_1.json', 'w+', encoding='utf-8') as f:
        json_str = json.dumps(data, indent=4, ensure_ascii=True)  # 这就是为什么json文件中的问题，里面不是GBK
        f.write(json_str)
        f.write('\n')
    f.close()
    return


def main():
    """调用相关函数获取信息，对introduction中的paper信息进行修改

    :param introduction: 所有老师信息的json格式list，可以利用键值对进行修改
    :return: 没有返回值
    """
    information = []
    teacher = get_file()
    count = 0
    for i in teacher:
        information.append({
            "name": str(i),
            "paper": None
        })
    for i in teacher:
        paper = None
        url = 'https://dblp.uni-trier.de/search?q=' + i
        # url = 'https://dblp.uni-trier.de/search/author?q=' + i
        # 第一次进行链接的访问
        soup = get_data(url)
        link_url = soup_easy(soup)

        if link_url != None:
            # 第二次进入核心链接进行访问
            link_soup = get_data(link_url)
            # print(soup_difficult(link_soup))
            paper = soup_difficult(link_soup)
        information[count]['paper'] = paper
        count = count + 1

    write_file(information)
    return


if __name__ == '__main__':
    main()
