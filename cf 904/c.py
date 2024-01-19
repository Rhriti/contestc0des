import bisect
for _ in range(int(input())):
    n,m=map(int,input().split())
    one=[]
    two=[]
    for _ in range(n):
        s,e=map(int,input().split())
        if s!=1:
            one.append([s,1])
            one.append([e+1,-1])
        if e!=m:
            two.append([s,1])
            two.append([e+1,-1])
    one.sort()
    two.sort()
    s=0
    maxm1=0
    for ele in one:
        s+=ele[1]
        maxm1=max(maxm1,s)
    s=0
    maxm2=0
    for ele in two:
        s+=ele[1]
        maxm2=max(maxm2,s)
    print(max(maxm1,maxm2))

    