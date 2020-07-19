import jieba
from collections import Counter
import re
import xlrdtest

def remove_punctuation(line):
    rule = re.compile(u"[^\u4e00-\u9fa5]")  # 只留下中文字
    line = rule.sub('',line)
    return line

if __name__ == '__main__':
    f = open("report2.txt","r")

    once_list = []  # 不存重複字
    mul_list = []  # 可存重複字
    for line in f:
        line = remove_punctuation(line)
        seg_list = jieba.lcut(line, cut_all=False)
        for i in seg_list:
            for j in i:
                if j not in once_list:
                    once_list.append(j)
                mul_list.append(j)
    print("文章使用的字：",end='')
    xlrdtest.Myprint(once_list)
    xlrdtest.Compare(once_list)

    c = Counter(mul_list)
    print("使用字數統計：")
    print(c)
    # print("總字數：",sum(c.values()))

    f.close()




