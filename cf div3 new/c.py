for _ in range(int(input())):
    n,k,x=map(int,input().split())
    ll=k*(k+1)//2
    new=n-k
    ul=n*(n+1)//2 -(new*(new+1)//2)
    if ll<=x<=ul:
        print('YES')
    else:
        print('NO')