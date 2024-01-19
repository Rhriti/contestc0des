from collections import defaultdict
from math import comb
for _ in range(int(input())):
    n=int(input())
    g=defaultdict(list)
    for _ in range(n-1):
        u,v=map(int,input().split());g[u].append(v);g[v].append(u)
    #root at 1
    numb={}
    v=set()
    def dfs(node):
        v.add(node)
        t=1
        for ch in g[node]:
            if ch not in v:
                t+=dfs(ch)

        numb[node]=t 
        return t
                   
    dfs(1)
    print(numb)

    v=set()
    def dfs2(node):
        v.add(node)
        if len(g[node])==1:return 2
        ways=1
        odds=0
        news=1
        for ch in g[node]:
            if ch not in v:
                if numb[ch]==0:
                    ways*=dfs2(ch)
                else:
                    news*=dfs2(ch)
                    odds+=1
        if odds%2==1:
            ways*=2*news*comb(odds,odds//2)
        else:
            ways*=news*(comb(odds,odds//2)+2*comb(odds,odds//2+1)) 
        return ways       

        
    print('ways',dfs2(1)%(10**9+7))            



# mod = 10**9 + 7
# def dfs(graph, start=0):
#     n = len(graph)

#     fac = [1]*(n+1)
#     for i in range(2, n+1): fac[i] = i*fac[i-1] % mod
#     inv = fac[:]
#     inv[-1] = pow(fac[-1], mod-2, mod)
#     for i in reversed(range(n)): inv[i] = inv[i+1] * (i+1) % mod
#     def C(n, r):
#         if n < r or r < 0: return 0
#         return fac[n] * inv[r] % mod * inv[n-r] % mod

#     dp = [[0, 0] for _ in range(n)]
#     subsz = [0]*n
#     visited, finished = [False] * n, [False] * n

#     stack = [start]
#     while stack:
#         start = stack[-1]

#         # push unvisited children into stack
#         if not visited[start]:
#             visited[start] = True
#             for child in graph[start]:
#                 if not visited[child]:
#                     stack.append(child)
#         else:
#             stack.pop()

#             # base case
#             subsz[start] = 1
#             prod, odds = 1, 0

#             # update with finished children
#             for child in graph[start]:
#                 if finished[child]:
#                     subsz[start] += subsz[child]
#                     prod = prod*dp[child][subsz[child] % 2] % mod
#                     odds += subsz[child]%2

#             finished[start] = True

#             if odds%2 == 0:
#                 dp[start][1] = prod * (C(odds, odds//2) + C(odds, odds//2 + 1)) % mod
#             else:
#                 dp[start][0] = 2 * prod * C(odds, odds//2) % mod
#     # print(dp)
#     return (dp[0][0] + 2*dp[0][1])%mod

# for _ in range(int(input())):
#     n = int(input())
#     tree = [ [] for _ in range(n)]
#     for i in range(n-1):
#         u, v = map(int, input().split())
#         tree[u-1].append(v-1)
#         tree[v-1].append(u-1)
#     print(dfs(tree))