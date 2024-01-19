#sqrt n time me
import math
def check_prime(n):
    arr=set()
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            arr.add(i)
    if len(arr)==0:
        print('prime hai')
    else:
        print('prime nahi hai')

check_prime(23)