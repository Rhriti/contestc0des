arr=set()
import math
def f(n):
    while n%2==0:
        arr.add(2)
        n=n//2
    for i in range(3,int(math.sqrt(n))+1):
        while n%i==0:
            n=n//i
            arr.add(i)
    if n!=1:
        arr.add(n)
    print(arr)

f(31)