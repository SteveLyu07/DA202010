import os
import pandas as pd

# path = os.path.realpath(os.curdir)  # 获取当前目录的绝对路径
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = path + "/poc_pandas/data/lesson4_data.xlsx"  # 加上文件名
print('reading excle file from:', excelpath)


#try(1) 读取excel的第一张表单
print("\n---try(1)---")
df = pd.read_excel(excelpath)
print(df)
print(df.info())

#try(2) 加权平均值
#list 方法
print("\n---try(2)(1)---")
list_data = df['price'].values.tolist()
sum=0.0
for p in list_data:
    sum += p
avg = sum / len(list_data)
print('price sum is %0.2f, average price is %0.2f'%(sum,avg))

#series
print("\n---try(2)(2)---")
sum = df['price'].sum()
avg = df['price'].mean()
print('price sum is %0.2f, average price is %0.2f'%(sum,avg))

#try(3) 过滤出符合条件的订单
#数值型过滤
print("\n---try(3)(1)---")
dumy_order1 = df.query('0<price<8 or 50<price')
print(dumy_order1)

#bool型过滤 | for or; & for and; ~ for not
print("\n---try(3)(2)---")
buy_order = df[~df['bid']]
print(buy_order)

#日期型过滤
print("\n---try(3)(3)---")
df = df.set_index('issueDate') #设置index
yesterday_order = df.loc['2020-9'] #location
print(yesterday_order)

#try(4) 删除无效订单重新计算平均价格
print("\n---try(4)---")
df = df.drop(
    df[(df.price<8) |
    (df.price>50)].index
)
print(df)
sum = df['price'].sum()
avg = df['price'].mean()
print('price sum is %0.2f, average price is %0.2f'%(sum,avg))

#try(5) 计算订单总量与被满足量
print("\n---try(5)---")
sum_volEntered = df['volEntered'].sum()
sum_volRemaining = df['volRemaining'].sum()
print('volEntered:%0.2f\n'%sum_volEntered)
print('volRemaining:%0.2f\n'%sum_volRemaining)
print('volSatisfied:%0.2f\n'%(1-sum_volRemaining/sum_volEntered))
