def fun(n1):
    if(n1%2==0):
        return 1
    else:
        return -1


n1=int(input("enter the value : "))
flag=fun(n1)
if(flag==1):
    print("even number")
if(flag==-1):
    print("odd number")
