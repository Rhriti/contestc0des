n,m=map(int,input().split())
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

assign={}
f=False
def dfs(node,c):
    global f
    assign[node]=c%2
    for ch in g[node]:
        if ch in assign:
            if assign[node]+assign[ch]!=1:
                f=True
                break
        else:
            dfs(ch,c+1)
    if f:
        return

for ele in range(1,n+1):
    if ele not in assign:
        dfs(ele,0)
        if f:
            break

if f:
    print('IMPOSSIBLE')
else:
    for ele in range(1,n+1):
        print(assign[ele]+1,end =' ')
    print()
    
    

