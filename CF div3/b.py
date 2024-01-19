for _ in range(int(input())):
    n=int(input())
    minm=float('inf')
    for _ in range(n):
        a,b=map(int,input().split())
        if b%2==0:
            minm=min(minm,a+  ( b//2 ) -1  )
        else:
            minm=min(minm,a+( (b-1)//2 ))
    print(minm)
