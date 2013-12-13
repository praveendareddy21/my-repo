class nod(object):
    def __init__(self ,elem):
        self.elem=elem
        self.le=None
        self.ri=None
    def setle(self ,le):
        self.le=le
    def getle(self):
        return self.le
    def setri(self ,ri):
        self.ri=ri
    def getri(self):
        return self.ri
class dll(object):
    def __init__(self,elem):
        self.elem=elem
        self.le=None
        self.ri=None
    def setle(self ,le):
        self.le=le
    def getle(self):
        return self.le
    def setri(self ,ri):
        self.ri=ri
    def getri(self):
        return self.ri

s=nod(12)
b=nod(7)
c=nod(14)
s.setle(b)
s.setri(c)
h=nod(9)
b.setri(h)
l=nod(13)
m=nod(16)
c.setle(l)
c.setri(m)
#print s.getle().elem
print s.__dict__
def trav(obj ,d):
    if obj.le is not None :
        trav(obj.getle(),d)
    print obj.elem
    if obj.ri is not None :
        trav(obj.getri(),d)
    else :
        t=d
        while t.ri is not None:
            t=t.getri()
        t.ri=obj
        obj.ri=None
        obj.le=t
            
d=dll('root')
trav(s ,d)
t=d
while t.ri is not None:
    print t.elem
    t=t.getri()
print t.elem
while t.le is not None :
    print t.elem
    t=t.getle()
        
