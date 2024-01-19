import math
for _ in range(int(input())):
    l,r=map(int,input().split())
    if r==3:
        print(-1)
    else:
        if r-l>=1:
            if r%2==0:
                print(r//2,r//2)
            else:
                print((r-1)//2,(r-1)//2)
        else:
            
            def is_prime(n):
                if n < 2:
                    return False
                i = 2
                while i*i <= n:
                    if n % i == 0:
                        return False
                    i += 1
                return True
            if is_prime(l):
                print(-1)
            else:
                i=2
                while i<=math.sqrt(l):
                    if l%i==0:
                        nn=(l//i)-1
                        print(i,i*nn)
                        break
                    i+=1
    print('upar')
        