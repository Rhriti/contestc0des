from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    g=defaultdict(list)
    for i in range(2*n):
        g[arr[i]].append(i)

    # print(g)
    hp=[]
    for k,v in g.items():
        hp.append([max(v[0],v[1])-min(v[0],v[1]),k])
    hp.sort()
    final=[]
    for ele in hp:
        final.append(ele[1])
    print(*final)