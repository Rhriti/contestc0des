import heapq as hq
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    if k%2==0:
        s=sorted(s)
        for ele in s:
            print(ele,end='')
        print()
    else:
        oh=[]
        eh=[]
        for i in range(len(s)):
            if i%2==0:
                hq.heappush(eh,s[i])
            else:
                hq.heappush(oh,s[i])
        final=[]
        #merge karna hai bus
        for i in range(len(s)):
            if i%2==0:
                final.append(hq.heappop(eh))
            else:
                final.append(hq.heappop(oh))
        for ele in final:
            print(ele,end='')
        print()
    print('ans ')
    