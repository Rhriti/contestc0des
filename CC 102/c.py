for _ in range(int(input())):
    n,k=map(int,input().split())
    rem=k%n 
    val=k//n
    if n==2:
        if k%2==1:
            print(*[k//2,(k//2)+1])
        else:
            print(-1)
    else:
        if rem==0:#base case
            arr=[k//n]*n 
            for i in range(n//2):
                if i%2==0:
                    arr[2*i]=val+1 
                else:
                    arr[2*i]=val-1
            if 0 in arr:
                print(-1)
            else:
                print(*arr)
        else:
            if (rem+val)==1:
                arr=[val]*(n-2)
                for i in range((n-2)//2):
                    if i%2==0:
                        arr[2*i]=val+1
                    else:
                        arr[2*i]=val-1
                arr.append(rem)
                arr.append(val)
                if 0 in arr:
                    print(-1)
                else:
                    print(*arr)
            else:print(-1)
        
        
            
        
        
        
        
        
        
        