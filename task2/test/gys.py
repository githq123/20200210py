def gys(x, y):
    if x > y:
        min = y
    else:
        min = x
    for i in range(1, min + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("第一个数字: "))
num2 = int(input("第二个数字: "))
print(num1, "和", num2, "的最1大公约数为", gys(num1, num2))
