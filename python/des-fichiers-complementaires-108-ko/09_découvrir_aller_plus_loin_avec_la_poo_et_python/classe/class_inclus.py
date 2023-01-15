
class Humain():
    class Cerveau():
        def do(self):
            return "Je réfléchis ..."
    class Estomac():
        def do(self):
            return "Je digère ..."
    class Jambe():
        def do(self):
            return "Elles marchent ..."
    class Main():
        def do(self):
            return "Elles bricolent ..."

    def __init__(self):
        self.organes = {
                'cerveau' : ( self.Cerveau(), ),
                'Estomac' : ( self.Estomac(), ),
                'Jambes' : (self.Jambe(), self.Jambe()),
                'Mains' : (self.Main(), self.Main())
                }

    def do(self):
        for k,v in self.organes.items():
            print( "%-15s" % k)
            for m in v:
                print( "%20s" % m.do() )

if __name__ in '__main__':
    H = Humain()
    H.do()
