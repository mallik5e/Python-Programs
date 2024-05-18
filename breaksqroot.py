import math
total_prime=0
total_composite=0
while(1):
    n=int(input("enter the value : "))
    if(n==99):
        break
    elif(n<0):
        print("negative square number cannot be calculated")
        continue
    else:
        print("square root of ",n,"=",math.sqrt(n))