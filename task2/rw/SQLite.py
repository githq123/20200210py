import sqlite3
conn=sqlite3.connect('adress.db')
print('创建数据库成功！')
print('\t\t我的通讯录')
while True:
    print('1.新建',end='')
    print('2.查找',end='')
    print('3.添加',end='')
    print('4.修改',end='')
    print('5.删除',end='')
    print('6.排序',end='')
    print('7.退出',end='')
    choice=int(input('请输入你的选择（0-6）:'))
    if choice==0:
        print("非法输入")
        continue
    if choice==1:#新建
        sqlstr='''
        create table myadress(
            id int primary key not null,\
            name text,\
            adress text)'''
        conn.execute(sqlstr)
        print('数据库创建成功')
    if choice==2:#查找
        xz=input()
        cursor=conn.cursor()
        if xz=='*':
            mylist=cursor.execute('select * from myadress')
        else:
            mylist=cursor.execute('select id,name,telephone,\
                                  adress from myadress where id=? or name like ?or\
                                  telephone like ? or adress like ?,\
                                  (xz.strip(),（'%'+xz.strip()+'%' ),（'%'+xz.strip()+'%' ),（'%'+xz.strip()+'%' )))')
            for row in mylist:
                print('编号=',row[0],end=' ')
                print('姓名=',row[1], end=' ')
                print('电话=',row[2], end=' ')
                print('地址=',row[3], end=' ')
    if choice==3:#添加
        myid=input('请输入编号')
        name=input('请输入名字')
        telephone=input('请输入电话')
        adress=input('请输入地址：')
        cursor.execute("insert into myadress(id,name,telephone,adress)\
                     values ((?),(?),(?),(?)) ",\
                       (int(myid),name,telephone,adress))
        conn.commit()
        cursor.close()
        print("这里是新建")
    if choice==4:#修改
        pass
    if choice==5:#删除
        pass
    if choice==6:#排序
        pass
    if choice==7:#退出
        pass