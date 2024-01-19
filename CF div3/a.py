import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    diff=abs(a-b)
    print(int(math.ceil(diff/(2*c))))
    