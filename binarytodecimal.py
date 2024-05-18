b=int(input("enter the value : "))
i=0
d=0
while(b!=0):
    r=b%10
    d=d+r*(2**i)
    b1=b/10
    b=int(b1)
    i=i+1
print(d)