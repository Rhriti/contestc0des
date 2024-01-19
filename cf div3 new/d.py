import bisect
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    arr=[]
    for i in range(k):
        arr.append([r[i],l[i]])
    arr.sort()
    r.sort()
    q=int(input())

    qq=list(map(int,input().split()))
    for x in qq:
        index=bisect.bisect_left(r,x)
        li=arr[index][1]
        ri=arr[index][0]
        a=min(x,ri+li-x)-1
        b=max(x,ri+li-x)-1
        ss=s[a:b+1][::-1]
        s=s[:a]+ss+s[b+1:]
    print(s)

