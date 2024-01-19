import bisect
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    q=int(input())
    final=[]
    for _ in range(q):
        s,p=map(int,input().split())
        count=0
        for i in range(len(arr)-1):
            
            sli=bisect.bisect_left(arr,s-arr[i],i+1)
            sri=bisect.bisect_right(arr,s-arr[i],i+1)
            if sri!=sli:
                pli=bisect.bisect_left(arr,p/arr[i],sli,sri-1)
                pri=bisect.bisect_right(arr,p/arr[i],sli,sri-1)
                if pli==pri:
                    if arr[pri]==p/arr[i]:
                        count+=pri-pli+1
                else:
                    count+=pri-pli+1
    
        final.append(count)
    for ele in final:
        print(ele,end=' ')
    print()
    
