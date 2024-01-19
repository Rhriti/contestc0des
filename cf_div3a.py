for _ in range(int(input())):
    n,m,k,H=map(int,input().split())
    h=list(map(int,input().split()))
    c=0
    for ele in h:
        diff=abs(H-ele)
        if k<=diff<=k*(m-1):
            c+=1
    print(c)
    print('upar')


