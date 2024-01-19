for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if c%2==1:
        if b>a:
            print('Second')
        else:
            print('First')
    else:
        if a>b:
            print('First')
        else:
            print('Second')
    