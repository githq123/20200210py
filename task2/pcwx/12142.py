# -*- coding: utf-8 -*-
from wxpy import *
import numpy as np
import  matplotlib.pyplot as plt
import  matplotlib as mat
from pyecharts import Map
def robot_login():
    bot=Bot(cache_path=True)
    #bot.self.send('Hello,robot')
    #bot.file_helper.send('发送给文件助手的信息')
    #bot.chats()
    friends=bot.friends()
    friends_info=friends.stats_text()
    print(friends_info)
   # myfriend=bot.friends().search('H.')[0]
    #myfriend.send('hello,i am a robot')
    #myfriend.send_image('a.png')
def drawFriendsPie():
    mat.rcParams['font.sans-serif']=['SimHei']
    labels=['男性','女性','未知']
    sizes=[57.1,32.2,10.7]
    explode=(0,0.1,0)
    fig1,ax1=plt.subplots()
    ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal')
    plt.legend()
    plt.show()
def drawFriendsBarProvince():
    mat.rcParams['font.sans-serif'] = ['SimHei']
    n_groups=5
    city_weight=(10.2,8.98,8.57,2.04,2.04)
    fig,ax=plt.subplots()
    index=np.arange(n_groups)
    bar_width=0.35
    opacity=0.4
    error_config={'ecolor':'0.3'}
    rects1=ax.bar(index,city_weight,bar_width,alpha=opacity,color='b',error_kw=error_config,label='城市')
    ax.set_xlabel('城市名称')
    ax.set_ylabel('数据占比（%）')
    ax.set_title('好友城市TOP5')
    ax.set_xticks(index+bar_width/2)
    ax.set_xticklabels(('菏泽','赣州','济宁','济南','Melbourne'))
    ax.legend()
    fig.tight_layout()
    plt.show()
def main():
    robot_login()
    drawFriendsPie()
    #drawFriendsBarProvince()
if __name__=='__main__':
    main()
