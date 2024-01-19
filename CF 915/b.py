from collections import defaultdict
import copy 
import math
for _ in range(int(input())):
    n=int(input())
    if n==1 :
        print(0)
    else:

        g=defaultdict(list)
        for _ in range(n-1):
            u,v=map(int,input().split())
            g[u].append(v);g[v].append(u)
        
        v=set()
        leafs=0
        for ch in g.values():
            if len(ch)==1:leafs+=1
       
        # print(leafs)
        print(1+math.ceil((leafs-2)/2))
        # print('ans')
        
    
