from collections import defaultdict
from random import getrandbits
# Anti hack: https://codeforces.com/blog/entry/101817
class Wrapper(int):
    RANDOM = getrandbits(32)
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ Wrapper.RANDOM
 
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    
    carryx={}
    carryy={}
    carryx[Wrapper(arr[0]%x)]={0}
    carryy[Wrapper(arr[0]%y)]={0}



    final=0

    for i in  range(1,n):
        chie_x=x-(arr[i]%x)
        if chie_x==x:chie_x=0
        chie_x=Wrapper(chie_x)
        chie_y=arr[i]%y
        chie_y=Wrapper(chie_y)
     
        if chie_x in carryx and chie_y in carryy:
            news=carryx[chie_x].intersection(carryy[chie_y])
            final+=len(news)
        
        if chie_x in carryx:
            carryx[chie_x].add(i)
        else:
            carryx[chie_x]={i}
       
        if chie_y in carryy:
            carryy[chie_y].add(i)
        else:
            carryy[chie_y]={i}

    print('ans',final)

        
