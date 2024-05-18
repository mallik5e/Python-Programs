m=int(input("enter the value : "))
sum=0
num=m
n=str(m)
while(m>0):
    r=m%10
    sum=sum+int(r)**len(n)
    m=m//10
print(sum)
if(sum==num):
    print("amstrong")
else:
    print("not armstrong")
