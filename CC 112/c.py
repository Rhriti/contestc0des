import copy
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    anew=copy.deepcopy(a)
    anew.sort()
    pres=[anew[0]]
    for j in range(1,n):pres.append(pres[-1]+anew[j])
    t=0
    for j in range(1,n):
        if pres[j-1]>=anew[j]:t+=1
    print('arr',anew)
    print('pres',pres)
    print('sort karke',t)

    mark, cursum, ans = [0]*n, 0, []
    while True:
        ch = -1
        for i in range(n):
            if mark[i]: continue
            if a[i] > cursum:
                if ch == -1 or a[i] < a[ch]: ch = i
        if ch == -1: break
        mark[ch] = 1
        ans.append(a[ch])
        cursum += a[ch]
    print('real ans',n - len(ans))
    for i in range(n):
        if not mark[i]: ans.append(a[i])
    pres1=[ans[0]]
    for j in range(1,n):pres1.append(pres1[-1]+ans[j])
    print(*pres1)
    print(*ans)