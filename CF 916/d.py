import heapq as hq
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    anew=[]
    bnew=[]
    cnew=[]
    for i in range(n):anew.append([a[i],i]);bnew.append([b[i],i]);cnew.append([c[i],i])
    anew.sort(reverse=True)
    bnew.sort(reverse=True)
    cnew.sort(reverse=True)

    
    
   


    
    