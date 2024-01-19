def gcd(x,y):
    if y==0:
        return abs(x)
    return gcd(y,x%y)

def LCM(x,y):
    return x*y//gcd(x,y)
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    xarr=n//x
    yarr=n//y
 
 
    common=n//LCM(x,y)   
    xarr-=common
    yarr-=common
    
    sumy=((yarr)*(yarr+1))//2
    sumx=xarr*(2*n-xarr+1)//2
    
    print(int(sumx-sumy))