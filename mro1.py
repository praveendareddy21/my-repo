class Base1(object):  
    def amethod(self): print "Base1"  
class Base5(object):
    pass
class Base4(Base1 ,Base5):
    pass
class Base7(object):
    pass
class Base6(Base7):
    pass
class Base2(Base1 ,Base6):  
    pass

class Base3(Base1):  
    def amethod(self): print "Base3"

class Derived(Base2,Base3,Base4,Base1):  
    pass

instance = Derived()  
instance.amethod()  
print Derived.__mro__ 
