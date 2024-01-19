#dijksta somple
import heapq as hq
for _ in range(int(input())):
    n,k,a,b=map(int,input().split())
    cord={}
    maj=set()
    for i in range(1,n+1):
        cord[i]=tuple(map(int,input().split()))
    # print(cord)

    if a<=k and b<=k:
        print(0)
    else:
    
        cost=[None for _ in range(n+1)]
        cost[a]=0
        # print(cost)
        st=[[0,a]]
        while st:
            out=hq.heappop(st)
            node=out[1]
            curr_cost=out[0]
            cost[out[1]]=out[0]
            if out[1]==b:
                break
            for ch in range(1,n+1):
                if ch==node:continue
                # print(ch)
                if cost[ch]==None:
                    if node<=k and ch<=k:
                        hq.heappush(st,[curr_cost,ch])
                    else:
                        hq.heappush(st,[  curr_cost + abs(cord[node][0]-cord[ch][0])  + abs(cord[node][1]-cord[ch][1])  , ch])
        print(cost[b])