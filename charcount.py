ch=input("enter the value : ")
num_count=0
up_count=0
lower_count=0
while(ch!="*"):
    if(ch>="a" and ch<="z"):
        lower_count=lower_count+1
    elif(ch>="A" and ch<="Z"):
        up_count=up_count+1
    else:
        num_count=num_count+1
print("num_count= ",num_count)
print("up_count=  ",up_count)
print("lower_count = ",lower_count)