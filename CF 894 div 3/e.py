import heapq as hq
for _ in range(int(input())):
    n,m,d=map(int,input().split())
    arr=list(map(int,input().split()))
    maxm=[0]*len(arr)
    st=[]
    sums=0
    for i in range(len(arr)):
        if arr[i]>0:
            if len(st)==0:
                hq.heappush(st,arr[i])
                sums=arr[i]
                maxm[i]=sums
            elif len(st)<m:
                hq.heappush(st,arr[i])
                sums+=arr[i]
                maxm[i]=sums
            else:
                sums+=arr[i]
                hq.heappush(st,arr[i])
                out=hq.heappop(st)
                sums-=out
                maxm[i]=sums
    ans=0
    for i in range(len(maxm)):
        ans=max(ans,maxm[i]-(i+1)*d)
    print(ans)

