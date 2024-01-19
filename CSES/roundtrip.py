n,m=map(int,input().split())
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

par={}
ans=[]
def dfs(node):
    for ch in g[node]:
        if ch in par:
            if ch !=par[node]:
                ans.append(ch)
                ans.append(node)
                return
        else:
            par[ch]=node
            dfs(ch)
        if len(ans)==2:
            return 

for ele in range(1,n+1):
    if ele not in par:
        par[ele]=ele
        dfs(ele)
        if len(ans)!=0:
            break
if len(ans)==2:
    itr=ans[1]
    final=[ans[0]]
    while itr!=ans[0]:
        final.append(itr)
        itr=par[itr]
    final.append(ans[0])
    print(len(final))
    for ele  in final:
        print(ele,end=' ')
    print()

else:
    print('IMPOSSIBLE')
