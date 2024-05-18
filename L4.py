#lambda receives no arguments but simply returns an expression
def fun(f,n):
    print(f(n))
twice=lambda x: x*2
thrice=lambda x: x*3
fun(twice,4)
fun(thrice,3)