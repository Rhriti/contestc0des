for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    minm=min(arr)
    index=None
    for i in range(n-1,-1,-1):
        if arr[i]==minm:
            index=i
            break
    
    rem=k%arr[index]
    if rem==0:
        times=k//arr[index]
        final=[times]*(index+1)
        final.extend([0]*(n-index-1))
        print(*final)
    else:
        times=(k//arr[index])-1
        left=arr[index]+(k%arr[index])
        f=False
        for j in range(n-1,index,-1):
            if arr[j]<=left:
                f=True
                i2=j
                break
        if f:
            final=[times+1]*(index+1)
            final.extend([1]*(i2-index))
            final.extend([0]*(n-i2-1))
            print(*final)
        else:
            final=[times+1]*(index+1)
            final.extend([0]*(n-index-1))
            print(*final)
 


