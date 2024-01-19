for _ in range(int(input())):
    x,y,n=map(int,input().split())
    arr=[y]*n
    c=1
    for i in range(len(arr)-2,-1,-1):
        arr[i]=arr[i+1]-c
        c+=1
    if x<=arr[0]:
        print(x,end=' ')
        for i in range(1,len(arr)):
            print(arr[i],end=' ')
        print()
    else:
        print(-1)
   