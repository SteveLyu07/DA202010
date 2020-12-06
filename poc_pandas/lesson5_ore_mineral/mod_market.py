import random
import os
import pandas as pd

ore_price_data_file = 'EVE标准矿石-模拟市场价格.csv'
mineral_price_data_file = 'EVE标准矿物-模拟市场价格.csv'

def read_ore_price_data():

    path = os.path.realpath(os.curdir)
    csvpath = path + "/poc_pandas/data/" + ore_price_data_file 

    f = open(csvpath)
    df = pd.read_csv(f, encoding = 'utf-8')
    f.close()
    return df

def get_ore_price(id):

    df = read_ore_price_data()
    #print(df)
    df = df[(df['typeID'] == id)]
    #print(df)
    #price = df['median'].mean()
    p1 = df['median'].min()
    p2 = df['median'].max()

    price = random.uniform(p1,p2)

    df2 = df[df['bid'] == 0]
    #print(df2)
    price = df2['min'].mean()

    
    return price

def get_mineral_price(id):

    price = 0.0

    if id == 34:
        price = 15
    elif id == 35:
        price = random.uniform(10.70*0.95, 10.70*1.05)
    elif id == 36:
        price = random.uniform(190, 210)
    elif id == 37:
        price = random.uniform(100, 120)
    elif id == 38:
        price = random.uniform(100, 120)
    elif id == 39:
        price = random.uniform(1000,1100)
    elif id == 40:
        price = random.uniform(1300,1500)
    elif id == 11399:
        price = random.uniform(13000,15000)
    elif id == 48927:
        price = random.uniform(140000, 160000)
    
    return price

if __name__ == '__main__':

    mineral_id = 35
    print('模拟动态获取矿物(%d)价格-------' % mineral_id)
    for i in range(5):
        p = get_mineral_price(mineral_id)
        print(p)

    ore_id = 18
    print('模拟动态获取矿石（%d)价格-------' % ore_id)
    for i in range(5):
        p = get_ore_price(ore_id)
        print(p)
