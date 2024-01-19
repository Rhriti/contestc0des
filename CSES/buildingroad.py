n,m=map(int,input().split())
from collections import defaultdict
g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(node):
    v.add(node)
    for ch in g[node]:
        if ch not in v:
            dfs(ch)
v=set()
count=0
order=[]
for i in range(1,n+1):
    if i not in v:
        count+=1
        order.append(i)
        dfs(i)
print(count-1)
for i in range(len(order)-1):
    print(order[i],end=' ')
    print(order[i+1])