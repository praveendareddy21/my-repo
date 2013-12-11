def genint(x):
    for i in xrange(x) :
        yield i
g=genint(3)
print g 
#print g.next()
a,b,c=genint(3)
print a
print b
print c
        
