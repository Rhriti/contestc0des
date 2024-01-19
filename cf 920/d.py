for _ in range(int(input())):
    n,m=map(int,input().split())
    arrn=list(map(int,input().split()))
    arrm=list(map(int,input().split()))

    arrn.sort()
    suff_n=[arrn[-1] for _ in range(n)]
    pref_n=[arrn[0]]
    for i in range(1,n):pref_n.append(arrn[i]+pref_n[-1])
    for i in range(n-2,-1,-1):suff_n[i]=suff_n[i+1]+arrn[i]

    arrm.sort(reverse=True)
    pref_m=[arrm[0]]
    suff_m=[arrm[-1] for _ in range(m)]
    for i in range(m-2,-1,-1):suff_m[i]=suff_m[i+1]+arrm[i]
    for i in range(1,m):pref_m.append(arrm[i]+pref_m[-1])
    maxm=-1

    for i in range(n+1):
        curr=0
        if i-1>=0:
            curr+=abs(pref_m[i-1]-pref_n[i-1])
        if i+abs(n-m)<=m-1:
            curr+=abs(suff_m[i+abs(n-m)]-suff_n[i])
        maxm=max(maxm,curr)
    
    print(maxm)

