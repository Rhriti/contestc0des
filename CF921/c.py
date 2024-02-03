for _ in range(int(input())):
    n,k,m=map(int,input().split())
    inmese={chr(ele) for ele in range(ord('a'),ord('a')+k,1)}
    s=input()
    
    sets=set()
    lasts=''
    for i in range(m):
        if s[i] in inmese:
            sets.add(s[i])
            if len(sets)==k:lasts+=s[i];sets=set()

    if len(lasts)>=n:print('YES')
    else:
        lasts+=(inmese-sets).pop()
        lasts+='a'*(n-len(lasts))
        print('NO')
        print(lasts)
        
        