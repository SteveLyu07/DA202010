import os
import pandas as pd 
import copy
import matplotlib.pyplot as plt

from mod_market import get_ore_price,get_mineral_price

ore_data_file = 'EVE标准矿石utf8.csv'
mineral_data_file = 'EVE标准矿物utf8.csv'
conversion_data_file = 'EVE标准矿石-标准矿物-产出换算utf8.csv'

class OreMineral:
    def __init__(self):
        #self.ore_data = None
        return

    def read_ore_data(self):
        '读取EVE矿石信息'

        print("\n ---read ore data---")
        path = os.path.realpath(os.curdir)
        csvpath = path + "/poc_pandas/data/" + ore_data_file # 加上文件名

        f = open(csvpath)
        df = pd.read_csv(f,encoding='utf-8')
        #print(df)
        f.close()

        del(df['mass'])
        del(df['capacity'])
        df = df.set_index('oreID')

        #将读取的df存入类的自有属性
        self.ore_data = copy.deepcopy(df)

        return

    def read_mineral_data(self):
        print("\n ---read mineral data---")
        path = os.path.realpath(os.curdir)
        csvpath = path + "/poc_pandas/data/" + mineral_data_file # 加上文件名

        f = open(csvpath)
        df = pd.read_csv(f,encoding='utf-8')
        #print(df)
        f.close()

        del(df['mass'])
        del(df['capacity'])
        df = df.set_index('mineralID')

        #将读取的df存入类的自有属性
        self.mineral_data = copy.deepcopy(df)
        return

    def read_conversion_data(self):
        print("\n ---read conversion data---")
        path = os.path.realpath(os.curdir)
        csvpath = path + "/poc_pandas/data/" + conversion_data_file # 加上文件名

        f = open(csvpath)
        df = pd.read_csv(f,encoding='utf-8')
        #print(df)
        f.close()

        self.ore_data = copy.deepcopy(df)


        #将读取的df存入类的自有属性
        self.conversion_data = copy.deepcopy(df)
        return

    def add_ore_price(self):
        prices = []

        for index,row in self.ore_data.iterrows():
            #获取矿石市场价格
            ore_price = get_ore_price(index)
            prices.append(ore_price)

        self.ore_data['price'] = prices

        return

    def cal_ore_value1(self):
        '计算3000单位的价值'
        ore_values = []
        ores = self.ore_data._stat_axis.values.tolist()
        '获取df的index'
        print('---ores---')
        print(ores)

        for ore in ores:
            value = 0.0
            #获取某个矿石的提炼信息，存入临时df
            df = self.conversion_data[
                (self.conversion_data['oreID'] == ore)
            ]
            #print(df)

            for index,row in df.iterrows():
                #获取可提取矿物数量，并计算累加价格
                print(index,row['oreVolume'],row['mineralID'],
                    row['extractQuantity'])
                value += row['extractQuantity'] * \
                get_mineral_price(int(ow['mineralID']))
                #反斜杠是表示下一行是一起的
                print('---value---')
                print(value)
            
            ss = df['orePortionSize']
            orePortionSize = ss.unique()
            print('---orePortionSize---')
            print(orePortionSize)

            if orePortionSize[0] == 1 :
                ore_values.append(value*3000)
            elif orePortionSize[0] == 15 :
                ore_values.append(value*200)
            elif orePortionSize[0] == 100 :
                ore_values.append(value*30)
            elif orePortionSize[0] == 1000 :
                ore_values.append(value*3)
        #循环结束
        #将矿石价值（series)添加到 ore_data中去（还没写）
        self.ore_data['value3000units'] = ore_values


        #只取出矿石名与价值并绘制图形
        ss_name = self.ore_data['oreNameZh']
        ss_value = self.ore_data['value3000units']

        df_value = pd.DataFrame.from_dict(
            {'oreNameZh':ss_name,
                'value3000units':ss_value
            }
        )
        print(df_value)
        self.draw_df(df_values)


    def draw_df(self,df):
        #直方图（纵向）
        #plt.plot.bar()
        #plt.show()

        #图形美化
        plt.rcParms['font.sans-serif'] = ['KaiTi']#字体楷体
        plt.rcParms['axes.unicode_minus'] = False #解决负号显示为方块的问题？

        #剔除高密度
        df = df[~
            df['oreNameZh'].str.contains('高密度')
        ]# 符号‘~’表示‘不包含’

        #排序
        df = df.set_index['oreNameZh']
        df.plot.barh()
        plt.show()

    

if __name__ == '__main__':
    
    om = OreMineral() #生成类
    om.read_ore_data()
    print(om.ore_data)

    om.read_mineral_data()
    print(om.mineral_data)

    om.read_conversion_data()
    print(om.conversion_data)

    om.add_ore_price()

    om.cal_ore_value1()

    #om.draw_df(om.ore_data)
