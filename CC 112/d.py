t,s=map(int,input().split())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()

    if n==1:print(arr[0])
    
    sums=0
    if n%2==0:
        for i in range(2,n,2):sums+=arr[i]
        sums+=arr[1]
    else:
        for i in range(1,n,2):sums+=arr[i]
        sums+=arr[0]
    print(sums)

           