import math
for _ in range(int(input())):
    n=int(input())
    i=1
    j=10**18
    ans=float('inf')
    while i<=j:
        mid=(i+j)//2
        ice_creams=((mid-1)*mid)/2
            
        if ice_creams>=n:
            ans=min(ans,mid)
            j=mid-1
        else:
            i=mid+1
    ways=ans*(ans-1)/2
    if ways==n:
        print(ans)
    else:
        ans-=1
        ways=ans*(ans-1)/2
        print(ans+(n-ways))

           










    