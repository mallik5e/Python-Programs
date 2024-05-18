d = int(input("enter the value : "))
b=0
i=0
while(d!=0):
    r = d%2
    b = b+r*(10**i)
    d1 = d/2
    d =int(d1)
    i=i+1
print(b)