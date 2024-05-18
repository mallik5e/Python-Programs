def small(a,b):
    if(a<b):
        return a
    else: 
        return b 
sum = lambda x,y : x+y
diff = lambda x,y : x-y 
print("smaller number of two numbers = ",small(sum(-3,-2),diff(-1,6)))