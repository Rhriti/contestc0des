#this method is useful when divisor is atamx 10^4
n,m=map(int,input().split())
arr=list(map(int,input().split()))
from collections import defaultdict
g=defaultdict(int)
for ele in arr:g[ele%m]+=1
newarr=[]
for k in g.keys():newarr.append(k)
ans=defaultdict(int)

for i in range(len(newarr)-1):
    for j in range(i+1,len(newarr)):
        new_raminder=(newarr[i]+newarr[j])%m
        left=m-new_raminder
        if left==newarr[i]:
            t=[left,left,newarr[j]]
            t.sort()
            ans[tuple(t)]=(g[left]*(g[left]-1))//2
            ans[tuple(t)]*=newarr[j]
        elif left==newarr[j]:
            t=[left,left,newarr[i]]
            t.sort()
            ans[tuple(t)]=(g[left]*(g[left]-1))//2
            ans[tuple(t)]*=newarr[i]
        else:
            t=[left,newarr[i],newarr[j]]
            t.sort()
            ans[tuple(t)]=left*newarr[i]*newarr[j]

print(sum(ans.values()))        
