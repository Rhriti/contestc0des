n,m=map(int,input().split())
from collections import defaultdict,deque
g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
st=deque()
st.append(1)
par={1:1}
while st:
    out=st.popleft()
    if out==n:
        break
    for ch in g[out]:
        if ch not in par:
            par[ch]=out
            st.append(ch)
if n in par:
    order=deque()
    itr=n
    while par[itr]!=itr:
        order.appendleft(itr)
        itr=par[itr]
    order.appendleft(itr)
    print(len(order))
    for ele in order:
        print(ele,end=' ')
    print()
else:
    print('IMPOSSIBLE')
