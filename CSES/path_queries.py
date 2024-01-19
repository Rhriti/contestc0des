import sys
sys.setrecursionlimit(10**9)
n,q=map(int,input().split())
val=[0]*(n+1)
vals=list(map(int,input().split()))
for i in range(len(vals)):
    val[i+1]=vals[i]
from collections import defaultdict
g=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
# print(g)
for _ in range(q):
    s=list(map(int,input().split()))
    if len(s)==3:
        val[s[1]]=s[2]
    else:
        ans=0
        def dfs(node,sums):
            global ans
            sums+=val[node]
            v.add(node)
            #base
            if node==s[1]:
                ans=sums
                return 
            for ch in g[node]:
                if ch not in v:
                    dfs(ch,sums)
            sums-=val[node]
    
        v=set()
        dfs(1,0)
        print(ans)
