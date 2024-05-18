def outer_func():
    outer_var=10
    def inner_func():
        inner_var=20
        print("outer_val =",outer_var)
        print("inner_val =",inner_var)
    inner_func()
    print("outer variable =",outer_var)
    print("inner variable =",inner_var)
outer_func()
          