import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    x=input()
    s=input()
    while len(x)<=n+m-1:
        x+=x
    f=False
    for i in range(n):
        if x[i:].startswith(s):
            f=True
            opr=math.ceil((i+m)/n)
            break
    if not f:
        print(-1)
    else:
        print(math.ceil(math.log(opr,2)))