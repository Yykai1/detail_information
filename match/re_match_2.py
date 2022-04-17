# -*- coding:utf-8 -*-
# @Time    : 2022/4/17 17:52
# @Author  : Yinkai Yang
# @FileName: re_match_2.py
# @Software: PyCharm
# @Description: this is a program related to
import json
import sixtxt
import re

paper_from = []
paper_number = []
paper_type = []
area = ['期刊A类', '期刊B类', '期刊C类', '会议A类', '会议B类', '会议C类']


def read_json():
    """获得老师的所有论文会议信息的出处,每一个老师是一个单独的list
    此时需要对老师的期刊会议信息进行判断

    :return:
    """
    paper_temp = []
    number_temp = []
    type_temp = []
    with open('paper_information_1.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for i in range(len(json_data)):  # 老师数量外层循环
        paper_temp = []
        number_temp = []
        type_temp = []
        count = 0
        for j in range(len(json_data[i]['paper'])):  # 老师的论文会议信息作为二层循环
            if json_data[i]['paper'][j]['paper_from'] not in paper_temp:
                paper_temp.append(json_data[i]['paper'][j]['paper_from'])
                number_temp.append(1)
                type_temp.append(json_data[i]['paper'][j]['paper_type'])
            else:
                index = paper_temp.index(json_data[i]['paper'][j]['paper_from'])
                number_temp[index] += 1
        paper_from.append(paper_temp)  # 临时list存储一个老师的信息
        paper_number.append(number_temp)
        paper_type.append(type_temp)
    for i in range(len(paper_from)):
        print(paper_from[i])
    # print(paper_from)  # 存储所有老师临时信息list的一个大list，实际上老师已经和下标对应起来了
    return


def data_process(i, j, flag, text, index, words):
    for number in range(len(text[index])):
        for character in range(len(words)):
            if words[character] not in '0123456789':
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
    return


def regex_match(text):
    # 现在老师的论文信息已经进行了精简。增加了去重和统计的操作
    # 老师的数量
    for i in range(len(paper_from)):
        print('-----------------------------第' + str(i + 1) + '个老师-----------------------------')
        # 去重后的论文出处信息
        for j in range(len(paper_from[i])):
            chars = str(paper_from[i][j])
            types = str(paper_type[i][j])
            pat = re.compile(r'\w+')
            words = pat.findall(chars)
            if types[0] == 'J':
                # 寻找期刊会议ABC类
                for index in range(len(text)):
                    # 寻找具体信息
                    flag = True
                    if index % 6 <= 2:
                        # 下面这个模块其实是重复的操作，可以放进一个模块里减少重复率
                        data_process(i, j, flag, text, index, words)

            if types[0] == 'C':
                # 寻找期刊会议ABC类
                for index in range(len(text)):
                    # 寻找具体信息
                    flag = True
                    if index % 6 >= 3:
                        data_process(i, j, flag, text, index, words)
    """
    第二种方法：
    # 第一层循环，老师的数量
    for i in range(len(paper_from)):
        print('-----------------------------第' + str(i + 1) + '个老师-----------------------------')
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

    return


def main():
    read_json()
    # 这边就可以调用sixtxt获取到text这个list了
    text = sixtxt.get_text()
    regex_match(text)
    return


if __name__ == '__main__':
    main()
