for _ in range(int(input())):
    n=int(input())
    totalmin=float('inf')
    totalsecminlist=0
    minsec=float('inf')
    for _ in range(n):
        input()
        arr=list(map(int,input().split()))
        if arr[0]<arr[1]:
            minm=arr[0]
            secmin=arr[1]
        else:
            minm=arr[1]
            secmin=arr[0]
        for i in range(2,len(arr)):
            if arr[i]<=minm:
                t=minm
                minm=arr[i]
                secmin=t
            else:
                if minm<arr[i]<secmin:
                    secmin=arr[i]
        totalsecminlist+=secmin
        minsec=min(minsec,secmin)
        totalmin=min(totalmin,minm)
    print(totalmin+totalsecminlist-minsec)
    
   