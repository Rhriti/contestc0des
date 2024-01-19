for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    f=True
    for ele in d:
        if ele<0:
            f=False
            print(ele)
            break
    if f:
        print(max(d))
            