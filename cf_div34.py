ps=[]
presum=0
for i in range(1,2*(10**5)+1):
    presum+=i
    ps.append(presum)

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    sums=ps[n-1]
    arr.sort()
    s=set()
    f=False
    for i in range(len(arr)-1):
        diff=arr[i+1]-arr[i]
        if diff in s or diff<0 or diff>sums-1:
            f=True
            break
        else:
            s.add(diff)
    if f:
        print('NO')
    else:
        print('YES')
    
