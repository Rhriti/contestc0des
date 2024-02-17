for _ in  range(int(input())):
    x,y=map(int,input().split())
    big=max(x,y)
    small=min(x,y)
    if x==y:
        if x%2==0:print('YES')
        else:print('NO')
    else:
        if small%2==0:print('YES')
        else:
            if big%2==0:
                if big==2*small:print('NO')
                else:print('YES')
            else:print('NO')