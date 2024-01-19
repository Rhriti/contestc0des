for _  in range(int(input())):
    n=int(input())
    d=input()

    t=None
    ans=''
    for i in range(n):
        #base
        if t is None:
            t=d[i]
            continue
        if t==d[i]:
            ans+=d[i]
            t=None
        else:
            continue
    print(ans)
