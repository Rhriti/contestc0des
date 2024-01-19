import math
for _ in range(int(input())):
    n=int(input())
    if n<7:
        print('NO')
    else:
        kmin=2
        kmax=max(math.ceil((-1+(4*n-3)**(.5))/2),
                 math.ceil((1+(4*n-3)**(.5))/2))
        f=False
        for k in range(kmin,kmax+1):
            try:
                x=math.log(n*(k-1)+1,k)
                if x==int(x) and x>=3:
                    f=True
                    break
            except:
                pass
        if f:
            print('YES')
        else:
            print('NO')

                    
        
    