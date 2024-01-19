for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>=(n//2)+n:
        arr=[1 for _ in range(n//2)]
        for _ in range(n//2):arr.append(2)
        left=k-((n//2)+n)
        if left%2==1:
            print(-1)
        else:
            for i in range(n):
                cut=10**5-2
                if cut<=left:
                    left-=cut
                    arr[i]+=cut
                else:
                    arr[i]+=left
                    left=0
                
            if left==0:print(*arr)
            else:print(-1)
    
    else:print(-1)
