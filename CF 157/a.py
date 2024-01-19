for _ in range(int(input())):
    x,y,k=map(int,input().split())
    if y<=x:
        print(x)
    else:
        diff=y-x
        if k>=diff:
            print(y)
        else:
            print( 2*y-x-k )
    