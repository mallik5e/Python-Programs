n1=int(input("enter the value : "))
n2=int(input("enter the value : "))
if(n1>n2):
    dividend=n1
    divisor=n2
else:
    dividend=n2
    divisor=n1
while(divisor!=0):
    r=dividend%divisor
    dividend=divisor
    divisor=r
print(dividend)