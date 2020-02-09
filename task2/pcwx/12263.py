# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import  matplotlib as mat
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html")
r.raise_for_status()
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text)
trs=soup.find_all('tr',class_='alt')
mat.rcParams['font.sans-serif']=['SimHei']
labels=[]
size=[]
for tr in trs:
    tds=tr.find_all('td')
    if tds[2].string == '江西':
       labels.append(tds[1].string)
       size.append(float(tds[9].string))
print(labels)
print(size)
num=0.0
sizes=[]
for i in range(len(size)):
     num=float(num)+size[i]
print(num)
for i in range(len(size)):
     sizes.append(str(size[i]/num))
print(sizes)
explode=(0,0,0,0,0,0.1,0,0,0,0,0,0,0,0,0,0,0)
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.legend()
plt.show()

