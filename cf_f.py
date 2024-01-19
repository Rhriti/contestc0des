from collections import defaultdict,Counter
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    s=Counter(s)
    g=defaultdict(int)
    for i in range(n):g[i]
    for ele in s.keys():
        if ele>n:
            continue
        else:
            for j in range(ele,n+1,ele):
                g[j]+=s[ele]
    print(max(g.values()))
  
