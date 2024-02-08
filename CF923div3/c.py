
for _ in range(int(input())):
    n,m,k=map(int,input().split())
   
    s1=list(map(int,input().split()))
    arr1={ele for ele in s1 if ele<=k}

    s2=list(map(int,input().split()))
    arr2={ele for ele in s2 if ele<=k}

    if len(arr1.union(arr2))==k:
        aex=arr1.difference(arr2)
        bex=arr2.difference(arr1)
      
        if len(aex)>k//2:print('NO')
        elif len(bex)>k//2:print('NO')
        else:print('YES')
    else:
        print('NO')
 
