from collections import deque
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    premax=[0]
    postmax=deque()
    postmax.append(n-1)
    
    for i in range(1,n):
        if arr[i]>arr[premax[-1]]:premax.append(i)
        else:premax.append(premax[-1])
    for j in range(n-2,-1,-1):
        if arr[j]>arr[postmax[0]]:postmax.appendleft(j)
        else:postmax.appendleft(postmax[0])
    mid=arr.index(max(arr))
    c=0
    i=mid
    while i!=0:
        leftmaxindex=premax[i-1]
        for j in range(leftmaxindex,i):
            c+=arr[leftmaxindex]-arr[j]
        i=leftmaxindex
    i=mid
    while i!=n-1:
        rightmaxindex=postmax[i+1]
        for j in range(i+1,rightmaxindex):
            c+=arr[rightmaxindex]-arr[j]
        i=rightmaxindex
   
    print(c+sum(arr))
        
    
            
        
        
        
    
    
    
    
    
    
    
    
    
    