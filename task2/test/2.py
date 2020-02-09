Mons=input("请输入带有符号的金额数：")
if Mons[-1]=='D':
    R=6.9*eval(Mons[0:-1])
    print("{:.1f}R".format(R))
elif Mons[-1]=='R':
    D=eval(Mons[0:-1])/6.9
    print("{0:.0f}D".format(D))


