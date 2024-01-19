import heapq as hq
from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    g=Counter(s)
    ss=sorted(s)
    eh=[]
    oh=[]
    for i in range(len(s)):
        if i%2==0:
            hq.heappush(eh,s[i])
        else:
            hq.heappush(oh,s[i])
    order=[]
    for i in range(n):
        if g[ss[i]]<=0:
            continue
        req=ss[i]
        if i%2==0: #we are at even position
            if req==eh[0]:
                out=hq.heappop(eh)
                order.append(out)
                g[out]-=1
            else:
                if (len(ss)-len(order))%2==0:
                    out=hq.heappop(oh)
                    order.append(out)
                    g[out]-=1
                    t=eh
                    eh=oh
                    oh=t
                else:
                    out=hq.heappop(eh)
                    order.append(out)
                    g[out]-=1
        else:
            if req==oh[0]:
                out=hq.heappop(oh)
                order.append(out)
                g[out]-=1
            else:
                if (len(ss)-len(order))%2==0:
                    out=hq.heappop(eh)
                    order.append(out)
                    g[out]-=1
                    t=eh
                    eh=oh
                    oh=t
                else:
                    out=hq.heappop(oh)
                    order.append(out)
                    g[out]-=1
    
    print('ans is ',order)





