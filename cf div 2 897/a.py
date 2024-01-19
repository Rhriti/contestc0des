for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    arr=[]
    for i in range(len(lst)):
        arr.append([lst[i],i])
    arr.sort()
    d=[i for i in range(1,n+1)]
    d.sort(reverse=True)
    newarr=[None for _ in range(n)]
    for i in range(n):
        newarr [  arr[i][1]   ]=d[i]
    for ele in newarr:
        print(ele,end=' ')    