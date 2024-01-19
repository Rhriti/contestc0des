import math

def printDivisors(n) : 
    fac=[]
    i=1
    while i <= math.sqrt(n): 
        
        if (n % i == 0) : 
            if (n / i == i) : 
                fac.append(i) 
            else : 
                fac.append(i)
                fac.append(n//i)
        i = i + 1
    return fac
import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    fac=printDivisors(n)
    c=0
    for ele in fac:
        g=0
        for i in range(n-ele):
            g=math.gcd(g,abs(arr[i+ele]-arr[i]))

        if g!=1:c+=1

    print(c)

        
            





