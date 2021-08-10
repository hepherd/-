# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:51:40 2021

@author: yande
"""


import matplotlib.pyplot as plt
import pandas as pd
import os


plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

path = os.getcwd()
path = 'C:\\Users\\yande\\Desktop\\项目交付内容\\01.数据\\'
order = pd.read_csv(r"C:\Users\yande\Desktop\项目交付内容\01.数据\附件1.csv", sep = ',', encoding = 'gbk')
detail = pd.read_csv(r"C:\Users\yande\Desktop\项目交付内容\01.数据\附件2.csv", sep = ',', encoding = 'gbk')
order['支付时间'] = pd.to_datetime(order['支付时间'])

##按大类将数据分类
order_detail = pd.merge(order,detail, on=['商品'], how='left')
order_detail_1 = order_detail.loc[order_detail['大类']=='饮料',:]
order_detail_2 = order_detail.loc[order_detail['大类']=='非饮料',:]
Sc = order_detail_1['商品'].drop_duplicates()
Sc = Sc.reset_index(drop=True)
sc = order_detail_2['商品'].drop_duplicates()
sc = sc.reset_index(drop=True)

##按地点分类
def od(str):
    od =  order_detail.loc[order_detail['地点']==str,:]
    return od

def task(od1):
    od1_sn = []
    num1 = []
    for x in range(0,len(Sc)):
        od1_1 = od1.loc[od1['商品']==Sc[x],:]
        od1_sn.append(len(od1_1))
        num1.append(x+1)

    od1_ = pd.DataFrame({'序号':num1,'饮料类':Sc,'销售量':od1_sn})

    task1=list(od1_['销售量'])

    for i in range(len(task1)):
         if(task1[i] >=50):
                task1[i] = '热销'
         elif(task1[i] >=20):
                task1[i]='正常'
         else:
                task1[i]='滞销'
    od1_['cluster']=task1
    task1=od1_['饮料类']
    task2=od1_['cluster']
    task=pd.DataFrame({'饮料类':task1,'标签':task2})
    return task

def task2(od1,task):
    
    od1_sn1 = []
    num1_1 = []
    for x in range(0,len(sc)):
        od1_2 = od1.loc[od1['商品']==sc[x],:]
        od1_sn1.append(len(od1_2))
        num1_1.append(x+1)

    od1_ = pd.DataFrame({'序号':num1_1,'非饮料类':sc,'销售量':od1_sn1})

    task3=list(od1_['销售量'])

    for i in range(len(task3)):
         if(task3[i] >=50):
                task3[i] = '热销'
         elif(task3[i] >=20):
                task3[i]='正常'
         else:
                task3[i]='滞销'
    od1_['cluster']=task3
    task3=od1_['非饮料类']
    task4=od1_['cluster']
    task['非饮料类']=task3
    task['非饮料类销售情况']=task4
    return task

task(od('A')).to_csv(path+'task3-1A.csv',sep = ',',encoding='utf_8_sig',index=False)
task2(od('A'),task(od('A'))).to_csv(path+'task3-2A.csv',sep = ',',encoding='utf_8_sig',index=False)

task(od('B')).to_csv(path+'task3-1B.csv',sep = ',',encoding='utf_8_sig',index=False)
task2(od('B'),task(od('B'))).to_csv(path+'task3-2B.csv',sep = ',',encoding='utf_8_sig',index=False)

task(od('C')).to_csv(path+'task3-1C.csv',sep = ',',encoding='utf_8_sig',index=False)
task2(od('C'),task(od('C'))).to_csv(path+'task3-2C.csv',sep = ',',encoding='utf_8_sig',index=False)

task(od('D')).to_csv(path+'task3-1D.csv',sep = ',',encoding='utf_8_sig',index=False)
task2(od('D'),task(od('D'))).to_csv(path+'task3-2D.csv',sep = ',',encoding='utf_8_sig',index=False)

task(od('E')).to_csv(path+'task3-1E.csv',sep = ',',encoding='utf_8_sig',index=False)
task2(od('E'),task(od('E'))).to_csv(path+'task3-2E.csv',sep = ',',encoding='utf_8_sig',index=False)
