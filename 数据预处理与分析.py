# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 01:01:11 2021

@author: yande
"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

path = os.getcwd()
path = 'C:\\Users\\yande\\Desktop\\项目交付内容\\01.数据\\'
order = pd.read_csv(r"C:\Users\yande\Desktop\项目交付内容\01.数据\附件1.csv", sep = ',', encoding = 'gbk')
order['支付时间'] = pd.to_datetime(order['支付时间'])

def od(str):
    od =  order.loc[order['地点']==str,:]
    return od

od('A').to_csv(path+'task1-1A.csv',sep = ',',encoding='utf_8_sig',index=False) ##生成task1-1A.csv
od('B').to_csv(path+'task1-1B.csv',sep = ',',encoding='utf_8_sig',index=False) ##生成task1-1B.csv
od('C').to_csv(path+'task1-1C.csv',sep = ',',encoding='utf_8_sig',index=False) ##生成task1-1C.csv
od('D').to_csv(path+'task1-1D.csv',sep = ',',encoding='utf_8_sig',index=False) ##生成task1-1D.csv
od('E').to_csv(path+'task1-1E.csv',sep = ',',encoding='utf_8_sig',index=False) ##生成task1-1E.csv

def odt(od):
    odt = od[(od['支付时间'] >=pd.to_datetime('20170501')) & (od['支付时间'] <= pd.to_datetime('20170531'))]
    return odt


##每台售货机每月的每单平均交易额与日均订单量
j=0
month = [i.month for i in order['支付时间']]
w = ['售货机A','售货机B','售货机C','售货机D','售货机E']
detail = pd.DataFrame({'售货机':w})
for x in range(1,13):
    i = month.count(x)
    m=j+i
    order1 = order.iloc[j:m,:]
    def od1(str):
        od1 =  order1.loc[order1['地点']==str,:]
        return od1
    
    def money(str):
        return round(float(od1(str).agg({'实际金额':np.mean})),1)
    
    task1 = [money('A'),money('B'),money('C'),money('D'),money('E')]

    def day(str):
        day = [i.day for i in od1(str)['支付时间']]
        d = []
        for i in day:
            if i not in d:
               d.append(i)
        return int(len(day)/len(d))

    task2 = [day('A'),day('B'),day('C'),day('D'),day('E')]
    
    detail[str(x)+'月平均交易额'] = task1
    detail[str(x)+'月的日订单量'] = task2
    j = m
    
detail.to_csv(path+'每台售货机每月的每单平均交易额与日均订单量.csv',sep = ',',encoding='utf_8_sig',index=False)