Num=str(eval(input("请输入数字：")))
a=False
for i in range(int(len(Num)/2)):
  if Num[i]==Num[-(i+1)]:
    i+=1
    a=True
  else:
     a=False
     break;
print(a)