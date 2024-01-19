for _ in range(int(input())):
    n,k,q=map(int,input().split())
    d=list(map(int,input().split()))

    def f(index,leftk):
        if index==k-1:
            if max(d[:k])<=q:
                return 1
            return 0
        
        if leftk==1:
            if d[index]<=q:
                return 1
            return 0
        
        if d[index]<=q:
            return f(index-1,leftk-1)
        return 0
    
    ans=0
    for i in range(k-1,len(d)):
        ans+=f(i,k)
    print(ans)
