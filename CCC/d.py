for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxm=max(arr)
    sets={arr[0]}
    newarr=[arr[0]]

    for i in range(1,n):
        if arr[i] not in sets:
            sets.add(arr[i])
            newarr.append(arr[i])
        else:
            newarr.append(maxm)
    print(*newarr)