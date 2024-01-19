import sys
sys.setrecursionlimit(10**7)
n=int(input())
from collections import defaultdict
g=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
tree=defaultdict(list)
par={}
def dfs(node):
    tree[node]
    for ch in g[node]:
        if ch not in tree:
            tree[node].append(ch)
            par[ch]=node
            dfs(ch)
dfs(1)
par[1]=1
height={}
def dfs(node):
    #base
    if node in height:
        return height[node]
    height[node]=0
    for ch in g[node]:
        if ch not in height:
            height[node]=max(height[node],1+dfs(ch))
    return height[node]
dfs(1)
uphei={1:0}
def dfsup(node):
    if node in uphei:
        return uphei[node]

    uphei[node]=dfsup(par[node])+1
    for ch in tree[par[node]]:
        if ch!=node:
            uphei[node]=max(uphei[node],height[ch]+2)
    return uphei[node]
for ele in range(1,n+1):
    if ele not in uphei:
        dfsup(ele)
for ele in range(1,n+1):
    print(max(uphei[ele],height[ele]),end=' ')
print()


















