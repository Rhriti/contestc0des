  
import math
 
def is_prime(n ):
     
    # Check if n=1 or n=0
    if n <= 1:
        return "false"
     
    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return "true"
     
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return "false"
     
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "false"
 
    return "true"

c=0
for i in range(1,10**6):
    x=is_prime(i)
    if x=='true':c+=1
print(c)
 
