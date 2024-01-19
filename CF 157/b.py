for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()

    newarr=[]
    for i in range(n):
        j=i+n
        newarr.append([arr[i],arr[j]])
    count=0
   
    for i in range(len(newarr)-1):
        j=i+1
        count+=abs( newarr[j][0]-newarr[i][0]  )+abs(newarr[j][1]-newarr[i][1] )
    print(count)
    for i in range(len(newarr)):print(*newarr[i])
