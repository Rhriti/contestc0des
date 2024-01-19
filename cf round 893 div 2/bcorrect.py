t=int(input())
while t:
    t-=1
    n,m,d=map(int,input().split())
    s=list(map(int,input().split()))
    s.insert(0,1-d)
    s.append(n+1)
    res=0
    for i in range(1,len(s)):
        res+=(s[i]-s[i-1]-1)//d
    res+=m
    print(f'totaleat {res}')
    l=[]
    for i in range(1,m+1):
        temp=((s[i+1]-s[i-1]-1)//d)-((s[i]-s[i-1]-1)//d+(s[i+1]-s[i]-1)//d)-1
        l.append(res+temp)
    x=min(l)
    print(x,l.count(x))