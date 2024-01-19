from collections import defaultdict
for _ in range(int(input())):
    n,m,d=list(map(int,input().split()))
    s=list(map(int,input().split()))
    totaleat=0
    for i in range(len(s)-1):
        totaleat+=(s[i+1]-s[i]-1)//d
    totaleat+=(n-s[-1])//d
    totaleat+=len(s)
    if s[0]!=1:
        totaleat+=1
        totaleat+=(s[0]-1-1)//d
    # print(f'totaleat {totaleat}')

    #lol
    minm=float('inf')
    g=defaultdict(int)
    for i in range(1,len(s)-1):
        eat=totaleat-((s[i]-s[i-1]-1)//d) -((s[i+1]-s[i]-1)//d )+((s[i+1]-s[i-1]-1)//d)  -1
        g[eat]+=1
        minm=min(minm,eat)
       
    
    #for s[0]
    if s[0]!=1:
        eat=totaleat -2-((s[1]-s[0]-1)//d)-(s[0]-2)//d  + (1+(s[1]-1-1)//d)
        g[eat]+=1
        minm=min(minm,eat)
    
    else:
        g[totaleat]+=1
        minm=min(minm,totaleat)
   
    #for s[-1]
    eat=totaleat-((s[-1]-s[-2]-1)//d )- ((n-s[-1])//d) -1 + ((n-s[-2])//d)
    g[eat]+=1
    minm=min(minm,eat)

    print(minm,end=' ')
    print(g[min(g.keys())])

    

