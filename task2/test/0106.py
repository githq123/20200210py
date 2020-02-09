#1：
# N=eval(input("请输入范围："))
# n=0
# for i in range(N):
#     if (i+1)%2==0:
#         n=n-(1/(i+1))
#     else:n=n+(1/(i+1))
# print(n)

#2:
# Tem=input("请输入带符号的温度值：")
# if Tem[-1]=='D':
#     R=float(Tem[0:-1])/6.9
#     print("{:.2f}R".format(R))
# elif Tem[-1]=='R':
#     D=float(Tem[0:-1])*6.9
#     print("{:.2f}D".format(D))
# else:
#    print("请输入正确格式！")

#3:
# Num=input("请输入数字：")
# a=False
# for i in range(len(Num)//2):
#     if Num[i]==Num[-(i+1)]:
#         a=True
#     else:
#         a=False
#         break
# print(a)

#4:
# import math
# a=eval(input("请输入边长a:"))
# b=eval(input("请输入边长b:"))
# c=eval(input("请输入边长c:"))
# if(a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a):
#     w=a+b+c
#     h=w/2
#     s=math.sqrt(h*(h-a)*(h-b)*(h-c))
#     print("可以构成三角形，周长为：{:.1f},面积为：{:.1f}。".format(w,s))
# else:print("不能构成三角形！")

#5：
# year=eval(input("请输入年份："))
# if (year%100!=0 and year%4==0)or year%400==0:
#     print("是闰年")
# else:print("不是闰年")
# #6:
# import math
# num=eval(input("请输入数字（大于1）："))
# a=False
# if num>1:
#     for i in range(2,int(math.sqrt(num))+1):
#         if num%i==0:
#             a=True
#             break
#         else:a=False
#     print(a)
# else:print("请输入有意义的数字！")

