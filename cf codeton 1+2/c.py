from collections import defaultdict
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    arr=[]
    for i in range(len(s)):
        arr.append([s[i],i,i])
    arr.sort()
    lr=lc=0
    rr=rc=n-1
    v=defaultdict(int)
    def RC(i,j):
        while (i,j) in v:
            i-=1
            j-=1
        return i,j
    def LC(i,j):
        while (i,j) in v:
            i+=1
            j+=1
        return i,j
    ans=defaultdict(int)
    for i in range(len(arr)):
        ele=arr[i][0]
        r=arr[i][1]
        c=arr[i][1]
        v[(r,c)]=max(v[(r,c)],  rc+rr-lc-lr+2   )
        ans[ele]=max(ans[ele],v[(r,c)])
        if r==lr and c==lc:
            lr,lc=LC(lr,lc)
        elif r==rr and c==rc:
            rr,rc=RC(rr,rc)
    
    final=[]
    for i in range(1,k+1):
        if i in ans:final.append(ans[i])
        else:final.append(0)
    print(*final)

