from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    amb=[[a[i]-b[i],i+1] for i in range(n)]
    amb.sort(reverse=True)
    g=defaultdict(list)
    for ele  in amb:
        g[ele[0]].append(ele[1])
    # print(g)
    # print(amb)
    node=amb[0][0]
    g[node].sort()
    print(len(g[node]))
    for ele in g[node]:
        print(ele,end=' ')
    print()

    
