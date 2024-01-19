n,k,p=map(int,input().split())
prod=[0]*(k)
devplan=[]
devmin=[float('inf')]*(n)
cost=[]
promin=0
sums=[0]*(k)
for x in range(n):
    arr=list(map(int,input().split()))
    for i in range(1,len(arr)):
        devmin[x]=min(devmin[x],arr[i])
        sums[i-1]+=arr[i]
    devplan.append(arr[1:])
    cost.append(arr[0])
print(devmin)
f=False
for ele in sums:
    if ele<p:
        f=True
        print(-1)
        break
if not f:
    memo={}
    def dp(r,promin):
        #base
        # if all(ele >= p for ele in prod):return 0
        if promin>=p:return 0
        if r==n:
            return float('inf')
        # print((r,tuple(prod)))

        if (r,promin) in memo:
            return memo[(r,promin)]
   
        mc=dp(r+1,promin)
        # for c in range(k):
        #     prod[c]+=devplan[r][c]

        mc2=cost[r]+dp(r+1,promin+devmin[r])
        # for c in range(k):
        #     prod[c]-=devplan[r][c]

        memo[(r,promin)]=min(mc,mc2)
        return min(mc,mc2)

    print(dp(0,promin)) #minm cost
