# -*- coding: utf-8 -*-
import sqlite3
import xlrd
import sys
class AddressBook:
  con =sqlite3.connect('rw1Excel.db')
  cur = con.cursor()
  def init(self):
    con = self.con
    cur = self.cur
    in_workbook = xlrd.open_workbook('Address.xlsx')
    worksheet = in_workbook.sheet_by_index(0)
    ls = []
    try:
        sqlstr = '''create table if not exists addr(id int primary key not null,name text not null,telephone int not null,address text);'''
        con.execute(sqlstr)
    except:
        print("创建表格失败")
        sys.exit(1)
        conn.execute(sqlstr)
    for i in range(worksheet.nrows):
        ls.append(worksheet.row_values(i))
        if i > 0:
            myid = ls[i][0]
            name = ls[i][1]
            telephone = ls[i][2]
            address = ls[i][3]
            cur.execute("insert into addr(id,name,telephone,address) values ((?),(?),(?),(?))",
                        (int(myid), name,int(telephone), address))
            con.commit()
            print("初始化成功！")
  def selectInfo(self,cz):
    con = self.con
    cur = self.cur
    if cz == "*":
        mylist = cur.execute('select * from addr')
    else:
        mylist = cur.execute('select * from addr where id=? or name like ? or telephone like ? or address like ?',
                              (cz.strip(),
                              ('%' + cz.strip() + '%'),
                              ('%' + cz.strip() + '%'),
                              ('%' + cz.strip() + '%'))
                             )
    for row in mylist:
        print("编号=", row[0], end='')
        print("姓名=", row[1], end='')
        print("电话=", row[2], end='')
        print("地址=", row[3], end='\n')
  def insertInfo(self,myid,name,telephone,address):
    con = self.con
    cur = self.cur
    cur.execute("insert into addr(id,name,telephone,address) values ((?),(?),(?),(?))",(int(myid), name, telephone, address))
    con.commit()
    print("添加成功！")
  def deleteInfo(self,myid):
    con = self.con
    cur = self.cur
    cur.execute('delete  from addr where id=(?)', (myid.strip()))
    con.commit()
    print("删除记录成功！\n")
  def updateInfo(self,myid,upNum,upInfo):
    con = self.con
    cur = self.cur
    mylist = cur.execute('select id,name,telephone,address'
                         ' from addr where id=(?)',
                         (myid.strip()))
    for row in mylist:
        print("1.编号=", row[0], end=' ')
        print("2.名字=", row[1], end=' ')
        print("3.号码=", row[2], end=' ')
        print("4.地址=", row[3], end='\n')
    while True:
        if upNum == '0':
            break
        elif upNum == '1':
            cur.execute('update addr set id=? where id=?', (upInfo.strip(), myid.strip()))
        elif upNum == '2':
            cur.execute('update addr set name=? where id=?', (upInfo.strip(), myid.strip()))
        elif upNum == '3':
            cur.execute('update addr set telephone=? where id=?', (upInfo.strip(), myid.strip()))
        elif upNum == '4':
            cur.execute('update addr set address=? where id=?', (upInfo.strip(), myid.strip()))
        con.commit()
    print("修改成功！")

ad=AddressBook()
#ad.init()
while True:
    print("============================")
    print('1.查找', end=' ')
    print('2.添加', end=' ')
    print('3.修改', end=' ')
    print('4.删除', end=' ')
    print('0.退出', end='\n')
    print("============================")
    choice = int(input("请输入你的选择（0-6）："))
    if choice == 0:
        break
    if choice < 0 or choice > 6:
        print("非法输入，请重输入!")
        continue
    if choice == 1:
        cz = input("请输入查找关键字，*代表全部")
        ad.selectInfo(cz)
    if choice == 2:
        myid = input("请输入编号：")
        name = input("请输入名字：")
        telephone = input("请输入电话：")
        address = input("请输入地址：")
        ad.insertInfo(myid,name,telephone,address)
    if choice == 3:
        myid = input("请输入要修改的编号：")
        upNum = input("请输入要修改项的编号(1-4)：")
        upInfo = input("请输入要修改的值：")
        ad.updateInfo(myid,upNum,upInfo)
    if choice == 4:
        myid = input("请输入要删除的编号：")
        ad.deleteInfo(myid)