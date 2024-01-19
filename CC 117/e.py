import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    d=abs(a-b)
    n=math.floor(math.sqrt(2*d))
    if n*(n+1)==2*d:print(n+1)
    else:
        od=d
        pres=0
        for i in range(1,10**9):
            pres+=1
            d+=i
            news=2*(d+pres)
            nnew=math.floor(math.sqrt(news))
            if nnew*(nnew+1)==news:
                print(nnew)
                break
            
            pres+=1
            d-=i
            news=2*(d+pres)
            nnew=math.floor(math.sqrt(news))
            if nnew*(nnew+1)==news:
                print(nnew)
                break
            
            
            
            
            
            
            
            
            
    
    