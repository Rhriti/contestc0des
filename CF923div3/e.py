for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[0 for _ in range(n)]
    maxm=n
    minm=1
    for i in range(k):
        if i%2==0:
            for j in range(i,n,k):arr[j]=minm;minm+=1
        else:
            for j in range(i,n,k):arr[j]=maxm;maxm-=1
    print(*arr)
