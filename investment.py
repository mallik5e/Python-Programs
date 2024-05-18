invalue=int(input("enter the value : "))
roi=int(input("enter the value : "))
yrs=int(input("enter the yrs : "))
futurevalue=invalue
for i in range(1,yrs+1):
   futurevalue=futurevalue*(1+roi/100)
   print(i,"\t\t",int(futurevalue))