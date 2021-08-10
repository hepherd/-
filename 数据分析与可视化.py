# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 01:01:11 2021

@author: yande
"""



from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.ticker import FuncFormatter
from numpy import mat
import seaborn as sns


plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

path = os.getcwd()
path = 'C:\\Users\\yande\\Desktop\\项目交付内容\\01.数据\\'
order = pd.read_csv(r"C:\Users\yande\Desktop\项目交付内容\01.数据\附件1.csv", sep = ',', encoding = 'gbk')
order['支付时间'] = pd.to_datetime(order['支付时间'])

##绘制2017年6月销量前5的商品销量柱状图
j=0
month = [i.month for i in order['支付时间']]
for x in range(1,7):
    i = month.count(x)
    m=j+i-1
    order1_1 = order.loc[j:m,:]
    j = i+j

sale = [i for i in order1_1['商品']]##提取商品列

arry = [elem for elem, _ in Counter(sale).most_common()]

values = (sale.count(arry[0]),sale.count(arry[1]),sale.count(arry[2]),sale.count(arry[3]),sale.count(arry[4])) 
plt.figure(figsize=(12,10))
plt.bar(np.arange(5), values, 0.5, color="#87CEFA") 
plt.xlabel('商品')
plt.ylabel('销量') 
plt.title('2017年6月销量前五商品') 
plt.xticks(np.arange(5) ,(arry[0], arry[1], arry[2], arry[3], arry[4])) 
plt.yticks(np.arange(0, int(sale.count(arry[0])), 100)) 

for i in range(len(values)):
    plt.text(i, values[i], values[i], va='bottom', ha='center')
    
plt.savefig(path+'2017年6月销量前五商品直方图.png')
plt.show()


##绘制每台售货机每月总交易额折线图
plt.figure(figsize=(8,7))

def mon(str):
    n=0
    mon = []
    month = [i.month for i in order['支付时间']]
    for x in range(1,13):
        i = month.count(x)
        m=n+i
        order1 = order.iloc[n:m,:]
        def od1(str):
            od1 =  order1.loc[order1['地点']==str,:]
            return od1
        def money(str):
            return round(float(od1(str).agg({'实际金额':np.sum})),1)
        mon.append(money(str))
        n = m
    return mon

plt.plot(np.arange(12),mon('A'),'bs-',
       np.arange(12),mon('B'),'ro-.',
       np.arange(12),mon('C'),'gH--',
       np.arange(12),mon('D'),'ys--',
       np.arange(12),mon('E'),'mH-.')

plt.xlabel('月份')## 添加横轴标签
plt.ylabel('交易额（元）')## 添加y轴名称
plt.xticks(np.arange(12) ,('一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'))
plt.title('每台售货机每月总交易额')## 添加图表标题
plt.legend(['A','B','C','D','E'])
plt.savefig(path+'每台售货机每月总交易额折线图.png')
plt.show()


##绘制各售货机的月环比增长率直方图
def turn_percentage(x):
    return '%.2f%%' % (x * 100);

def to_percent(temp, position):
    return '%10.0f'%(100*temp) + '%'

def momg(str):
    mon1 =[]
    for x in range(0,11):
        mon1.append(round((((mon(str)[x+1]-mon(str)[x])/mon(str)[x])),2))
    
    plt.figure(figsize=(8,7))
    plt.bar(np.arange(11), mon1, 0.5, color="#87CEFA") 
    plt.xlabel('月份')
    plt.ylabel('增长率（%）') 
    plt.title('售货机'+str+'的月环比增长率') 
    plt.xticks(np.arange(11) ,('一月~二月','二月~三月','三月~四月','四月~五月','五月~六月','六月~七月','七月~八月','八月~九月','九月~十月','十月~十一月','十一月~十二月'),rotation=45) 
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

    for i in range(11):
        plt.text(i, mon1[i], turn_percentage(mon1[i]), va='bottom', ha='center')
    
    plt.savefig(path+'售货机'+str+'的月环比增长率直方图.png')
    plt.show()

momg('A')
momg('B')
momg('C')
momg('D')
momg('E')

detail = pd.read_csv(r"C:\Users\yande\Desktop\项目交付内容\01.数据\附件2.csv", sep = ',', encoding = 'gbk')

##按大类分类
order_detail = pd.merge(order,detail, on=['商品'], how='left')
order_detail_1 = order_detail.loc[order_detail['大类']=='饮料',:]
order_detail_2 = order_detail.loc[order_detail['大类']=='非饮料',:]

profit = round(order_detail_1.agg({'实际金额':np.sum})/4,1)+round(order_detail_2.agg({'实际金额':np.sum})/5,1)

def od1(str):
        od1 =  order_detail_1.loc[order_detail_1['地点']==str,:]
        return od1
def od2(str):
        od2 =  order_detail_2.loc[order_detail_2['地点']==str,:]
        return od2
def money1(str):
    return round(float(od1(str).agg({'实际金额':np.sum}))/4,2)
def money2(str):
    return round(float(od2(str).agg({'实际金额':np.sum}))/5,2)
    
##求每台售货机毛利润占总毛利润比例
profit1 = money1('A')+money2('A')
profit2 = money1('B')+money2('B')
profit3 = money1('C')+money2('C')
profit4 = money1('D')+money2('D')
profit5 = money1('E')+money2('E')

##绘制每台售货机毛利润占总毛利润比例饼图
plt.figure(figsize=(6,6))
label= ['A','B','C','D','E']
explode = [0.01, 0.01, 0.01, 0.01, 0.01]
plt.pie((profit1,profit2,profit3,profit4,profit5), explode=explode, labels=label, autopct='%1.1f%%')

plt.title('每台售货机毛利润占总毛利润比例')
plt.savefig(path+'每台售货机毛利润占总毛利润比例饼图')
plt.show()



Sc = detail['二级类'].drop_duplicates()
Sc = Sc.reset_index(drop=True)

##提取二级类种类
z = 0
M =  []
for x in range(1,13):
    i = month.count(x)
    m=z+i
    order2 = order_detail.iloc[z:m,:]
    for y in range(0,len(Sc)):
        order2_1 = order2.loc[order2['二级类']==Sc[y],:]
        M.append(round(float(order2_1.agg({'实际金额':np.mean})),2))
    z = m

##使横纵轴长度一致
month1 = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
Mon = []
for i in range(0,len(Sc)):
    for j in range(0,12):
        Mon.append(month1[j])

cate = []
for i in range(0,12):
    for j in range(0,len(Sc)):
        cate.append(Sc[j])

data = pd.DataFrame({'月份':Mon,'二级类':cate,'每月交易额均值':M})

##绘制每月交易额均值气泡图
plt.figure(figsize=(10,10))
size=data['每月交易额均值'].rank()
n=20
colors = np.random.rand(len(Sc)*12)
plt.scatter(data['月份'],data['二级类'],s=size*n, c=colors,alpha=0.6)
plt.savefig(path+'每月交易额均值气泡图')
plt.show()


##提取售货机C的某月数据
order3 = order_detail.loc[order_detail['地点']=='C',:]
order3 = order3.reset_index(drop=True)
def od3(y):
    od3 = order3[(order3['支付时间'] >=pd.to_datetime('20170'+str(y)+'01')) & (order3['支付时间'] <= pd.to_datetime('20170'+str(y)+'30'))]
    od3 = od3.reset_index(drop=True)
    return od3

def transformMatrix(m):
    
    return np.transpose(m).tolist()

##绘制售货机C订单量热力图
def hot(y):
    
    c = 0
    day1 = [i.day for i in od3(y)['支付时间']]
    data1 = []
    for x in range(1,31):
        i = day1.count(x)
        m=c+i
        dayorder1 = od3(y).iloc[c:m,:]
        c = m
    
        hour1 = [i.hour for i in dayorder1['支付时间']]
        num1 = []
    
        for x in range(0,24):
            num1.append(hour1.count(x))
    
        data1.append(num1)
    A = mat(data1)

    df1 = pd.DataFrame(transformMatrix(A), 
                      index=[i for i in range(1,25)],#DataFrame的行标签设置为大写字母
                      columns=[i for i in range(1,31)])#设置DataFrame的列标签
    plt.figure(dpi=360)
    sns.heatmap(data=df1,
                cmap=plt.get_cmap('Greens'),#matplotlib中的颜色盘'Greens'
                )
    plt.savefig(path+'售货机C'+str(y)+'月订单量热力图')
    plt.show()
hot(6)
hot(7)
hot(8)