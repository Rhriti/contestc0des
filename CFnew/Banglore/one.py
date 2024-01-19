for _ in range(int(input())):
    n,k,q=map(int,input().split())
    d=list(map(int,input().split()))
    count=0
    arr=[]
    for ele in  d:
        if ele<=q:
            count+=1
        else:
            if count>=k:
                arr.append(count)
            count=0
    if count>=k:
        arr.append(count)
    print(arr)