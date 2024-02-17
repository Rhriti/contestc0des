for _ in range(int(input())):
    n,k=map(int,input().split())
    double=2*n-2
    if k<=2*double:
        if k%2==0:print(k//2)
        else:print(((k-1)//2)+1)
    else:
        left=k-2*double
        print(left+double)
   