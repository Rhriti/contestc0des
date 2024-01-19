from collections import defaultdict
class Solution:
    def __init__(self):
        self.flag=False

    def isPossible(self,paths):
        g=defaultdict(list)
        nodes=set()
        edges=0
        for r in range(len(paths)):
            for c in  range(len(paths[0])):
                if paths[r][c]==1:
                    g[r].append(c)
                    nodes.add(r)
                    nodes.add(c)
                    edges+=1
                
        def dfs(start,node,visit):
            t=False
           
            for ch in g[node]:
                if (node,ch) not in visit:
                    visit.add((node,ch))
                    visit.add((ch,node))
                    t=True
                    dfs(start,ch,visit)
            
            if t is False and start==node and len(visit)==edges:
                self.flag=True

        for n in nodes:
            self.flag=False
            dfs(n,n,set())
            if self.flag is True:
                return 1
        return 0

s=Solution()
print(s.isPossible(
# [
# [0 ,1 ,-1 ,-1 ,1 ,1],[
# 1 ,0 ,1 ,1 ,1 ,1],[
# 1 ,1 ,0 ,1 ,-1 ,1],[
# -1 ,1, 1 ,0 ,1 ,1],[
# 1 ,1 ,1 ,1 ,0 ,-1],[1 ,1 ,-1 ,-1 ,-1 ,0]

# ]
[
[0 ,1 ,1 ,1, 1],[
1 ,0, -1, 1, -1],[
1 ,-1, 0, 1, -1],[
1, 1, 1, 0, 1]
,[1, -1, -1, 1, 0]]


))