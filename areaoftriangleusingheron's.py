a=float(input("enter the value: "))
b=float(input("enter the value: "))
c=float(input("enter the value: "))
print(a,b,c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)