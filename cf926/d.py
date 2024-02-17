from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    g=defaultdict(list)
    counter=defaultdict(int)
    for _ in range(n-1):
        u,v=map(int,input().split())
        g[u].append(v)
        counter[v]+=1
        counter[u]+=1
        g[v].append(u)

    root=1
    below={}
    v=set()

    def dfs(node):
        v.add(node)
        b=1
        for ch in g[node]:
            if ch not in v:
                b+=dfs(ch)
        below[node]=b
        return b
    dfs(root)


    st=[1]
    v={1}
    while st:
        out=st.pop()
        b=1
        for ch in g[out]:
            if ch not in v:
                v.add(ch)
                b+=below[ch]



        
    
