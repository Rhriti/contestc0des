for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    ad=[]
    for i in range(len(a)):
        ad.append([a[i],d[i]])
    ad.sort()
    sets=set()
    
