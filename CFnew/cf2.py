for _ in range(int(input())):
    n,k=map(int,input().split())
    
    def func(index,coins,memo):
        if (index,coins) in memo:
            return memo[(index,coins)]
        
        if index==k:
            return 1
        if coins>=2**index:
            t=func(index+1,coins-(2**index),memo)
        else:
            return 1
        
        t+=func(index+1,coins,memo)
        memo[(index,coins)]=t
        
        return t
    
    print(func(0,n,{}))


