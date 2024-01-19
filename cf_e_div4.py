import math
for _ in range(int(input())):
    n,c=map(int,input().split())
    s=list(map(int,input().split()))
    ss=sum(s)
    sss= sum([i*i for i in s])
    w=((-2*ss)+math.sqrt(4*ss*ss-4*n*(sss-c)))/(2*n)
    w2=((-2*ss)-math.sqrt(4*ss*ss-4*n*(sss-c)))/(2*n) 
    w=w/2
    w2=w2/2
    ans=[]
    if int(w)==w :
        ans.append(w)
    if int(w2)==w2:
        ans.append(w2)
    print(int(max(ans)))
