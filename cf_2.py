from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=[]
    for _ in range(n):
        a,b=map(int,input().split())
        arr.append([a,-b])
    arr.sort()
    sums=0
    count=0
    broken=0
    gout=defaultdict(int)
    for i in range(len(arr)):
        if arr[i][0]<=broken:
            continue
        else:
            sums+=-arr[i][1]
            count+=1
            broken=max(broken,count)
            gout[arr[i][0]]+=1
            if count in gout:
                t=count
                count-=gout[count]
                del gout[t]
                
    print(sums)
