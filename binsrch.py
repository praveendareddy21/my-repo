def binsrch1(ar,el,lt ,rt):
    half=(lt+rt)/2
    if rt-lt==1 :# critical Boudary case 
        if ar[lt]==el : return lt
        if ar[rt]==el : return rt
        
    if ar[half]==el :
        return half
    if ar[half]> el :
        rt=half
    else :
        lt=half
    return binsrch1(ar,el,lt,rt)
def binsrch2(ar,el,lt ,rt):
    while(True):
        half=(lt+rt)/2
        if rt-lt==1 :
            if ar[lt]==el : return lt
            if ar[rt]==el : return rt
            
        if ar[half]==el :
            return half
        if ar[half]> el :
            rt=half
        else :
            lt=half   
ar=[-11,-2,4,7,11,12,20,23,54,77,112,145]
print ar[binsrch2(ar,7,0,11)]    
         
    
