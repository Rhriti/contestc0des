# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    arr=[]
    for ele in s:arr.append(int(bin(ele)[-1]))
    newarr=arr[:k]
    g=Counter(newarr)
    i=0
    j=k-1
    count=0
    if len(g)==1 and list(g.keys())[0]==0:count+=1
    # print('arr',arr)
    # print('newarr',newarr)
    # print('count',count)

    for j in range(j+1,len(s)):
        g[arr[i]]-=1
        g[arr[j]]+=1
        if g[arr[i]]==0:
            del g[arr[i]]
        i+=1
        if len(g)==1 and list(g.keys())[0]==0:count+=1

    print((len(s)-k+1)-count)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    