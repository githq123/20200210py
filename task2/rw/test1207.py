import  json
import sqlite3
import xlsxwriter
import xlrd
con =sqlite3.connect('readAndwrite.db')
def main():
    ls=readCSV()
    #writeCSV(ls)
    #readJson()
    #writeJson(ls)
    #readText()
    #writeText(ls)
    #readExecl()
    #writeExcel(ls)
    writeSqlLite(ls)
    readSqlLite()
    con.close()
def readCSV():
    ls=[]
    with open('price2016.csv','r',encoding='gbk') as in_csv:
        for line in in_csv:
             line =line.replace('\n','')
             ls.append(line.split(','))
    return ls
def writeCSV(ls):
    out_csv=open('out_csv.csv','w')
    for i in range(len(ls)):
        out_csv.write(','.join(ls[i])+'\n')
        print('写完成！')
def readJson():
    in_json=open('price2016.json','r')
    ls=json.load(in_json)
    data=list(ls[0].keys())
    for item in ls:
        data.append(list(item.values()))
    in_json.close()
    for item in data:
        print(''.join(item)+'\n')
def writeJson(ls):
    out_json=open('out_price2016.json','w')
    for i in range(1,len(ls)) :
        ls[i]=dict(zip(ls[0],ls[i]))
    json.dump(ls[i:],out_json,sort_keys=True,indent=4)
    out_json.close()
    print('写Json完成')
def readText():
    in_text=open('test_text.txt','r')
    for line in in_text.readlines():
        print(line)
    print('读Text完成')
def writeText(ls):
    out_text=open('test_text.txt','w')
    for i in range (1,len(ls)):
        out_text.write(''.join(ls[i])+'\n')
    out_text.close()
    print('写text完成')
def readExecl():
    in_workbook=xlrd.open_workbook('test_excel.xlsx')
    worksheet=in_workbook.sheet_by_index(0)
    ls=[]
    for i in range(worksheet.nrows):
        ls.append(worksheet.row_values(i))
    print(ls)
def writeExcel(ls):
    out_workbook=xlsxwriter.workbook('out_excel.xlsx')
    worksheet=out_workbook.add_worksheet('sheet1')
    for i in range(len(ls)-1):
        worksheet.write_row('A'+str(i+1),ls[i])
    out_workbook.close()
def readSqlLite():
    cur=con.cursor()
    result=cur.execute('select * from cityprice')
    for row in result:
        print(row[0], end=' ')
        print(row[1], end=' ')
        print(row[2], end=' ')
        print(row[3], end=' ')
def writeSqlLite(ls):
    cur=con.cursor()
    droptable_sql='drop table if exists cityprice'
    cur.execute(droptable_sql)
    con.execute('''create table cityprice(
                 '城市' text primary key not null,
                 '环比' text not null,
                 '同比' text not null,
                 '定基' text not null)''')
    print('创建成功')
    for i in range(len(ls)-1):
        sqlstr= 'insert into cityprice(城市,环比,同比,定基)values ((?),(?),(?),(?))'
        cur.execute(sqlstr,(ls[i+1][0],ls[i+1][1],ls[i+1][2],ls[i+1][3]))
    con.commit()
    cur.close()
    print('插入数据完成')

if __name__=='__main__':
    main()