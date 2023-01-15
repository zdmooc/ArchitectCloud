class A():
    def f1(self):
        print(" A f1 ")

class B( A ):
    pass

class C():
    def f1(self):
        print(" C f1 ")

class D( B, C):
    pass


o = D()
o.f1()

print ( D.mro() )
