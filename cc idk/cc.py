for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    def check(t):
        j=0
        for i in range(1,len(t)-1):
            if t[i-1]<t[i]>t[i+1]:
                j+=1
            elif t[i-1]>t[i]<t[i+1]:
                j-=1
            else:
                return False
            if j<-1 or j>1:
                return False

        return True
            
    if n%2==1:
        #upar niche
        index=(n//2)+1
        newarr=[None for _ in range(n)]
        j=0
        for i in range(index):
            newarr[j]=arr[i]
            j+=2
        j=1
        for i in range(index,n):
            newarr[j]=arr[i]
            j+=2
     
        #niche upar 
        newarr2=[None for _ in range(n)]
        index=n//2
        j=0
        for i in range(index,n):
            newarr2[j]=arr[i]
            j+=2
        j=1
        for i in range(index):
            newarr2[j]=arr[i]
            j+=2
        
        #check
        if check(newarr):
            print(*newarr)
        elif check(newarr2):
            print(*newarr2)
        else:
            print(-1)
        
    else:
        newarr=[None for _ in range(n)]
        newarr2=[None for _ in range(n)]
        index=n//2
        j=0
        for i in range(index):
            newarr[j]=arr[i]
            j+=2
        j=1
        for i in range(index,n):
            newarr[j]=arr[i]
            j+=2
        j=0
        for i in range(index,n):
            newarr2[j]=arr[i]
            j+=2
        j=1
        for i in range(index):
            newarr2[j]=arr[i]
            j+=2
    
        if check(newarr):
            print(*newarr)
        elif check(newarr2):
            print(*newarr2)
        else:
            print(-1)
        

        



