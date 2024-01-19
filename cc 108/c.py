import math
from collections import Counter,defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    fo={}
    lo={}
    prev={}
    for i in range(n):
        if arr[i] not in fo:fo[arr[i]]=i;prev[arr[i]]=i
    for i in range(n-1,-1,-1):
        if arr[i] not in lo:lo[arr[i]]=i
    
    maxgap=defaultdict(lambda: -float('inf'))
    for j in range(n):
        if j-prev[arr[j]]==1:
            maxgap[arr[j]]=max(maxgap[arr[j]],0)
        else:
            diff=j-prev[arr[j]]-1
            if diff%2==1:maxgap[arr[j]]=max(maxgap[arr[j]],diff//2+1)
            else:maxgap[arr[j]]=max(maxgap[arr[j]],diff//2)
    
        prev[arr[j]]=j
    final=[]
    for clan,gap in maxgap.items():
        final.append( [ max(gap,fo[clan],n-1-lo[clan]) , clan  ]    )
    final.sort()
    print(final[0][1],final[0][0])






            
