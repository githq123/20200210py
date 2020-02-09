import math
a=eval(input("请输入边长a："))
b=eval(input("请输入边长b："))
c=eval(input("请输入边长c："))
if(a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
    w=a+b+c
    h=w/2
    s=math.sqrt(h * (h - a) * (h - b) * (h - c))
    print("可以构成三角形，周长：{:.1f},面积：{:.1f}".format(w,s))
else:
    print("无法构成三角形！")