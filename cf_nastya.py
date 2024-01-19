from collections import defaultdict
for _ in range(int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    zerocost=list(map(int,input().split()))
    t=[ele-1 for ele in zerocost]
    zerocost=set(t)
    g=defaultdict(list)
    for i in range(n):
        g[i]
        d=list(map(int,input().split()))
        if len(d)==1:
            continue
        else:
            d=d[1:]
            t=[ele-1 for ele in d]
            d=t
            g[i]=d
    
    fcost=[0]*n
    visit={}
    def dfs(index):
        if index in zerocost:
            fcost[index]=0
            return 0
        if index in visit:
            return visit[index]
        
        t=False
        s=0
        for ch in g[index]:
            t=True
            s+=dfs(ch)
        if t:
            fcost[index]=min(s,c[index])
        else:
            fcost[index]=c[index]
        visit[index]=fcost[index]
        return fcost[index]

    for i in range(n):
        if i not in visit:
            dfs(i)
    for i in range(len(fcost)-1):
        print(fcost[i],end=' ')
    print(fcost[-1])

                  