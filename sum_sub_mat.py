def fun(a,i,j):#sub square matrix with all 1's 
    b=[]
    b.append(a[0])
    for k in range(1,i):
        b.append([a[k][0]])
    print b[1]
    for l in range(1,i) :
        for m in range(1,j):
            #print globals()
            val=1
            print b[l][m-1]
            val= min(b[l-1][m],b[l][m-1],b[l-1][m-1])+1
            b[l].append(val)
    print b
    
a=[[1,2,3,4],[3,4,5,6],[3,2,1,4]]
fun(a,3,4)
