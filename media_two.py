## calculate median from joining arrays (linear alg- place em in arr and find out inefficient  )
def helper(dif,l2,l4,i1 ,i2 ):
    while(dif != 1):
        if(l2[i1] <l4[i2]):
            i1=i1+1
            dif=dif-1
        elif(l2[i1] <l4[i2]) :
            i2=i2 + 1
            dif=dif-1
        else :
            i1=i1+1
            dif=dif-1
            
    if(l2[i1] <l4[i2]):
        print l2[i1]
    else :
        print l4[i2]
            
                        
                    
                    
    
st1=raw_input("")
st2=raw_input("")
l1=st1.split()
l2=[int(x) for x in l1]
l3=st2.split()
l4=[int(x) for x in l3]
l2.sort()
l4.sort()
length=len(l2)
mid1=mid2=length/2
while(True) :
    if l2[md1] < l4[md2] :
        count=count-md1+1
        if(count <5  and count  <=0 ) :
            print 'er'
            break
           
        if(count <5 ) :
            helper(count,l2,l4 ,md1,md2)
            break
            

        md1=md1+(md1) /2
        md2=md2-(md1) /2
        pass
    elif l2 [md1] > l4[md2] :
        count=count-md2+1
        if(count <5  and count  <=0 ) :
            print 'er'
            break
           
        if(count <5 ) :
            helper(count,l2,l4,md1,md2)
            break
     
        md2=md2 +(md2)/2
        md1=md1 -(md2)/2
        if count ==0 :
            print
        pass
    else :
        count=count-md1
        count=count-md2
        if count==0 :
            print l2[md1]
            break 
        
        
        
    
    
