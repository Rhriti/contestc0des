n=int(input())
nodes=set()
for _ in range(n):nodes.add(int(input()))
e=int(input())
from collections import defaultdict
import heapq as hq
g=defaultdict(list)
for _ in range(e):
    u,v,w=map(int,input().split())
    g[u].append([v,w])
    g[v].append([u,w])
start=int(input())
end=int(input())
st=[[0,start]]
v=set()

# print(g)

while st:
    out=hq.heappop(st)
    v.add(out[1])
    if out[1]==end:print(out[0]);break 
    for ele in g[out[1]]:
        if ele[0] not in v:
            hq.heappush(st,[out[0]+ele[1],ele[0]])
    








