from collections import Counter,defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    g=Counter(arr)
    # if len(g)==1 :print('ans',-1);continue
    c=0
    for v in g.values():
        if v>1:c+=1
    if c==0 or c==1:print(-1);continue
  
    gnew=defaultdict(list)
    b=[1 for _ in range(len(arr))]
    for i in range(len(arr)):gnew[arr[i]].append(i)
    f=False
    for v in gnew.values():
        if len(v)>1:
            if not f:
                f=True
                b[v[0]]=2
            else:
                b[v[0]]=3

    print(*b)
  