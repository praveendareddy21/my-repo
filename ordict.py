from collections import OrderedDict

class DefaultOrderedDict(OrderedDict):
    def __missing__(self, key):
        self[key] = type(self)()
        return self[key]
d=DefaultOrderedDict()
d['a']['c']['d']=1234
d['as'][4][2]='sdf'
d[3][4][2]=322
print [(i, j, k, d[i][j][k]) for i in d for j in d[i] for k in d[i][j]]
it=d.__iter__()
print it.next()
print it.next()
print it.next()
#print it.next()
c={1:1,2:2,3:3}
for k ,v in c.items() :
    print( '{} -- {}'.format(k,v))
b='dsf sdfs'
print b.join(['122','2323'])
print b

#############
from collections import OrderedDict
dic=OrderedDict()
dic.update({12:'sdazs'})
dic['second']='valie'
dic['third']='dfsa'
d={}
d['second']='valie'
d['third']='dfsa'
d['sdf']='sdfas'
it=d.__iter__()
print it
while(1):
    try :
        print it.next()
    except StopIteration :
        print 'done'
        break
#dic.itervalues()
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
it=fib()
print fib()
print it.next()
print it.next()
print it.next()
