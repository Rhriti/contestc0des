for _ in range(int(input())):
    n,f,a,b=map(int,input().split())
    arr=list(map(int,input().split()))

    prev=0
    fl=True

    for ele in arr:
        f=max(f-(ele-prev)*a,f-b)
        prev=ele
        if f<=0:fl=False;break
    if fl:print('YES')
    else:print('NO')