def gcd(x,y):
    rem=x%y
    if(rem==0):
        return y
    else:
        return gcd(y,rem)


m=int(input("enter the value : "))
n=int(input("enter the value : "))
print("GCD =",gcd(m,n))