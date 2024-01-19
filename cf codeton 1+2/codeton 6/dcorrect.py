for t in range (int(input())):  
    n=int(input())
    c=list(map(int,input().split()))
    k=int(input())
    mi=c[n-1]
    lst=[c[-1]]
    for i in range (n-2,-1,-1):
        mi=min(mi,c[i])
        lst.append(mi)
    print(lst)
    a=lst[::-1]
    kq=[k//a[0]]+[0]*(n-1)
    k-=a[0]*(k//a[0])
    for i in range (1,n):
        if a[i]>a[i-1]:
            kq[i]+=min(kq[i-1],k//(a[i]-a[i-1]))
            k=k-(a[i]-a[i-1])*kq[i]          
        else:
            kq[i]+=kq[i-1]
    print(*kq) 