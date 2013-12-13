from collections import Counter
l=[12,3,4,2,4,2,4,23,4,1,2]
c=Counter(iterable=l)
print c.most_common(2)
print list(c.elements())
c.clear()
