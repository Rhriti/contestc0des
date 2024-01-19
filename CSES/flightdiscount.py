n,m=map(int,input().split())
from collections import defaultdict
g=defaultdict(list)
grev=defaultdict(list)
weight={}
weight_rev={}
q=[]
for _ in range(m):
    a,b,w=map(int,input().split())
    q.append((a,b))
    g[a].append(b)
    grev[b].append(a)
    weight[(a,b)]=w
    weight_rev[(b,a)]=w

import heapq as hq
cost=defaultdict(lambda:float('inf'))
cost[1]=0    #one jane k cost zero,bcoz hum whi per hai
st=[[0,1]]  #[cost,ndoe]
visit=set()
while st:
    out=hq.heappop(st)
    if out[1] not in visit:
        cost[out[1]]=out[0]
        visit.add(out[1])

    if out[1]==n:
        break
    for ch in g[out[1]]:
        if ch not in visit:
            hq.heappush(st,[out[0]+weight[(out[1],ch)] , ch ]    )

cost_rev=defaultdict(lambda:float('inf'))
cost_rev[n]=0
st=[[0,n]] #[cost,node]
visit=set()
while st:
    out=hq.heappop(st)
    if out[1] not in visit:
        visit.add(out[1])
        cost_rev[out[1]]=out[0]

    if out[1]==1:
        break
    for ch in grev[out[1]]:
        if ch not in visit:
            hq.heappush(st,[out[0]+weight_rev[(out[1],ch)] , ch ]    )
# print(cost)
# print(cost_rev)

minm=cost[n]
for ele in q:
    # print(f'cost form {ele[0]} to {ele[1]} is {cost[ele[0]]+cost_rev[ele[1]]+(weight[ele]//2)}')
    minm=min(minm,cost[ele[0]]+cost_rev[ele[1]]+(weight[ele]//2))
print(minm)








