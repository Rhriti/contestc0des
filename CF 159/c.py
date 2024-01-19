import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:
        print(1)
    else:

        newarr=[]
        for i in range(1,n):newarr.append(arr[i]-arr[i-1])
        if all(element==0 for element in newarr):
            print(1)
            continue

        prev=newarr[0]
        for i in range(1,len(newarr)):
            prev=math.gcd(prev,newarr[i])
        
        # print(prev)
        maxm=max(arr)
        if maxm-prev in arr:
            arr.append(maxm+prev)
        else:
            arr.append(maxm-prev)

        op=0
        for ele in arr:
            op+=abs(ele-maxm)//prev
            # print(op)
        print('ans',op)

