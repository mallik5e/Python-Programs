array = [3,1,2,4,6,5]
arr=len(array)
for i in range(0,arr):
    for j in range(i+1,arr):
        if(array[i]>array[j]):
          temp=array[i]
          array[i]=array[j]
          array[j]=temp 
print(array)