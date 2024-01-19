for _ in range(int(input())):
    n,a,q=map(int,input().split())
    s=input()
    if a==n:
        print('YES')
    else:
        pos=0
        f=False
        sums=a
        for ele in s:
            if ele=='+':
                pos+=1
                sums+=1
            else:
                sums-=1
            if sums==n:
                f=True
                break
        if f:
            print('YES')
        else:
            if pos+a<n:
                print('NO')
            else:
                print('MAYBE')
