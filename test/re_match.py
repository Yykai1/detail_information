# -*- coding:utf-8 -*-
# @Time    : 2022/4/13 18:13
# @Author  : Yinkai Yang
# @FileName: re_match.py
# @Software: PyCharm
# @Description: this is a program related to 主要是进行会议期刊与老师会议信息的匹配，来判断这个会议是ABC类
import json
import sixtxt
import re

paper_from = []
area = ['期刊A类', '期刊B类', '期刊C类', '会议A类', '会议B类', '会议C类']


def read_json():
    """获得老师的所有论文会议信息的出处,每一个老师是一个单独的list
    此时需要对老师的期刊会议信息进行判断

    :return:
    """
    paper_temp = []
    with open('./all_information.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for i in range(len(json_data)):  # 老师数量外层循环
        for j in range(len(json_data[i]['paper'])):  # 老师的论文会议信息作为二层循环
            paper_temp.append(json_data[i]['paper'][j]['paper_from'])
        paper_from.append(paper_temp)  # 临时list存储一个老师的信息
    print(paper_from)  # 存储所有老师临时信息list的一个大list，实际上老师已经和下标对应起来了
    return


def regex_match(text):
    # 第一层循环，老师的数量
    for i in range(len(paper_from)):
        print('-----------------------------第' + str(i+1) + '个老师-----------------------------')
        # 二层循环，老师的作品数量
        for j in range(len(paper_from[i])):
            chars = str(paper_from[i][j])
            # print(chars)
            # 方法二：获得所有字母，每一个都进行匹配，只有都存在才可以操作
            pat = re.compile(r'\w+')
            words = pat.findall(chars)
            # print(words)
            # 寻找期刊会议ABC类
            for index in range(len(text)):
                # 寻找具体信息
                flag = True
                for number in range(len(text[index])):
                    for character in range(len(words)):
                        if words[character] not in text[index][number]:
                            flag = False
                            break
                        else:
                            continue
                    if not flag:
                        break
                    else:
                        print(paper_from[i][j], end='')
                        print('---------->', end='')
                        print(area[index % 6])
                        break
            """
            # 方法一：只匹配大写字母
            if len(str) > 8:
                # 正则表达式
                pat = re.compile(r'[A-Z]+')
                # 获取所有的大写字母并连接在一起
                str = ''.join(pat.findall(str))
            print(paper_from[i][j], end='')
            print('---------->', end='')
            # 寻找期刊会议ABC类
            for index in range(len(text)):
                # 寻找具体信息
                for number in range(len(text[index])):
                    # 如果匹配上就返回
                    if str in text[index][number]:
                        print(area[index % 6], end=',')
                        break
            print()
            """
    return


def main():
    read_json()
    # 这边就可以调用sixtxt获取到text这个list了
    text = sixtxt.get_text()
    regex_match(text)
    return


if __name__ == '__main__':
    main()
