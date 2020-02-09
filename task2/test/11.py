for N in [1,2,3,4,5,6,7,8,9,10]:
 dayup = 1.0
 for i in range(364):
    if (i+1) % 7 not in [5,6,0]:
        dayup = dayup * (1 + N*0.001)
    else:
        dayup = dayup
 print("_{:.2f}".format(dayup))