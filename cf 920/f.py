for _ in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=[]
    for _ in range(q):
        s,d,k=map(int,input().split())
        c=0
        i=s-1
        coeff=1
        for _ in range(k):
            c+=coeff*arr[i]
            i+=d 
            coeff+=1
        ans.append(c)
    print(*ans)

