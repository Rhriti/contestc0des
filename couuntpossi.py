from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    root={x for x in range(1,n+1)}
    g=defaultdict(list)
    for _ in range(n-1):
        u,v=map(int,input().split())
        g[u].append(v)
        root.remove(v)
    # print(root.pop())
    root=root.pop()
    # print(root)
    levels={}
    below={}
    def dfs(node,c):
        levels[node]=c
        belows=0
        for ch in g[node]:
            belows+=dfs(ch,c+1)
            belows+=1
        below[node]=belows
        return belows
    dfs(root,0)
    
    
    arr=[0 for _ in range(n+1)]
    for node in range(1,n+1):
        arr[levels[node]]+=1
        arr[n-below[node]]-=1
    final=[]
    sums=0
    for ele in arr:
        sums+=ele
        final.append(sums)
    final.pop()
    print(*final)



    