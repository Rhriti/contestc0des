import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr=[0]+arr+[x]
   
    maxm=-1
    for i in range(len(arr)-1):
        maxm=max(maxm,arr[i+1]-arr[i])
    maxm=max(maxm,2*(arr[-1]-arr[-2]))
    print(maxm)
