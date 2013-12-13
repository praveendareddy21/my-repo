def rod(cos,n):
    if n==0 :
        return 0
    l=[]
    for i in range(0,n):
        l.append(cos[i+1]+rod(cos,n-i-1))
    return max(l)
cos=[0,2,4,5,6,5]
print rod(cos,5) 
############
def fun(str,count,init):
    print 'me'
    if count ==0 :
        return ['']
    if count > len(str) :
        return ['']
    if count ==len(str) :
        print str[init:]
        return [str[init:]]
        
    out =fun(str[init+1 :],count-1,0)
    res=[]
    for i in out :
        res.append(str[init]+i)
    res.extend(fun(str[init+1: ],count,0))
    return res
print fun('abcde',2,0)

    
