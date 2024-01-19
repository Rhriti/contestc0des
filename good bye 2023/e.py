#may give tle due to recursive approach
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    par=list(map(int,input().split()))   #par[node-1]
    val=list(map(int,input().split()))   #val[node-1]
    g=defaultdict(list)
    for i in range(n-1):g[par[i]].append(i+2)


    f={}
    c=defaultdict(int)
    def dfs(node):
        c[val[node-1]]+=1
        f[node]=len(c)

        for ch in g[node]:dfs(ch)

        c[val[node-1]]-=1
        if c[val[node-1]]==0:del c[val[node-1]]
        

    dfs(1)

    def dfs1(node):

        if len(g[node])==2:
            left=dfs1(g[node][0])
            right=dfs1(g[node][1])
            maxm[0]=max(maxm[0],(left-f[node]+1)*(right-f[node]+1))
            return max(left,right,f[node])
        
        elif len(g[node])==1:
            left=dfs1(g[node][0])
            maxm[0]=max(maxm[0],left-f[node]+1)
            return max(left,f[node])
        elif len(g[node])==0:
            maxm[0]=max(maxm[0],1)
            return f[node]
        else:
            one=max(dfs1(g[node][0]),dfs1(g[node][1]))
            two=min(dfs1(g[node][0]),dfs1(g[node][1]))
            for i in range(2,len(g[node])):
                ch=g[node][i]
                if two<dfs1(ch)<one:two=dfs1(ch)
                if dfs1(ch)>=one:
                    t=one
                    one=dfs1(ch)
                    two=t 
            maxm[0]=max(maxm[0],(one-f[node]+1)*(two-f[node]+1))
            return max(one,f[node])

    maxm=[0]
    dfs1(1)
    print(maxm[0])

