row,col=map(int,input().split())
import sys
sys.setrecursionlimit(10**9)
from collections import deque
start=end=None

g=[]
for r in range(row):
    s=input()
    t=[]
    for c in range(col):
        if s[c]=='A':
            start=[r,c]
        if s[c]=='B':
            end=[r,c]
        t.append(s[c])
    g.append(t)
        
st=[start]
v={(start[0],start[1])}
par={(start[0],start[1]):(start[0],start[1])}
f=False
while st:
    t=[]
    while st:
        out=st.pop()
        r=out[0]
        c=out[1]
        if (r,c)==(end[0],end[1]):
            f=True
            break
        if (r+1)<len(g) and (r+1,c) not in v and (g[r+1][c]=='.' or g[r+1][c]=='B'):
            v.add((r+1,c))
            t.append([r+1,c])
            par[(r+1,c)]=(r,c)
        if 0<=(r-1) and (r-1,c) not in v and (g[r-1][c]=='.' or g[r-1][c]=='B'):
            v.add((r-1,c))
            t.append([r-1,c])
            par[(r-1,c)]=(r,c)
        if (c+1)<len(g[0]) and (r,c+1) not in v and (g[r][c+1]=='.' or g[r][c+1]=='B'):
            v.add((r,c+1))
            t.append([r,c+1])
            par[(r,c+1)]=(r,c)
        if 0<=(c-1) and (r,c-1) not in v and (g[r][c-1]=='.' or g[r][c-1]=='B'):
            v.add((r,c-1))
            t.append([r,c-1])
            par[(r,c-1)]=(r,c)
    st=t
    if f:
        break

if f is False:
    print('NO')
else:
    order=deque()
    itr=(end[0],end[1])
    while par[itr]!=itr:
        if par[itr][0]>itr[0]:
            order.appendleft('U')
        elif par[itr][0]<itr[0]:
            order.appendleft('D')
        elif par[itr][1]>itr[1]:
            order.appendleft('L')
        else:
            order.appendleft('R')
        itr=par[itr]
    print("YES")
    print(len(order))
    for ele in order :
        print(ele,end='')
    print()


