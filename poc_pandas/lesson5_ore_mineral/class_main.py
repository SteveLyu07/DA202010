import os
import pandas as pd 
import copy

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


        #将读取的df存入类的自有属性
        self.conversion_data = copy.deepcopy(df)
        return

if __name__ == '__main__':
    
    om = OreMineral() #生成类
    om.read_ore_data()
    print(om.ore_data)

    om.read_mineral_data()
    print(om.mineral_data)

    om.read_conversion_data()
    print(om.conversion_data)