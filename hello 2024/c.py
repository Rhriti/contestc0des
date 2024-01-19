for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    one=float('inf')
    two=float('inf')
    c=0
    for ele in arr:
        if ele>max(one,two):
            if one >two:two=ele
            else:one=ele
            c+=1
        elif ele<=min(one,two):
            if one<two:one=ele
            else:two=ele
        else:
            if one<two:two=ele
            else:one=ele
    print(c)
