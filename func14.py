def fun(name,*favsubjects):
    print("\n",name,"like to read ")
    for subject in favsubjects:
        print(subject,end=" ")
fun("goransh","maths","physics")
fun("richa","c","data structure","daa")
fun("krish")