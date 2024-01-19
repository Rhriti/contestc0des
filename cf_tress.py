class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def f(n1,n2):
    au=n1
    av=n2
    parents={n1}
    while par[n1]!=n1:
        n1=par[n1]
        parents.add(n1)
    if n2 in parents:
        return 0
    while par[n2]!=n2:
        n2=par[n2]
        if n2 in parents:
            if au<n2<av:
                return 1
            else:
                return 0
    

n=int(input())
arr=list(map(int,input().split()))
par={1:1}
from collections import defaultdict
g=defaultdict(list)
node=2
for ele in arr:
    par[node]=ele
    g[ele].append(node)
    g[node].append(ele)
    node+=1
count=0
val={}

def valueasign(node,count):
    val[node]=count
    if len(g[node])==1 and 
 



for i in range(1,n+1):
    for j in range(i+1,n+1):
        count+=f(i,j)
print(f'ans is {count}')



