import math
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    if n==1:
        print(1)
    else:
        lcm=1
        c=1
        for i in range(1,n):
            lcm=math.lcm(lcm,s[i])
            c+=1
            if lcm>n:
                c-=1
                break
        print(f'c is {c} c+1 is {c+1}')


