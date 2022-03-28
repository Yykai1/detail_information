# -*- coding:utf-8 -*-
# @Time    : 2022/3/20 19:36
# @Author  : Yinkai Yang
# @FileName: teachers_to_excel.py
# @Software: PyCharm
# @Description: this is a program related to
import json
import re

import numpy as np
import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

import extraction_utils
import extract_version_1

teachers = []
name = []
introduction = []


def read_file():
    """从teachers_page.txt中读取老师网页

    :return: 存放老师网页url的list
    """
    with open('teachers_page.txt', 'r', encoding='utf-8') as f:
        tmp = []
        lines = f.readlines()

        for i in lines:
            tmp.append(i.rstrip('\n'))
        f.close()
        return tmp


def get_soup(url):
    """根据url，将网页处理成可以操作的soup对象

    :param url: 网页的路径（html界面的路径）
    :return: 返回一个html页面的操作对象soup
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }
    # 获取页面的内容，然后进行soup操作
    page = requests.get(url=url, headers=header)
    page.encoding = 'utf-8'
    content = page.text
    # 创建soup
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def soup_process(soup):
    """获取老师的个人简介，存放进teachers中

    :param soup: 一个可以处理的soup对象
    :return: 无
    """
    # 通过soup进行操作，这里才是操作的关键
    for item in soup.find_all('div', attrs={'class': 'Article_Content'}):
        # print(item.get_text().strip().replace(' ', '').replace('个人简介：', '').replace('个人简介', '').replace('基本信息：',
        #                                                                                                 '').replace(
        #     '基本信息', '').encode('gbk', 'ignore').decode('gbk'))
        teachers.append(
            item.get_text().strip().replace(' ', '').replace('个人简介：', '').replace('个人简介', '').replace('基本信息：',
                                                                                                      '').replace(
                '基本信息', '').replace('学者网主页', '').encode('gbk', 'ignore').decode('gbk'))
    return


def write_file():
    """将introduction信息写teacher_information_other_test.json文件

    :return: 无
    """
    with open('teacher_information_other_test.json', 'w+', encoding='utf-8') as f:
        json_str = json.dumps(introduction, indent=4, ensure_ascii=False)  # 这就是为什么json文件中的问题，里面不是GBK
        f.write(json_str)
        f.write('\n')
    f.close()
    return


def create_excel(name):
    """将老师的中文名字写进teachers_name.xlsx文件中

    :param name: 老师的中文姓名list
    :return: 无
    """
    # 创建xls对象
    wb = Workbook()

    # 新增表单页
    sheet = wb.active

    # 写入数据
    label_name = ['姓名']

    # 转换格式
    teacher_name = np.array(name)
    sheet.append(label_name)
    for i in range(len(teacher_name)):
        temp_list = []
        temp_list.append(teacher_name[i])
        sheet.append(temp_list)

    wb.save('teachers_name.xlsx')
    return


def main():
    """main函数，调用内部或者外部的函数

    :return: 无
    """
    teacher = read_file()
    for i in teacher:
        soup = get_soup(i)
        soup_process(soup)

    # 这一块也是可以作为一个单独的功能，显得思路清晰
    for i in teachers:
        # 利用正则表达式获取老师的姓名，正则表达式处理后还不是一个String类型的，需要.group()才可以获取到信息
        pat = re.compile(r'[\u4e00-\u9fa5]*(?=\s*，|,)')
        teacher_name = pat.search(i).group()
        # print(teacher_name)
        name.append(teacher_name)
        introduction.append({
            "name": str(teacher_name),
            "introduction": str(i),
            "superior_administrative": "Nanjing University of Posts and Telecommunications",
            "second_administrative": "School of Modern Posts",
            "paper": None
        })
    create_excel(name)

    # 调用其他.py文件，先将老师的中文名字改成英文名字，进而获取老师的论文信息
    extraction_utils.util_function()
    extract_version_1.dblp_function(introduction)

    # 这一步其实里面很容易出问题，编码格式的问题就像赌博一样，不细心的话永远不知道那一次会没有报错
    write_file()
    return


if __name__ == '__main__':
    main()
