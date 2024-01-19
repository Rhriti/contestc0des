for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    d.sort()
    s=set(i for i in range(1,n+1))
    diff=[d[0]]
    for i in range(len(d)-1):
        diff.append(d[i+1]-d[i])

    c=0
    sums=None
    for ele in diff:
        if ele in s:
            s.remove(ele)
        else:
            c+=1
            sums=ele
    if c==0:
        print('YES')
    else:
        if c==1:
            if len(s)==2 and s.pop()+s.pop()==sums:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')


