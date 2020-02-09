# -*- coding: utf-8 -*-
import numpy as np
import  matplotlib.pyplot as plt
import  matplotlib as mat
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html")
r.raise_for_status()
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text)
trs=soup.find_all('tr',class_='alt')
m1=[]
m2=[]
m3=[]
for tr in trs:
    tds=tr.find_all('td')
    if tds[1].string == '南昌大学' :
       m1.append(float(tds[3].string))
       m1.append(float(tds[4].string))
       m1.append(float(tds[5].string.strip('%')))
       m1.append(float(tds[9].string))
    elif tds[1].string == '华东交通大学':
        m2.append(float(tds[3].string))
        m2.append(float(tds[4].string))
        m2.append(float(tds[5].string.strip('%')))
        m2.append(float(tds[9].string))
    elif tds[1].string == '江西理工大学':
        m3.append(float(tds[3].string))
        m3.append(float(tds[4].string))
        m3.append(float(tds[5].string.strip('%')))
        m3.append(float(tds[9].string))
mat.rcParams['font.sans-serif']=['SimHei']
ind = np.arange(len(m1))
width = 0.3
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width,m1, width, yerr=None,  label='南昌大学')
rects2 = ax.bar(ind ,m2, width, yerr=None,label='华东交通大学')
rects3 = ax.bar(ind+width,m3, width, yerr=None,label='江西理工大学')
ax.set_ylabel('数量，分数或百分比')
ax.set_title('三校比较')
ax.set_xticks(ind)
ax.set_xticklabels(('总分（分）', '生源质量（分）', '培养结果（百分之）', '顶尖成果（篇）'))
ax.legend()
def autolabel(rects,xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
