num=int(input("enter the value : "))
if(num==0):
    fact=1

fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)