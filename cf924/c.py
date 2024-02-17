
import math
def printDivisors(n):

    i=1
    while i<=math.sqrt(n):
        if (n%i==0):
            if (n//i==i):
                if i%2==0 :final.add(i)
            else:
                if i%2==0 :final.add(i)
                if (n//i) %2==0:final.add(n//i)
        i+=1
  
for _ in range(int(input())):
    n,x=map(int,input().split())
    final=set()
    printDivisors(n-x)
    printDivisors(n+(x-2))
    c=0
    for ele in final:
        k=(ele+2)//2
        if k>=x:c+=1
    print(c)

   
   
      
        

 
