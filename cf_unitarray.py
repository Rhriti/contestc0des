import math
for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    g={1:0,-1:0}
    for ele in d:
        g[ele]+=1
    if g[1]>=g[-1]:
        if g[-1]%2==0:
            print(0)
        else:
            print(1)
    else:
        op=math.ceil((g[-1]-g[1])/2)
        g[1]+=op
        g[-1]-=op
        if g[-1]%2==0:
            print(op)
        else:
            print(op+1)          
