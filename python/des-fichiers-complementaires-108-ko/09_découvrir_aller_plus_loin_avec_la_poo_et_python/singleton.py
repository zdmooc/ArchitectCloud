class Singleton(object):
   class __Singleton:
      def __init__(self):
         self.val = None
      def __str__(self):
          return 'self : ' + self.val

   instance = None

   def __new__(class__):            # _new_ est toujours une méthode de classe
      if not Singleton.instance:
          Singleton.instance = Singleton.__Singleton()
      return Singleton.instance

   def __getattr__(self, attr):
      return getattr(self.instance, attr)

   def __setattr__(self, attr, val):
      return setattr(self.instance, attr, val)


if __name__ == '__main__':
    Une = Singleton()
    print("Instance Une    : %s " % id(Une))
    Une.val = 'Une'
    print(" Une.val   = ", Une.val )
    Deux = Singleton()
    print("Instance Deux   : %s " % id(Deux))
    print(" Deux.val  = ", Deux.val )
    Deux.val = 'Deux'
    print(" Deux.val  = ", Deux.val )
    Trois = Singleton()
    print("Instance Trois  : %s " % id(Trois))
    print(" Trois.val = ", Trois.val )
    Trois.val = 'Trois'
    print(" Trois.val = ", Trois.val )
    print("===============================")
    print(" Une.val   = ", Une.val )
    print(" Deux.val  = ", Deux.val )
    print(" Trois.val = ", Trois.val )
