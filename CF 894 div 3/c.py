for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr[0]>(10**5)*2:
        print('NO')
    else:
        newarr=[0]*arr[0]
        for ele in arr:
            newarr[ele-1]+=1
        s=0
        f=False
        if len(arr)==arr[0]:
            for i in range(len(newarr)-1,-1,-1):
                s+=newarr[i]
                if arr[i]!=s:
                    f=True
                    break
            if f:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')
