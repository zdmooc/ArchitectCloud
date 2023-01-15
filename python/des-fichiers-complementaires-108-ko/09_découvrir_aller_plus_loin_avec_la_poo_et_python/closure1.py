
def func1():
    def s_func1():
        print(" S_func1 ")
    return s_func1

f = func1()

f()
f()

