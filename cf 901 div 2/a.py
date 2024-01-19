import heapq as hq
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    st=list(map(int,input().split()))
    hq.heapify(st)
    curr=b
    tf=0
    while curr!=0 :
        #base
        if len(st)==0:
            tf+=curr
            break
        minm=hq.heappop(st)
        if minm+curr>a:    
            if curr==1:
                tf+=1
                curr=min(a-1,minm)
            else:g
                wait=curr-1
                curr=min(minm,a-1)
                tf+=wait+1
        else:
            tf+=1
            curr=minm+curr-1
    print(tf)
            


