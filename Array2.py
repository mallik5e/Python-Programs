from array import *

arr = array('i',[])
n=int(input('Enter the length of the array: '))

for i in range (n):
    x=int(input('Enter the values'))
    arr.append(x) 
    
print(arr)

n=int(input('Enter the searching Element'))
k=0
for i in arr:
    if i == n:
        print(k)
        break
    k+=1 #indexing
    
