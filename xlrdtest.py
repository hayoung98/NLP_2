import xlrd
from array import *

dic = {'0':"前10%",'1':"10% ~ 20%",'2':"20% ~ 30%",'3':"30% ~ 40%",'4':"40% ~ 50%",'5':"50% ~ 60%",'6':"60% ~ 70%",'7':"70% ~ 80%",'8':"80% ~ 90%",'9':"90% ~ 100%",}

def Myprint(list):
    for i in range(len(list)):
        print(list[i],end="、")
    print("")

def Range(a):  # 把str格式的趴數轉成int格式的range ex."94.56%" -> 9
    return (int(float(a[:-1])//10))

def Compare(load_list):
    wb = xlrd.open_workbook("104.xls")
    sheet_0 = wb.sheet_by_index(0)

    range_list = []  # [0,0,0,1,1,2,2,......]
    for i in range(2721):
        range_list.append(Range(sheet_0.cell_value(i + 1, 5)))

    B = []
    for i in range(10):
        B.insert(i,[])

    print("\n---------------------統計---------------------")
    for i in range(2721):
        if sheet_0.cell_value(i+1,1) in load_list:  #從字頻表第一字開始比對，有無出現在文章中。
            index = Range(sheet_0.cell_value(i+1,5))
            B[int(index)].append(sheet_0.cell_value(i+1,1))
    for dic_r in range(10):
        range_name = dic.get(str(dic_r))
        range_count = range_list.count(dic_r)
        use_count = len(B[dic_r])
        b = B[dic_r]
        print("在 %s 的 %d 個字中共出現 %d 個字，分別為："%(range_name,range_count,use_count),end=' ')
        Myprint(b)
