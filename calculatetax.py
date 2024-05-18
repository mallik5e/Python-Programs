min1=150001
max1=300000
rate1=0.1
min2=300001
max2=500000
rate2=0.2
max=500001
rate3=0.3
income=int(input("enter the income : "))
tax_income=income-150000
if(tax_income>=0 and tax_income<min1):
    print("no tax")
elif(tax_income>=min1 and tax_income<=max1):
    tax=(tax_income-min1)*rate1
elif(tax_income>=min2 and  tax_income<=max2):
    tax=(tax_income-min2)*rate2
else:
    tax=(tax_income-max)*rate3
print("tax = ",int(tax))