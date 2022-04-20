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
paper_number = []
paper_type = []
areas = ['计算机体系结构/并行与分布计算/存储系统', '计算机网络', '网络与信息安全',
         '软件工程/系统软件/程序设计语言', '数据库/数据挖掘/内容检索',
         '计算机科学理论', '计算机图形学与多媒体', '人工智能', '人机交互与普适计算', '交叉/综合/新兴']


def read_json():
    """获得老师的所有论文会议信息的出处,每一个老师是一个单独的list
    此时需要对老师的期刊会议信息进行判断

    :return:
    """
    paper_temp = []
    number_temp = []
    type_temp = []
    with open('data/paper_information.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for i in range(len(json_data)):  # 老师数量外层循环
        paper_temp = []
        number_temp = []
        type_temp = []
        count = 0
        for j in range(len(json_data[i]['paper'])):  # 老师的论文会议信息作为二层循环
            if json_data[i]['paper'][j]['paper_from'] not in paper_temp:
                # paper_temp.append(json_data[i]['paper'][j]['paper_from'])
                from_temp = json_data[i]['paper'][j]['paper_from']
                # print("original name: "+from_temp)
                from_temp = re.sub(r'\(.*\)', '', from_temp)
                from_temp = from_temp.split('/')[0]
                # print("      modified name: " + from_temp)
                paper_temp.append(from_temp.strip())
                number_temp.append(1)
                type_temp.append(json_data[i]['paper'][j]['paper_type'])
            else:
                index = paper_temp.index(json_data[i]['paper'][j]['paper_from'])
                number_temp[index] += 1
        paper_from.append(paper_temp)  # 临时list存储一个老师的信息
        paper_number.append(number_temp)
        paper_type.append(type_temp)
    # print(paper_from)  # 存储所有老师临时信息list的一个大list，实际上老师已经和下标对应起来了
    return


def regex_match(text):
    # 获得所有的字符串
    allnames = " ".join(text)
    # print("--------------")
    # print(allnames)
    reg = []
    # 第一层循环，老师的数量
    for i in range(len(paper_from)):
        print('--------------------------------------------第' + str(i + 1) + '个老师--------------------------------------------')
        # 二层循环，老师的作品数量
        for j in range(len(paper_from[i])):
            pfName = paper_from[i][j]
            pfType = paper_type[i][j]
            if pfType == 'Journal Articles':
                reg = pfName.replace(".", "[A-Z|a-z]+").replace(" ", "[ |-]")
                reg = "" + reg + "( Journal|\s|\(|（)"
            elif pfType == 'Conference and Workshop Papers':
                reg = "[（|\(]" + pfName + "[）|\)]"
            else:
                continue

            # print("dblp conf / jour name: " + pfName + " , type: " + pfType)
            # print("    pattern is:  " + str(reg))
            pat = re.compile(r'' + str(reg) + '')
            # If the text contains a journal or conference name from dblp, then locate its level
            if pat.search(allnames) != None:
                # print("locating ... ")
                for index2 in range(len(text)):
                    # print("search text : " + text[index])
                    res = pat.search(text[index2])
                    if (res != None):
                        level = judge_level(index2, pfType)
                        area = judge_area(index2)
                        if level != None:
                            print("dblp conf / jour name: " + pfName + " , type: " + pfType)
                            print("    pattern is:  " + str(reg))
                            print("    所属等级： " + level)
                            print("    研究领域： " + area)
                            break
    return


def judge_level(index, type):
    mod = index % 6
    level = None
    if mod == 0 and type == 'Journal Articles':
        level = "杂志A类"
    elif mod == 1 and type == 'Journal Articles':
        level = "杂志B类"
    elif mod == 2 and type == 'Journal Articles':
        level = "杂志C类"
    elif mod == 3 and type == 'Conference and Workshop Papers':
        level = "会议A类"
    elif mod == 4 and type == 'Conference and Workshop Papers':
        level = "会议B类"
    elif mod == 5 and type == 'Conference and Workshop Papers':
        level = "会议C类"
    return level


def judge_area(index):
    mod = index // 6
    area = areas[mod]
    return area


def main():
    read_json()
    # 这边就可以调用sixtxt获取到text这个list了
    text = sixtxt.get_text()
    regex_match(text)
    return


if __name__ == '__main__':
    main()
