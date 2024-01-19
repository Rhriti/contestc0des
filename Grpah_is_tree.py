from os import *
from sys import *
from collections import defaultdict
from math import *

def checkgraph(edges, n, m):
    n=0
    g=defaultdict(list)
    check={} #
    for u,v in edges:
        check[u]=-1
        check[v]=-1
        g[u].append(v)
        g[v].append(u)
    cycle=[False]
    def dfs(node):
        check[node]=0#visiting
        for ch in g[node]:
            if check[ch]==-1:
                dfs(ch)
            else:
                if check[ch]==0:
                    cycle[0]=True
                    return
        check[node]=1

    dfs(0)
    print(cycle)
    print(g)
    print(check)
    if cycle[0]==True:
        return False
    for val in check.values():
        if val==-1:
            return False
    return True
    
print(checkgraph([[0,1],[0,2],[0,3],[1,4]],5,4))





        

