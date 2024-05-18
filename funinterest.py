def fun(p,y):
    if(senior=='y'):
         return (p*y*12)/100
    if(senior=='n'):
        return (p*y*10)/100


price=int(input("enter the principle : "))
yrs=int(input("enter the years : "))
senior=input("offered y/n :")
interest=fun(price,yrs)
print("total_amount of interest : ",interest)
