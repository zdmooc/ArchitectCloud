
class A():
    __slots__ = ('a', 'b', 'c')

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

if __name__ == '__main__':
    o = A()
    print(o.a , o.b, o.c)
