# -*- coding:utf-8 -*-
# @Time    : 2022/3/20 14:01
# @Author  : Yinkai Yang
# @FileName: extraction_utils.py
# @Software: PyCharm
# @Description: this is a program related to
import pandas as pd
from pypinyin import lazy_pinyin


def write_file(teachers):
    """写文件，向teacher.txt文件中写入老师的英文名字

    :param teachers: 老师的英文名字列表list
    :return: 无
    """
    count = 0
    with open("teacher.txt", "w+") as f:
        for i in teachers:
            f.write(i)
            count = count + 1
            if count != len(teachers):
                f.write('\n')
    f.close()
    return


def util_function():
    """从teaches_name.xlsx文件中读取老师的中文名字，转换成英文。
    这边功能有点杂糅，可以把将数据处理定义为一个函数（略过此操作）

    :return: 无
    """
    teachers_list = []
    ex = pd.read_excel("teachers_name.xlsx")
    for i in ex['姓名']:
        name_list = lazy_pinyin(i)

        first_name = name_list[0]
        last_name_list = name_list[1:]
        last_name = ""
        for character in last_name_list:
            last_name = last_name + character

        en_name = last_name.capitalize() + "_" + first_name.capitalize()
        teachers_list.append(en_name)
    write_file(teachers_list)
    return

