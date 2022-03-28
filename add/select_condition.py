# -*- coding:utf-8 -*-
# @Time    : 2022/3/26 20:07
# @Author  : Yinkai Yang
# @FileName: select_condition.py
# @Software: PyCharm
# @Description: this is a program related to
# 尝试做一下精准选择，根据老师的一些个人信息进行准确定位
import requests
from bs4 import BeautifulSoup

name = []


def read_file():
    """从teacher.txt文件中读取老师的信息，存放在临时list里面

    :return: 返回一个存储老师名字的list
    """
    with open('test_add.txt', 'r') as f:
        tmp = []
        lines = f.readlines()

        for i in lines:
            tmp.append(i.rstrip('\n'))
            name.append(i.replace('_', ' ').strip('\n'))
        f.close()
        return tmp


def get_soup(url):
    """根据url，将网页处理成可以操作的soup对象

    :param url: 网页的路径（html界面的路径）
    :return: 返回一个html页面的操作对象soup
    """
    page = requests.get(url=url)
    content = page.text
    # 创建soup
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def soup_first(soup, counter, information):
    """根据已有的信息进行老师的精确选择，只有精确匹配到才会返回路径

    :param soup: 一个可以操作的soup对象
    :return: 精确查找后老师论文信息的url
    """
    url = ''
    print("==========================================================================================================")
    for item in soup.find_all('li', attrs={'itemtype': 'http://schema.org/Person'}):
        thing = item.select('span')
        temp_name = thing[0].get_text()
        if temp_name == name[counter]:
            temp_infor = item.select('small')
            a = temp_infor[0].get_text().encode('gbk', 'ignore').decode('gbk')
            b = information[counter]['superior_administrative'] + ', ' + information[counter]['second_administrative']
            if b in a:
                print('true')
                little = item.select('a')
                url = little[0].get('href')
                print(little[0].get('href'))
        else:
            break

    return url


def create_information():
    """用于信息比较，提供自己编写的数据

    :return: 存储有老师信息的information的list
    """
    information = [
        {
            "name": "胡伟",
            "introduction": "胡伟，男，博士，副教授",
            "superior_administrative": "Nanjing University",
            "second_administrative": "State Key Laboratory for Novel Software Technology",
            "paper": [
                {
                    "first_author": "Hanshu Hong",
                    "second_author": "Zhixin Sun",
                    "third_author": None,
                    "fourth_author": None,
                    "fifth_author": None,
                    "paper_title": "",
                    "paper_from": "",
                    "paper_page": "",
                    "paper_year": ""
                }
            ]
        },
        {
            "name": "丁磊",
            "introduction": "丁磊，男，博士，副教授",
            "superior_administrative": "Nanjing University of Posts and Telecommunications",
            "second_administrative": "School of Modern Posts",
            "paper": [
                {
                    "first_author": "Hanshu Hong",
                    "second_author": "Zhixin Sun",
                    "third_author": None,
                    "fourth_author": None,
                    "fifth_author": None,
                    "paper_title": "",
                    "paper_from": "",
                    "paper_page": "",
                    "paper_year": ""
                }
            ]
        }
    ]
    return information


def dblp_function():
    """调用相关函数获取信息，对introduction中的paper信息进行修改

    :param
    :return: 没有返回值
    """
    information = create_information()
    teacher = read_file()
    count = 0
    for i in teacher:
        url = 'https://dblp.uni-trier.de/search/author?q=' + i
        # 第一次进行链接的访问
        soup = get_soup(url)
        soup_first(soup, count, information)
        count = count + 1

    return


if __name__ == '__main__':
    dblp_function()
