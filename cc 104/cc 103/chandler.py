from collections import deque
for _ in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    d=[]
    dback=[]
    for i in range(n):
        d.append(a[i]-m[i])
        dback.append(a[i]-m[i])
    # minchie=deuqe()
    for i in range(n-2,-1,-1):
        if m[i]>=d[i+1]:
            pass
        else:
            aage_tak_udane=d[i+1]-m[i]
            apun_udane=max(d[i],aage_tak_udane)
            d[i]=apun_udane
    for i in range(1,n,1):
        if m[i]>=dback[i-1]:
            pass
        else:
            aage_tak_udane=dback[i-1]-m[i]
            apun_udane=max(dback[i],aage_tak_udane)
            dback[i]=apun_udane
    final=[None]*n
    final[0]=d[0]
    final[-1]=dback[-1]
    for i in range(1,n-1):
        if m[i]>=d[i+1]+dback[i-1]:
            final[i]=d[i]
        else:
            aage=d[i+1]+dback[i-1]-m[i]
            apun=max(d[i],aage)
            final[i]=apun
    print(*final)