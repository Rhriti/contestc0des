for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    rem=k%(n+1)
    if rem==0:
        for ele in arr:
            print(ele,end=' ')
    
    else:
        v=set()
        for i in range(n+1):
            v.add(i)
        for ele in arr:
            v.remove(ele)
    
        miss=[v.pop()]
        miss.extend(arr[:len(arr)-(rem-1)])
        final=arr[len(arr)-(rem-1):]
        final.extend(miss)
        for i in range(len(final)-1):
            print(final[i],end=' ')
        print()