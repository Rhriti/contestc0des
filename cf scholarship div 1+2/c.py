import math
for _ in range(int(input())):
    x=int(input())
    arr=[]
    def printDivisors(n) :
        
        # Note that this loop runs till square root
        i = 1
        while i <= math.sqrt(n):
            
            if (n % i == 0) :
                
                # If divisors are equal, print only one
                if (n / i == i) :
                    arr.append(i)
                    arr.append(i)
                else :
                    # Otherwise print both
                    arr.append(i)
                    arr.append(i)
                    arr.append(int(n/i))
                    arr.append(int(n/i))
            i = i + 1
    printDivisors(x)
    arr.sort(reverse=True)
    ans=[x]
    for ele in arr:
        #base
        if x-ele>0:
            x=x-ele
            ans.append(x)
        if x==1:
            break
    print('ans',ans)








