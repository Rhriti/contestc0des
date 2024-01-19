# Python program to print prime factors 

import math 
def primeFactors(n): 
    c=0
    while n % 2 == 0: 
        n = n / 2
 
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0: 
            c+=1
            n = n / i 
			
    if n > 2: 
        c+=1
    return c

for _ in range(int(input())):
    n=int(input())
    c=primeFactors(n)
    if c%2==0:print('Bob')
    else:print('Alice')