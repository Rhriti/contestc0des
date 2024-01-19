for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    diff=[]
    f=False
    for i in range(len(d)-1):
        if d[i+1]>=d[i]:
            diff.append(d[i+1]-d[i])
        else:
            f=True
            break
    if f:
        print(0)
    else:
        mingap=min(diff)
        print((mingap//2)+1)
    
