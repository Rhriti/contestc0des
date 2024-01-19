
class Solution:
	def findMotherVertex(self, V, adj):
		
		def dfs(node,v):
		    v.add(node)
		    for ch in adj[node]:
		        if ch not in v:
		            dfs(ch,v)
		    if len(v)==len(adj):
		        return True,None
		    else:
		        return False,v
	    
	    notreach=set()
	    for node in range(len(adj)):
	        if node not in notreach:
	            ans=dfs(node,set())
	            if ans[0]:
	                return node
	            else:
	                notreach.union(ans[1])
	    return -1
#time complexity is O(V+E)