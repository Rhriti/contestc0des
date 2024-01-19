from collections import defaultdict
def countCompatiblePairs(nodes,frm ,to, wei,val):
    g=defaultdict(list)
    par={1:[1,0]}
    for i in range(len(frm)):g[frm[i]].append([to[i],wei[i]]);par[to[i]]=[frm[i],wei[i]]
    dis={}
    v=set()
    def dfs(node,c):
        v.add(node)
        dis[node]=c
        for ch in g[node]:
            if ch[0] not in v:
                dfs(ch[0],c+ch[1])
    dfs(1,0)

    final=0
    for node in range(1,nodes+1):
        value=val[node-1]
        distance=0
        while True:
            distance+=par[node][1]
            node=par[node][0]
            if distance<=value:
                final+=1
            else:
                break
            if node==1:break
    print(final-1)
