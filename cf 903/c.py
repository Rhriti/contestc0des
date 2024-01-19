for _ in range(int(input())):
    n=int(input())
    g=[]
    for _ in range(n):g.append(input())
    v=set()
    final=0
    for r in range(n):
        for c in range(n):
            if (r,c) not in v:
                maxm='a'
                arr=[]
                while (r,c) not in v:
                    v.add((r,c))
                    arr.append(g[r][c])
                    maxm=max(maxm,g[r][c])
                    t=r
                    r=c
                    c=n-1-t
                for ele in arr:
                    final+=abs(ord(ele)-ord(maxm))
    print(final)


    