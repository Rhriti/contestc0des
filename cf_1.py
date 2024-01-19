for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    d=[]
    sums=0
    for i in range(len(arr)-1):
        d.append(abs(arr[i]-arr[i+1]))
        sums+=abs(arr[i]-arr[i+1])
    d.sort()
    d=list(reversed(d))
    sub=sum(d[:k-1])
    print(sums-sub)    