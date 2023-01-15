class A(object):
    def __init__(self):
        self. at1 = 1

    def __getattribute__(self,name):
        if name=='test':
            return 0
        else:
            return self.__dict__[name]

o = A()
print(o.at1)

