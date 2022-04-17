text = []


def read_source():
    '''主要是利用汉字长度为4进行一个简单判断，领域信息一共9个，我们不需要做过多考虑，可以把领域信息删掉
    每次读到长度为4的行时，创建一个list或者是list置空 && 把list放进text中，做到这里才仅仅是把所有期刊和会议的ABC作为列表，一共54条，0~53
    而期刊A总是出现在0，6，12，位置上，做一个循环把类似位置上的放进一个list就行了

    :return:
    '''
    with open('../../old/paper_number/source.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        list = []
        for i in lines:
            temp = i.rstrip('\n')
            if len(temp) == 4:
                if len(list) != 0:  # list为空不添加
                    text.append(list)  # 添加进text
                    list = []  # list置空
            else:
                list.append(temp)
        text.append(list)  # 由于循环的原因，最后一次的list未添加进去，补充即可


# def print_list():
#     '''结构信息的测试，一共54个list，0~53，结果没有问题，剩下的问题学姐自己处理吧
#
#     :return:
#     '''
#     count = 0
#     for i in text:
#         print(count)
#         print(i)
#         count += 1
#         print('\n')


def get_text():
    read_source()
    # print_list()
    print(text)
    return text

