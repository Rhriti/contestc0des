from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    #base case
    # if n==3:
    #     if c[0]==c[1]==c[2]:
    #         print('YES')
    #     else:
    #         print('NO')
    # else:
    agecol=c[0]
    pichecol=c[-1]
    c1=0
    i1=None
    for i in range(len(c)):
        if c[i]==agecol:
            c1+=1
            i1=i
        if c1==k:
            break
    c2=0
    i2=None
    for i in range(len(c)-1,-1,-1):
        if c[i]==pichecol:
            c2+=1
            i2=i
        if c2==k:
            break
    g=Counter(c)
    if (c1==k and c2==k and i2 is not None and i1 is not None and i2>i1) :
        print('YES')
    elif c[0]==c[-1] and g[c[0]]-2>=k-2:
        print('YES')
    else:
        print('NO')
    

               