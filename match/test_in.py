# -*- coding:utf-8 -*-
# @Time    : 2022/4/17 18:57
# @Author  : Yinkai Yang
# @FileName: test_in.py
# @Software: PyCharm
# @Description: this is a program related to
import re
def main():
    # a = ['CHI(1)', 'CHII', 'CHI(2)', 'CHI']
    # b = 'CHI'
    # print(b in a)
    pat = re.compile(r'\w+')
    strs = 'WISE (1)'
    words = pat.findall(strs)
    print(words)
    return


if __name__ == '__main__':
    main()
