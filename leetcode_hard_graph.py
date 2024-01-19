from collections import defaultdict
class Solution:
    def minOperationsQueries(self, n , ed , que) :
        g=defaultdict(list)
        for u,v,w in ed:
            g[u].append([v,w])
            g[v].append([u,w])
            
        final=[]
        print(g)
        for u,v in que:
            gnew=defaultdict(int)
            v=set()
            
            def dfs(node):
                v.add(node)
                if node==v:
                    if len(gnew)==1:
                        final.append(0)
                    else:
                        print('yeah')
                        maxm=max(gnew.values())
                        sums=sum(gnew.values())
                        final.append(sums-maxm)
                    return 
                
                for ch in g[node]:
                    if ch[0] not in v:
                        gnew[ch[1]]+=1
                        dfs(ch[0])
                        gnew[ch[1]]-=1
            dfs(u)
        print(final)
        return final
                
            
x=Solution()
x.minOperationsQueries(7,
[[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]],
[[0,3],[3,6],[2,6],[0,6]])