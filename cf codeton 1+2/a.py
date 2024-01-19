for _ in range(int(input())):
    n,k,x=map(int,input().split())
    if n>=k and x>=k-1:
        ans=(k-1)*k//2
       
        if k!=x:  
            ans+=(n-k)*x
        else:
            ans+=(n-k)*(x-1)
        print(ans)
    else:print(-1)
