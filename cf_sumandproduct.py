import math
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    g=defaultdict(int)
    for ele in arr:
        g[ele]+=1
    q=int(input())
    
    for _ in range(q):
        s,p=map(int,input().split())
        if s*s-4*p>=0:
            t1=(s+math.sqrt(s*s-4*p))/2
            t2=(s-math.sqrt(s*s-4*p))/2
            if t1!=t2 :
                print(g[t1]*g[t2])
            else:
                print((g[t1]*(g[t1]-1))//2)
        else:
            print(0)

        


