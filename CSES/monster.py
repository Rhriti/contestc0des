#its multisource bfs
row,col=map(int,input().split())
import sys
sys.setrecursionlimit(10**9)
m=[]
a=[]
g=[[None for _ in range(col)] for _ in range(row)]
par={}
v=set()
for r in range(row):
    s=input()
    for c in range(len(s)):
        g[r][c]=s[c]
        if s[c]=='M':
            m.append([r,c])
            v.add((r,c))
        if s[c]=='A':
            par[(r,c)]=(r,c)
            a.append([r,c])
if a[0][0]==0 or a[0][0]==len(g)-1 or a[0][1]==0 or a[0][1]==len(g[0])-1:
    print('YES')
    print(0)
else:

    st=[]
    for ele in m:
        for x,y in [[ele[0]+1,ele[1]],[ele[0]-1,ele[1]],[ele[0],ele[1]+1],[ele[0],ele[1]-1]]:
            if 0<=x<len(g) and 0<=y<len(g[0]) and (x,y) not in v and g[x][y]=='.':
                st.append([x,y])
                v.add((x,y))
    m=st
    av={(a[0][0],a[0][1])}
    f=False
    while a:
        temp=[]
        while a:
            out=a.pop()
            r=out[0]
            c=out[1]
            for x,y in[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                if 0<=x<len(g) and 0<=y<len(g[0]) and (x,y) not in v and (x,y) not in av and g[x][y]=='.':
                    if x==0 or x==len(g)-1 or y==0 or y==len(g[0])-1:
                        par[(x,y)]=(r,c)
                        f=True
                        break
                    par[(x,y)]=(r,c)
                    av.add((x,y))
                    temp.append((x,y))
        a=temp
        #base
        if f:
            break
        t=[]
        while m:
            out=m.pop()
            r=out[0]
            c=out[1]
            for x,y in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                if 0<=x<len(g) and 0<=y<len(g[0]) and (x,y) not in v and g[x][y]=='.':
                    v.add((x,y))
                    t.append([x,y])
        m=t
    if f:
        itr=(x,y)
        order=[]
        while par[itr]!=itr:
            if par[itr][0]>itr[0]:
                order.append('U')
            elif par[itr][0]<itr[0]:
                order.append('D')
            elif par[itr][1]>itr[1]:
                order.append('L')
            else:
                order.append('R')
            itr=par[itr]
        order.reverse()
        print('YES')
        print(len(order))
        for ele in order:
            print(ele,end='')
        print()
    else:
        print('NO')

