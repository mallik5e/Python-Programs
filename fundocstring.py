def add(*args):
    '''function returns the sum of values passed to it'''
    sum=0
    for i in args:
        sum+=i
    return sum

print(add.__doc__)
print("sum = ",add(25,30,50,45))