for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    diff=[]
    for i in range(n-1):
        diff.append(s[i+1]-s[i])
    maxm=0
    c=0
    for ele in diff:
        if ele>k:
            c=0
        else:
            c+=1
            maxm=max(maxm,c)
  
    print(n-(maxm+1))

        
