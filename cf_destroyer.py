for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    g={}
    for i in range(100):
        g[i]=0
    for ele in d:
        g[ele]+=1
    f=False
    for i in range(100):
        if i==0:
            prev=g[0]
        else:
            if g[i]<=prev:
                prev=g[i]
            else:
                f=True
                break
    if f:
        print('NO')
    else:
        print('YES')
