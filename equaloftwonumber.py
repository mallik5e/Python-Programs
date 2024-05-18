def fun(a,b):
    if(a==b):
        return 0
    if(a>b):
        return 1
    if(a<b):
        return -1
x=5
y=4
f=fun(x,y)
if(f==0):
    print("a is equal")
if(f==1):
    print("a is greater")
if(f==-1):
    print("a is lesser")
