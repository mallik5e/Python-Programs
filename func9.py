def outer_func():
    var=20
    def inner_func():
        var=10
        print("inner_func =",var)
    inner_func()
    print("outer_func =",var)
outer_func()