for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    eq=sum(arr)//n
    curr=0
    f=False

    for ele in arr:
        d=ele-eq
        curr+=d
        if curr<0:f=True;break
    if f:print('NO')
    else:print('YES')