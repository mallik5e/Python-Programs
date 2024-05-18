n1=10
print("Global variable = ",n1)
def fun(n2):
    print("local variable n2 = ",n2)
    n3=30
    print("local variable n3 = ",n3)
fun(20)
print("Global variable n1 = ",n1)
print("local variable n2 = ",n2)
print("local variable n3 = ",n3)