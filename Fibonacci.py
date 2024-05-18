m=0
n=1
x=int(input())
print("Fibonnacci numbers :")
print(m)
print(n)

for i in range(2,x):
    temp = m+n
    print(temp)
    m=n
    n=temp