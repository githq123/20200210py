N=eval(input("请输入总范围："))
sum=0
for i in range(N):
    if((i+1)%2==0):
        sum=sum-(1/(i+1))
        i+=1
    else:
        sum=sum+(1/(i+1))
        i+=1
print(sum)

