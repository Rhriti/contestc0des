from collections import deque
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    news=[[s[i],i] for i in range(len(s))]
    s.sort()
    news.sort()

    sums=0
    pres=[]
    for ele in s:
        sums+=ele
        pres.append(sums)
    sums=0
    ss=deque()
    ss.append(0)
    for i in range(len(s)-1,-1,-1):
        sums+=s[i]
        ss.appendleft(sums)
    final=[]
    for i in range(len(s)):
        final.append(ss[i+1]-s[i]*(len(s)-1-i)+s[i]*(i+1)-pres[i]+len(s))
    ans=[None]*len(s)
    for i in range(len(news)):
        ans[news[i][1]]=final[i]
    for ele in ans:
        print(ele,end=' ')
    print()

    
    


