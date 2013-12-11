'''
 * Copyright (c) 2013 Vidcentum R&D Pvt Ltd. All Rights Reserved.
 *
 * This software is the confidential and proprietary information of 
 * Vidcentum R&D Pvt Ltd. ("Confidential Information"). You shall not  
 * disclose such Confidential Information and shall use it only in  
 * accordance with the terms of the license agreement you entered into
 * with Vidcentum.
 
Created on Sep 25, 2013

@author: kapil
'''
from collections import deque
str1=raw_input("en")
d=deque()
res=''
for i in str1 :
    print '_'
    if i in [str(x) for x in range(10)] :
        res=res+i
    if i=='*' or i=='/' :
        if len(d)==0 :
            d.appendleft(i)
        elif d[0] in ['*','/'] :
            res=res+d.popleft()
            d.appendleft(i)
        elif d[0] in ['+','-'] :
            d.appendleft(i)
    if i=='+' or i=='-' :
        if len(d)==0 :
            d.appendleft(i)
        elif d[0] in ['+','-'] :
            res=res+d.popleft()
            d.appendleft(i)
        elif d[0] in ['*','/'] :
            res=res+d.popleft()
            if len(d) != 0 and d[0] in ['+','-'] :
                res=res+d.popleft()
                d.appendleft(i)
            if len(d)==0 :
                d.appendleft(i)
if len(d)>0 :res=res+d.popleft()
if len(d)==1 :
    res=res+d.popleft()
print res
def fun(sr1):
    if sr1=='*' : return lambda x,y:x*y
    elif sr1=='/' : return lambda x,y:x/y
    elif sr1=='+' : return lambda x,y:x+y
    elif sr1=='-' : return lambda x,y:x-y
    
#print fun('*')(12,4)
def calcu(str1):
    d1=deque()
    co=len(str1)
    i=0
    while(True) :
        if i <co :
            d1.appendleft(str1[i])
            i+=1
       
        if(len(d1)==1 and i==co ):
            print d1[0]
            break
        
        if(len(d1)>2 ):
            if d1[0] in ['+','-','*','/'] :
                
                if(d1[1].isdigit() and d1[2].isdigit()):
                    print 'me'
                    v=fun(d1[0])(int(d1[1]),int(d1[2]))
                    d1.popleft()
                    d1.popleft()
                    d1.popleft()
                    d1.appendleft(str(v))
                    print d1
calcu('12+4+12*+')
                    
                    
                    
                
        
    
