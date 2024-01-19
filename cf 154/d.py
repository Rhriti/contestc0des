#main logic is at max n-1 operations are required to make 
#array striclty increasing
#since all elements of array are positive, subarray to its right must be multiplied with positve X
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    prev=arr[-1]
    suffix=[0 for _ in range(n)]
    for i in range(n-2,-1,-1):
        if arr[i]<prev:
            suffix[i]=suffix[i+1]
        else:
            suffix[i]=suffix[i+1]+1
        prev=arr[i]
    #prefix ke lie jitne ups hai wo jodo
    f=False
    prefix=[0 for _ in range(n)]
    prev=arr[1]
    for i in range(2,n):
        if arr[i]>=prev:
            arr[i-1]=arr[i-2]+1
        else:
            arr[i-1]=arr[i-2]

            