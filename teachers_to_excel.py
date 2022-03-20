# -*- coding:utf-8 -*-
# @Time    : 2022/3/20 19:36
# @Author  : Yinkai Yang
# @FileName: teachers_to_excel.py
# @Software: PyCharm
# @Description: this is a program related to
import json
import re
import requests
from bs4 import BeautifulSoup

teachers = []
name = []
introduction = []


def read_file():
    with open('teachers_page.txt', 'r', encoding='utf-8') as f:
        tmp = []
        lines = f.readlines()

        for i in lines:
            tmp.append(i.rstrip('\n'))
        f.close()
        return tmp


def get_soup(url):
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


def soup_easy(soup):
    # 通过soup进行操作，这里才是操作的关键
    for item in soup.find_all('div', attrs={'class': 'Article_Content'}):
        # print(item.get_text().strip().replace(' ', '').replace('个人简介：', '').replace('个人简介', '').replace('基本信息：', '').replace('基本信息', '').encode('gbk', 'ignore').decode('gbk'))
        teachers.append(item.get_text().strip().replace(' ', '').replace('个人简介：', '').replace('个人简介', '').replace('基本信息：', '').replace('基本信息', '').encode('gbk', 'ignore').decode('gbk'))
    return


def write_file():
    with open('teacher_information_other_test.json', 'w+', encoding='gbk') as f:
        json_str = json.dumps(introduction, indent=4, ensure_ascii=False)  # 这就是为什么json文件中的问题，里面不是GBK
        f.write(json_str)
        f.write('\n')
    f.close()
    return


def create_excel():

    return


def main():
    teacher = read_file()
    for i in teacher:
        soup = get_soup(i)
        soup_easy(soup)
    # write_file()
    for i in teachers:
        # 可以单独写成一个函数，放在这里没有必要
        pat = re.compile(r'[\u4e00-\u9fa5]*(?=\s*，)')
        teacher_name = pat.search(i).group()
        introduction.append({
            "name": str(teacher_name),
            "introduction": i,
            "superior_administrative": None,
            "second_administrative": None,
            "paper": None
        })
    write_file()
    create_excel()
    return


if __name__ == '__main__':
    main()
