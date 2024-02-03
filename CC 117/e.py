import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    d=abs(a-b)
    i=0
    j=10**5
    f=False
 
    while i<=j:
        mid=(i+j)//2
        if mid*(mid+1)//2>d:
            j=mid-1
        elif mid*(mid+1)//2<d:
            i=mid+1
        else:f=True;break


    if f:print(mid);continue
    if mid*(mid+1)//2<d:mid+=1

    final=mid*(mid+1)//2
    
    if final%2==d%2:print(mid)
    elif (final+mid+1)%2==d%2:print(mid+1)
    elif(final+mid+1+mid+2)%2==d%2:print(mid+2)
    else:print(-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
    
    