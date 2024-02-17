for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:print(0);continue

    aage=arr[0]
    piche=arr[-1]
    ac=0
    pc=0
    for i in range(n):
        if arr[i]==aage:ac+=1
        else:break 
    for i in range(n-1,-1,-1):
        if arr[i]==piche:pc+=1
        else:break 

    if aage==piche:
        if ac==pc==n:print(0)
        else:
            print(n-ac-pc)
    else:
        print(n-max(ac,pc))
 

