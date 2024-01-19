import bisect
for _ in range(int(input())):
    n,m,h=map(int,input().split())
    ans=[]
    for i in range(n):
        timepq=list(map(int,input().split()))
        timepq.sort()
        sums=[]
        c=0
        for ele in timepq:
            c+=ele
            sums.append(c)
        solved=bisect.bisect_right(sums,h)
        p=sum(sums[:solved])
        ans.append([-solved,p])
        if i==0:
            rinkupoint=-solved
            rinkupenalty=p

    ans.sort()
    fa=0
    # print(ans)
    # print(rinkupoint,rinkupenalty)
    for i in range(len(ans)):
        if ans[i][0]==rinkupoint and ans[i][1]==rinkupenalty:
            fa=i
            break
    print(fa+1)



        