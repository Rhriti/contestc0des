from sys import stdin
def input(): return stdin.readline().rstrip("\r\n")


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(0,n,2):arr[i]=-arr[i]
    s=0;pres={0};f=False

    for ele in arr:
        s+=ele
        if s in pres:f=True
        else:pres.add(s)

        if f:break
    if f:print('YES')
    else:print('NO')
