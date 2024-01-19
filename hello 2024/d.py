for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    err=0
    for i in range(n-1):
        if abs(arr[i+1]-arr[i])!=1:
            err+=1

    
