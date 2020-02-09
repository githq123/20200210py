import time
import random
ll=[]
for i in range(9999):
  ll.append(random.randint(0,20000))
def bubble1(l):
    flag = True
    for i in range(len(l)-1, 0, -1):
        if flag:
            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
def insert(l):
  for i in range(1, len(l)):
     j = i - 1
     while j >= 0 and l[i] < l[j]:
       l[i] = l[j]
       j-=1
       l[j + 1] = l[i]
def selection(l):
    for i in range(0, len (l)):
        min = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
start1 = time.clock()
bubble1(ll)
end1 = time.clock()
a = end1 - start1
start2 = time.clock()
insert(ll)
end2 = time.clock()
b = end2 - start2
start3 = time.clock()
selection(ll)
end3 = time.clock()
c = end3 - start3
print("冒泡排序时间：{:.3f}".format(a))
print("插入排序时间：{:.3f}".format(b))
print("选择排序时间：{:.3f}".format(c))

