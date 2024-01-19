for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    prea=[a[0]]
    maxb=[b[0]]
    for i in range(1,n):
        prea.append(prea[-1]+a[i])
        maxb.append(max(maxb[-1],b[i]))
    # print('maxb',maxb)
    # print('pres',prea)

    maxm=-1
    for i in range(n):
        if i==k:
            break
        maxm=max(maxm,prea[i]+ maxb[i]*(k-i-1)   )
    print(maxm)

    