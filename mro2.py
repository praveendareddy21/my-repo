class F(object):
    def echo(self) :
        print ('F')
class G(object):
    def echo(self) :
        print ('G')
      
class E(G):
    def echo(self) :
        print ('E')

class H(object) :
    pass
class A (object):
    pass
class B(A,E,G) :
    pass
    #def echo(self) :
        #print "B"
class C(E) :
    pass
class D(B,C,H) :
    pass
d=D()
d.echo()
print (D.__mro__)
    
