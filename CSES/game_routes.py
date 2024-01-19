n,m=map(int,input().split())
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)

memo={}
def dfs(node):
    if node==n:
        return 1
    if node in memo:
        return memo[node]
    ways=0
    for ch in g[node]:
        ways+=dfs(ch)
    memo[node]=ways
    return ways
print(dfs(1)%(10**9+7))
