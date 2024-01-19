from sys import stdin
def input(): return stdin.readline().rstrip("\r\n")

# Python program to print prime factors

import math

# A function to print all prime factors of
# a given number n
def primeFactors(n,count):
	# Print the number of two's that divide n
	while n % 2 == 0:
		count.append(2)
		n = n // 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i ad divide n
		while n % i== 0:
			count.append(i)
			n = n // i
			
	if n > 2:
		count.append(n)

     
		

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    s=1
    for ele in arr:s*=ele
    if n+k>6:print('NO')
    else:
        if 2023%s==0:
            s=2023//s 
            count=[]
            primeFactors(s,count)
            if k<=len(count):
                print('YES')
                final=1
                for i in range(len(count)-k):
                    final*=count[i]
                count=count[len(count)-k:]
                print(final,*count)

            else:
                print('NO')
        else:print('NO')