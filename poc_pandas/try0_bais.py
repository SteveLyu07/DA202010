# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)----------------------------------
# author by : （学员ID)
# created:  2020.9

# Description:
#   pandas 技术验证用
#   各类基本技巧的练习
# ------------------------(max to 80 columns)----------------------------------

import os
import pandas as pd

# Try(1) 创建一个系列并输出
print('\n---Make a numberic series---')
s = pd.Series([1, 2, 3, 4, 5, 6])
print(s)

'''
该函数主要用于生成一个固定频率的时间索引，在调用构造方法时，
必须指定start、end、periods中的两个参数值，否则报错。
主要参数说明：
periods：固定时期，取值为整数或None
freq：日期偏移量，取值为string或DateOffset，默认为'D'
其他参数（部分）
normalize：若参数为True表示将start、end参数值正则化到午夜时间戳
name：生成时间索引对象的名称，取值为string或None
'''
# start、end、periods、freq
print('\n---Make a date series---')

dates = pd.date_range('20200101', periods=6)
print(dates)

dates = pd.date_range(start='20200101', end='20201231', freq='30D')
print(dates)

# Try(2) 创建一个Dataframe：
print('\n---Read a specified row from dataframe ---')
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  #index=['cobra', 'viper', 'sidewinder'],
                  #columns=['max_speed', 'shield'])
                  columns = ['班级','姓名'])
print(df)


# Try(3) 从csv文件中直接读取系列
print('\n---Make a datafram from csv file---')
path = os.path.realpath(os.curdir)  # 获取当前目录的绝对路径
csvpath = path + "\\poc_pandas\\data\\try3-ANSI.csv"  # 加上文件名

# 遇到文件或路径名中带有中文，则需要改成如下方式
f = open(csvpath)
df = pd.read_csv(f, encoding='utf-8')
print(df)
f.close()

# Try(4) 快速查看 DataFrame
print('\n---Quick check dataframe---')
print('DataFrame 的形状是：', df.shape)
print('DataFrame 总行数是', len(df))
print('DataFrame 各列名稱：', df.columns)

# Head 与 Tail
# head() 与 tail() 用于快速预览 Series 与 DataFrame，
# 默认显示 5 条数据，也可以指定显示数据的数量。
print('\n---Head n rows---')
print(df.head(3))
print('\n---Tail n rows---')
print(df.tail(1))

# 從 Dataframe 中获取series
print('\n---Get series from dataframe---')
s = df['title']
print(s)
print(type(s))
print(type(df))

# Try(5) 排序
print('\n---Sort a dataframe ---')
df_sorted = df.sort_values(by='col2', ascending=False)
print(df_sorted)