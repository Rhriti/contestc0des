from collections import defaultdict
for _ in range(int(input())):
    g=defaultdict(list)
    s=set()
    for _ in range(4):
        a,b=map(int,input().split())
        s.add(a)
        g[a].append(b)
    
    final=1

    for ele in s:final*=abs(g[ele][0]-g[ele][1])
    print(final)

    
