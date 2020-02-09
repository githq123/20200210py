def bubble(l):
#    flag = True
    for i in range(len(l)-1, 0, -1):
#        if flag:
#            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
#        else:
 #           break
    print (l)
li = input("请输入数字，用逗号隔开：").split(",")
bubble(li)
