from collections import defaultdict
import math
for _ in range(int(input())):
    n=int(input())
    x=defaultdict(int)
    y=defaultdict(int)
    sumd=defaultdict(int)
    diffd=defaultdict(int)
    for _ in range(n):
        a,b=map(int,input().split())
        x[a]+=1
        y[b]+=1
        sumd[a+b]+=1
        diffd[b-a]+=1
    s=0
    for val in sumd.values():
        if val>1:
            s+=math.factorial(val)/math.factorial(val-2)
    for val in diffd.values():
        if val>1:
            s+=math.factorial(val)/math.factorial(val-2)
    for val in x.values():
        if val>1:
            s+=math.factorial(val)/math.factorial(val-2)
    for val in y.values():
        if val>1:
            s+=math.factorial(val)/math.factorial(val-2)
    print(int(s))
    print('upar')

