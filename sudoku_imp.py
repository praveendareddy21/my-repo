import sys
sys.stdin=open('C:/Python27/input.txt')
ls=[]
for i in xrange(9):
    li=raw_input("").split()
    li=[int(x) for x in li]
    ls.append(li)
def linechecker(ls):
    for i in range(9):
        count=0
        for j in range(9) :
            if ls[i][j]==0 and count ==0 :
                count=i
            if ls[i][j]==0 and count !=0 :
                count=-1
        if count >0 :
            ls[i][count]=[x for x  in range(9) if x not in ls[i]][0]
    for j in range(9):
        count=0
        for i in range(9) :
            if ls[i][j]==0 and count ==0 :
                count=i
            if ls[i][j]==0 and count !=0 :
                count=-1
        if count >0 :
            s=range(1,10)
            for k in range(9):
                if k not in s :ls[count][j]=k
def sud():
    pass
