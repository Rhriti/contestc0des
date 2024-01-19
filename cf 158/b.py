for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    final=0
    s=set()
    
    for i in range(n-1):
        if arr[i+1]==0:continue
        else:
            if arr[i+1]>arr[i]:
                if arr[i] not in s:
                    s.add(arr[i]);final+=abs(arr[i+1]-arr[i])
                    

    for i in range(1,n):
        if arr[i]!=0 and arr[i-1]==0:final+=1
    print('ans',final)

     
