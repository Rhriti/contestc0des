# from sys import stdin
# import heapq as hq
# def input(): return stdin.readline().rstrip("\r\n")
# from collections import defaultdict
# from random import getrandbits
# # Anti hack: https://codeforces.com/blog/entry/101817
# class Wrapper(int):
#     RANDOM = getrandbits(32)
#     def __init__(self, x):
#         int.__init__(x)
#     def __hash__(self):
#         return super(Wrapper, self).__hash__() ^ Wrapper.RANDOM



# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     g=defaultdict(list)
#     for _ in range(m):
#         u,v,w=map(int,input().split())
#         g[u].append([v,w])
#         g[v].append([u,w])
#     bike=list(map(int,input().split()))
    
#     st=[[0,1,bike[0]]]  #[cost,node,bike speed]
#     total=0
#     v=set()
#     while st :
#         out=hq.heappop(st)
#         if out[1]==n:total=out[0];break
#         v.add(out[1])
#         for ch in g[out[1]]:
#             if ch[0] not in v:
#                 hq.heappush(st,[out[0]+ch[1]*min(out[2],bike[out[1]-1]),ch[0],min(out[2],bike[out[1]-1])])
    
#     print('final',total)

from sys import stdin
import heapq as hq
def input(): return stdin.readline().rstrip("\r\n")
from collections import defaultdict
from random import getrandbits
# Anti hack: https://codeforces.com/blog/entry/101817
# class Wrapper(int):
#     RANDOM = getrandbits(32)
#     def __init__(self, x):
#         int.__init__(x)
#     def __hash__(self):
#         return super(Wrapper, self).__hash__() ^ Wrapper.RANDOM

from random import getrandbits

class WrapperTuple(tuple):
    RANDOM = getrandbits(32)

    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    def __hash__(self):
        return super().__hash__() ^ self.RANDOM


for _ in range(int(input())):
    n,m=map(int,input().split())
    g=defaultdict(list)
    for _ in range(m):
        u,v,w=map(int,input().split())
        g[u].append([v,w])
        g[v].append([u,w])
    bike=list(map(int,input().split()))
    
    st=[[0,1,bike[0]]]  #[cost,node,bike speed]
    v={}
    total=0
    while st :
        out=hq.heappop(st)
        if out[1]==n:total=out[0];break
        if (out[1],out[2]) in v and v[(out[1],out[2])]<=out[0]:continue
        v[(out[1],out[2])]=out[0]
        for ch in g[out[1]]:
            hq.heappush(st,[out[0]+ch[1]*min(out[2],bike[out[1]-1]),ch[0],min(out[2],bike[out[1]-1])])
    
    print(total)







