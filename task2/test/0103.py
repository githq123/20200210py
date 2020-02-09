# world=' world'
# print('hello'+world)
# from math import sqrt
# print (sqrt(3)**2)
# s="Happy New Year"
# print(s[3:8])
#strchr(str1,str2)
# < 0 为未找到
# from filecmp import cmp
#
# str1 = 'strchr'
# str2 = 'strch'
# print (cmp(str1,str2))
# str = '0123456789'
# print (str[0:3])    #截取第一位到第三位的字符
# print (str[:])      #截取字符串的全部字符
# print (str[6:])     #截取第七个字符到结尾
# print (str[:-3])    #截取从头开始到倒数第三个字符之前
# print (str[2])     #截取第三个字符
# print (str[-1])     #截取倒数第一个字符
# print (str[::-1])   #创造一个与原字符串顺序相反的字符串
# print (str[-3:-1])  #截取倒数第三位与倒数第一位之前的字符
# print (str[-3:])    #截取倒数第三位到结尾
# print (str[:-5:-3]) #逆向截取，倒数第一位与倒数第五位之间的字符，步长为3
# import math
# print( math.sin(math.pi/2))
# a=open("test_text.txt","r").read()
# print(a)
# def foo(s):
#   if s == "":
#     return s
#   else:
#     return foo(s[1:]) + s[0]
# print (foo("Happy New Year"))
# def foo(list,num):
#   if num == 1:
#     list.append(0)
#   elif num == 2:
#     foo(list,1)
#     list.append(1)
#   elif num > 2:
#     foo(list,num-1)
#     list.append(list[-1]+list[-2])
# mylist = []
# foo(mylist,10)
# print (mylist)
# k=1000
# i=0
# while k>1:
#     i+=1
#     print (k)
#     print(i)
#     k=int(k/2)
# print(1/4+2.75)
# s = "hi"
# print ("hi",2*s)
# print(1.2-1.0)
# a = 1
# b = 2 * a / 4
# a = "one"
# print (a,b)
# print('%d%%%d'%(1%2,3%4))
# def lazy_sum(*args):
#     def sum():
#         x=0
#         for n in args:
#             x=x+n
#         return x
#     return sum
# #lazy_sum(1,2,3,4,5,6,7,8,9) #这时候lazy_sum 并没有执行，而是返回一个指向求和的函数的函数名sum 的内存地址。
# f=lazy_sum(1,2,3,4,5,6,7,8,9)
# print(type(f))
# print(f())  # 调用f()函数，才真正调用了 sum 函数进行求和，
# a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
# a.sort()
# last=a[-1]
# for i in range(len(a)-2,-1,-1):
#   if last==a[i]:
#     del a[i]
#   else:last=a[i]
# print(a)
# import math
# n = 0
# for  m  in  range(101, 201, 2):
#   k = int(math.sqrt(m))
#   for i in range(2, k+1):
#     if m % i == 0:
#       break
#   if i ==k:
#     if n % 10 == 0:
#       print ("\n")
#     print ("%d " % m)
#     n += 1
#print(5//2)
# tup1=(1,2,3,4,5);list2=[6,7,8,9,10];dict3 = {'name':'xiaoming','sex':'man','age':'20'};str4='Hello World'
# print("A小题：")
# print ("元组转为字符串:",str(tup1))
# print ("元组转为列表:",list(tup1))
# print("元组不可以直接转为字典，先转换成列表：",dict(zip(list(tup1),list(tup1))))
# print("B小题：")
# print ("列表转为字符串:",str(list2))
# print ("列表转为元组:",tuple(list2))
# print("列表转为字典",dict(zip(list2,list2)))
# print("C小题：")
# print ("字典转为字符串:",(dict3))
# print ("字典转为元组:",tuple(dict3))
# print("字典转为列表：",list(dict3))
# print("D小题：")
# print ("字符串转为元组:",tuple(str4))
# print("字符串转为列表：",list(str4))
# print("字符串不可以直接转换为字典，先转成列表：",dict(zip(list(str4),list(str4))))
# a=open('a.txt','r').read()
# b=open('b.txt','w')
# for s in a:
#     b.write(s)
# b.close()
# c=open('b.txt','r').read()
# print(c)
# a=[1]
# b=a
# b.append(3)
import math
print(math.log(2,4))