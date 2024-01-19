for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    v=set()
    c=0
    for ele in arr:
        if ele-1 in v: 
            v.add(ele)
        else:
            c+=1
            v.add(ele)
    print('ans',c-1)