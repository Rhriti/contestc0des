import heapq as hq
import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    modu=[ele%k for ele in h]
    zeromod=[]
    restmod=[]
    order=[]

    for i in range(len(modu)):
        if modu[i]==0:
            zeromod.append(i)
            order.append(i+1)
        else:
            restmod.append([-modu[i],i])
    restmod.sort()
    for ele in restmod:
        order.append(ele[1]+1)
    for ele in order:
        print(ele,end=' ')
    print()

    