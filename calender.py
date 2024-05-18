start_day=int(input("enter the start_day : "))
num_of_days=int(input("enter the num_of_days : "))
print("sun mon tue wed thurs fri sat ")
print("------------------------------")
for i in range(start_day-1):
    print(end=" ")
    i=start_day-1
for j in range(1,num_of_days+1):
    if(i>6):
        print()
        i=1
    else:
        i=i+1
    print(str(j)+"  ",end=" ")