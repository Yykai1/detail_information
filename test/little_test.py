# -*- coding:utf-8 -*-
# @Time    : 2022/4/13 20:28
# @Author  : Yinkai Yang
# @FileName: little_test.py
# @Software: PyCharm
# @Description: this is a program related to
import re
import string


def main():
    # 只对大写进行匹配
    str_source = 'Knowledge-Based Systems（KBS）   Elsevier   http://dblp.uni-trier.de/db/journals/kbs/'
    str_a = 'Knowl. Based Syst.'  # 直接利用in匹配的话结果是false
    # if len(str_a) > 4:
    str_b = 'KBS'
    # 第一种思路，肯定是不全的
    pat = re.compile(r'[A-Z]+')
    str_c = ''.join(pat.findall(str_a))
    print(str_c)

    print(str_a in str_source)
    print(str_b in str_source)
    print(str_c in str_source)
    return


if __name__ == '__main__':
    main()
