for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    ori=[]
    for ele in d:
        if ele%2==0:
            ori.append(0)
        else:
            ori.append(1)
    d.sort()
    want=[]
    for ele in d:
        if ele%2==0:
            want.append(0)
        else:
            want.append(1)
    if want==ori:
        print('YES')
    else:
        print('NO')
    