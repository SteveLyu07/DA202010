# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)----------------------------------
# author by : （学员ID)
# created:  2020.9

# Description:
#   pandas 技术验证用
#   各类基本技巧的练习
# 注：需安裝 pip install xlrd
# ------------------------(max to 80 columns)----------------------------------

import os
import pandas as pd

# path = os.path.realpath(os.curdir)  # 获取当前目录的绝对路径
print("\n---try(2)---")
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = path + "/poc_pandas/data/DataOfExcel.xlsx"  # 加上文件名
print('reading excle file from:', excelpath)


#try(1) 读取excel的第一张表单
df = pd.read_excel(excelpath)
print(df)

#try(2) 读取excel的指定表单
print("\n---try(2)(1)---")
df = pd.read_excel(excelpath,sheet_name='ShuHu108People')
print(df)

print("\n---try(2)(2)---")
df = pd.read_excel(excelpath,sheet_name=[0,1])
print(df)

#try(3)
print("\n---try(3)---")
df = pd.read_excel(excelpath,sheet_name=['Students'],usecols=[2,3],skiprows=[0])
print(df)

#try(4)
print("\n---try(3)---")
df = pd.read_excel(excelpath,sheet_name=['Students'],usecols=[2,3],skiprows=[0])
print(df)

OrderedDict(
    [('Students',xxxxx)]
)

print("\n***changed dataframe***")
df2 = pd.DataFrame(df['Students'])
#纯粹的dataframe



 


