import math
for _ in range(int(input())):
    n=int(input())
    xp,xn,yp,yn=False,False,False,False
    for _ in range(n):
        x,y=map(int,input().split())
        if x>0:xp=True
        if x<0:xn=True
        if y>0:yp=True
        if y<0:yn=True

    if xp and xn and yp and yn:print('NO')
    else:print('YES')